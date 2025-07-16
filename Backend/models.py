from pydantic import BaseModel

class YouTubeURL(BaseModel):
    url: str

class YouTubeID(BaseModel):
    id: str

class TranscriptResponse(BaseModel):
    transcript: str

class ChatRequest(BaseModel):
    url: str
    query: str

class ChatResponse(BaseModel):
    query: str
    response: str
