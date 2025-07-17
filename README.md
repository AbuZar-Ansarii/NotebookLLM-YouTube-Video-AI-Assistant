# 📚 YouTube Learning AI Assistant – NotebookLM Clone

An AI-powered system that lets you **chat with YouTube videos** and **listen to transcripts**.
An AI-powered learning assistant that lets you chat with YouTube videos, extract transcripts, and listen to the content.
Inspired by Google NotebookLM, built with FastAPI, LangChain, Gemini Pro, Streamlit & Docker.

# Images
<img width="1920" height="1080" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/9e9a62a1-a14f-4f16-8936-338a3a94bc70" />
<img width="1920" height="1080" alt="Screenshot (48)" src="https://github.com/user-attachments/assets/84aa8b1a-0004-407a-8f92-02ff30e8e9ea" />
<img width="1920" height="1080" alt="Screenshot (49)" src="https://github.com/user-attachments/assets/48c01ed3-87c5-4082-a48c-246ac662fac6" />
<img width="1920" height="1080" alt="Screenshot (52)" src="https://github.com/user-attachments/assets/47ad5667-9526-4410-a7ba-9012ab308b21" />

## 🎯 Features

- Extract YouTube video transcripts  
- Ask contextual questions using **Gemini Pro LLM (LangChain)**  
- Convert transcripts to audio with **gTTS**  
- Interactive **Streamlit frontend**  
- **FastAPI backend** handling all AI logic  
- Fully **Dockerized** & deployment ready  

---

## 🧰 Tech Stack

| Layer        | Technology                     |
|--------------|-------------------------------|
| Backend API  | FastAPI, LangChain, Gemini API |
| Frontend UI  | Streamlit                     |
| LLM          | Google Gemini 1.5 (via LangChain) |
| Audio        | gTTS (Text-to-Speech)         |
| Deployment   | Docker, Docker Compose        |

---
# Add File 📂

Please add .env file to backend folder 
content - GEMINI_API_KEY = "YOUR API KEY"

## ⚙️ Setup & Run

### 1️⃣ Clone the repo

```bash
git clone https://github.com/AbuZar-Ansarii/NotebookLLM-YouTube-Video-AI-Assistant.git
cd youtube-learning-assistant

## 📂 Project Structure

youtube-learning-assistant/
├── backend/ # FastAPI API (LLM logic here)
├── frontend/ # Streamlit UI (API calls only)
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md


---



