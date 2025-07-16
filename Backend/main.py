from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import YouTubeURL, YouTubeID, TranscriptResponse, ChatRequest, ChatResponse
from .llm_service import LLMService
from .utils import extract_youtube_video_id

app = FastAPI(title="YouTube Learning Assistant API")

llm_service = LLMService()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "API is running smoothly"}

@app.post("/generate_videoid", response_model=YouTubeID)
def generate_videoid(y_url: YouTubeURL):
    vid = extract_youtube_video_id(y_url.url)
    if not vid:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL.")
    return {"id": vid}

@app.post("/generate_transcript", response_model=TranscriptResponse)
def generate_transcript(y_id: YouTubeID):
    try:
        transcript = llm_service.get_transcript(y_id.id)
        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat", response_model=ChatResponse)
def chat(query_req: ChatRequest):
    try:
        response = llm_service.chat_with_transcript(query_req.url, query_req.query)
        return {"query": query_req.query, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
