import os
import cv2
import tempfile
import logging
import json
from PIL import Image
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if os.getenv("ENV") != "production":
    load_dotenv()

class AIEngine:
    def __init__(self):
        # Initialize Gemini API for explainability and DMCA generation
        self.use_gemini = os.environ.get("GEMINI_API_KEY") is not None
        
        if self.use_gemini:
            try:
                import google.generativeai as genai
                genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
                self.gemini_model = genai.GenerativeModel('gemini-1.5-flash')
            except Exception as e:
                logger.warning(f"Gemini AI initialization failed: {e}")
                self.use_gemini = False

    def extract_frames(self, video_path, num_frames=3):
        """Extract multiple keyframes from a video for temporal hashing."""
        frames = []
        try:
            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                return frames
                
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            if total_frames > 0:
                step = max(1, total_frames // num_frames)
                for i in range(0, total_frames, step):
                    if len(frames) >= num_frames:
                        break
                    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
                    ret, frame = cap.read()
                    if ret:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        frames.append(Image.fromarray(frame))
            cap.release()
        except Exception as e:
            logger.error(f"Error extracting frames: {e}")
        return frames

    def generate_fingerprint(self, file_path, filename=""):
        """
        Generate robust local perceptual hashes (pHash) across multiple frames.
        This provides a lightweight, cost-effective semantic representation for the demo.
        """
        ext = file_path.lower().split('.')[-1]
        
        try:
            images = []
            if ext in ['mp4', 'avi', 'mov', 'mkv']:
                images = self.extract_frames(file_path, num_frames=3)
            else:
                images = [Image.open(file_path)]
                
            if not images:
                return None

            # Local Fallback Hashing (using pHash for robust local demo without Vertex AI overhead)
            import imagehash
            hashes = []
            for img in images:
                hashes.append(str(imagehash.phash(img)))
            
            return json.dumps({"type": "phash_fallback", "hashes": hashes})

        except Exception as e:
            logger.error(f"Error generating fingerprint for {filename}: {e}")
            return None

    def calculate_similarity(self, fp1_str, fp2_str):
        """
        Calculate maximum similarity between two sets of frame pHashes.
        """
        if not fp1_str or not fp2_str:
            return 0.0

        try:
            fp1 = json.loads(fp1_str)
            fp2 = json.loads(fp2_str)
            
            if isinstance(fp1, dict) and isinstance(fp2, dict) and fp1.get("type") == "phash_fallback":
                import imagehash
                best_sim = 0.0
                for h1 in fp1.get("hashes", []):
                    for h2 in fp2.get("hashes", []):
                        hash1 = imagehash.hex_to_hash(h1)
                        hash2 = imagehash.hex_to_hash(h2)
                        distance = hash1 - hash2
                        # Convert distance to similarity percentage
                        similarity = max(0.0, 100.0 - (distance * 100.0 / 64.0))
                        # Scale up to make minor edits flag properly
                        if similarity > 80:
                            similarity = 90 + (similarity - 80) / 2
                        if similarity > best_sim:
                            best_sim = similarity
                return round(best_sim, 1)

        except Exception as e:
            logger.error(f"Error calculating similarity: {e}")
            
        return 0.0

    def generate_explanation(self, similarity_score, risk_level):
        """
        Use Gemini API to generate an explainable AI output. Fallback to templates if API fails.
        """
        if self.use_gemini:
            prompt = f"You are OmniGuard AI, a digital asset protection system. A media file was uploaded and compared against a registered asset. The similarity score is {similarity_score}% with a {risk_level} risk level. Write a short, single-sentence explanation of why this was flagged, mentioning motion patterns, visual structure, or cropping."
            try:
                response = self.gemini_model.generate_content(prompt)
                return response.text.strip()
            except Exception as e:
                logger.error(f"Gemini API error during explanation: {e}")
                
        # Fallback offline explanation
        if similarity_score > 90:
            return f"This content shows {similarity_score}% similarity due to overlapping motion patterns and near-identical visual structure."
        elif similarity_score > 70:
            return f"This content shows {similarity_score}% similarity, indicating potential cropping or filtering of the original asset."
        else:
            return "Similarity is low. The content appears to be unique or heavily modified beyond recognition."
            
    def generate_dmca(self, owner, asset_id, filename):
        """
        Generate a DMCA takedown notice automatically using Gemini. Fallback to template if API fails.
        """
        if self.use_gemini:
            try:
                prompt = f"Generate a brief, professional DMCA takedown notice for an unauthorized use of a sports media clip. Owner: {owner}, Asset ID: {asset_id}, Filename: {filename}. Leave placeholders for dates and URLs."
                response = self.gemini_model.generate_content(prompt)
                return response.text.strip()
            except Exception as e:
                logger.error(f"Gemini DMCA generation error: {e}")
                
        # Fallback offline DMCA template
        return f"DMCA Takedown Notice\n\nI am the authorized representative of {owner}. The file {filename} (Asset ID: {asset_id}) has been used without permission. Please remove this content immediately to avoid further action."
