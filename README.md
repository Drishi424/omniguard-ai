# OmniGuard AI – Scalable Digital Asset Protection System

OmniGuard AI is an AI-assisted system that detects unauthorized reuse of digital media using perceptual fingerprinting and Gemini-powered explainability, fully deployed on Google Cloud.

---

## 🧠 Problem Statement

Digital sports and media content is frequently stolen, edited, and redistributed across platforms. Traditional detection systems fail when content is:

- Cropped  
- Filtered  
- Trimmed  
- Re-encoded  

This makes ownership enforcement extremely difficult.

---

## 🚀 Solution Overview

OmniGuard AI enables content owners to:

1. **Register original media**
2. **Scan suspicious content**
3. **Detect similarity using multi-frame perceptual hashing**
4. **Understand why content was flagged (AI explanation)**
5. **Generate a DMCA takedown notice instantly**

---

## 🔄 How It Works

1. User uploads an original asset → system generates fingerprint  
2. New content is uploaded for verification  
3. Multi-frame pHash compares visual structure  
4. If similarity > threshold:
   - Gemini generates explanation  
   - System generates DMCA notice  
5. User can verify ownership via asset ID  

---

## 🔥 Core Features

- **Perceptual Hash Detection**  
  Robust detection even for edited/cropped media  

- **Explainable AI (Gemini 1.5)**  
  Human-readable reasoning for flagged content  

- **Auto DMCA Generator**  
  One-click legal notice generation  

- **Cloud-Native Deployment**  
  Fully deployed on Google Cloud Run (serverless, scalable)  

- **Duplicate Detection**  
  Prevents re-registering same content  

---

## ☁️ Google Technology Used

- **Google Cloud Run**  
  Serverless backend deployment (auto-scaling, pay-per-use)

- **Gemini API (Google AI)**  
  Used for:
  - Content explanation  
  - DMCA generation  

---

## 🌐 Live Demo

- **Frontend**  
  https://omniguard-frontend-1090729890343.asia-south1.run.app/

- **Backend API Docs**  
  https://omniguard-backend-1090729890343.asia-south1.run.app/docs

---

## 🧪 Demo Flow (For Judges)

1. Upload an original media file  
2. Upload a modified version  
3. Observe:
   - Similarity score  
   - AI explanation  
4. Click **Generate DMCA**  
5. Click **View Original Asset**

---

## ⚙️ Local Setup (Optional)

```bash
# Frontend
npm install
npm run dev

# Backend
python app.py
```

---

## 🏆 Highlights
- Fully deployed on Google Cloud
- Zero-idle-cost architecture
- Real-world piracy detection use case
- AI-powered legal automation

---

## 👥 Team
- **Drishi Kachchhawaha**
- **Vishv Gehlot**
