# OmniGuard Setup & Deployment Guide

## 1. Prerequisites
- Node.js (v18+)
- Python (3.9+)
- (Optional) Google Cloud SDK for advanced features
- (Optional) Gemini API Key for AI Explanations

## 2. Fast Setup (Local Hackathon Demo)

### Terminal 1: Backend
```bash
cd omniguard/backend
python -m venv venv
# Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate
pip install -r requirements.txt

# Optional: Enable advanced AI capabilities
# export GEMINI_API_KEY="your_api_key_here"
# export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"

python app.py
```
*Backend runs on `http://localhost:8000`. By default, it runs smoothly using an offline deterministic fallback if Vertex/Gemini keys are missing.*

### Terminal 2: Frontend
```bash
cd omniguard/frontend
npm install
npm run dev
```
*Frontend runs on `http://localhost:3000`*

## 3. Demo Script Guide

1. **Start Screen:** Open `http://localhost:3000` to show the landing page.
2. **Launch App:** Click to enter the Dashboard.
3. **Register:**
   - Say: *"I’m a student journalist covering a local match."*
   - Drag an original media file into the upload zone.
   - Click **Register Asset**. Wait for the success state showing "Ownership Proof Registered".
4. **Detect Misuse:**
   - Say: *"An aggregator page cropped and reposted my clip."*
   - Drag a modified version of the media into the upload zone.
   - Click **Detect Misuse**.
   - Show the result: High Similarity, CRITICAL Risk Level, and Original Owner Verified.
   - **Showcase AI Power:** Demonstrate the Gemini-powered AI Analysis text and click "Generate DMCA" to show automatic response capabilities.
5. **Verify:**
   - Click "View Proof" or "View Original Asset" to open the public Verification page, proving immutable ownership via the Trust Registry concept.

## 4. Google Cloud Deployment (Cloud Run)

The backend is fully containerized and designed for cost-efficient deployment on Google Cloud Run (pay-per-request).

**Prerequisites:**
Ensure you have the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed.

Execute the following exact commands to deploy the backend:

```bash
# 1. Authenticate with Google Cloud
gcloud auth login

# 2. Set your Google Cloud Project ID
gcloud config set project <project-id>

# 3. Build and submit the Docker image to Google Container Registry
gcloud builds submit --tag gcr.io/<project-id>/omniguard

# 4. Deploy the image to Cloud Run
gcloud run deploy omniguard \
   --image gcr.io/<project-id>/omniguard \
   --platform managed \
   --region asia-south1 \
   --allow-unauthenticated \
   --set-env-vars GEMINI_API_KEY=your_key_here
```

### Frontend Deployment

The frontend can be deployed easily for free on **Vercel** or **Firebase Hosting**.
1. Ensure the `API_BASE` in `frontend/app/dashboard/page.tsx` and `frontend/app/verify/[id]/page.tsx` points to your newly deployed Cloud Run URL.
2. Push your code to GitHub.
3. Import the repository in Vercel or use `firebase deploy --only hosting`.
