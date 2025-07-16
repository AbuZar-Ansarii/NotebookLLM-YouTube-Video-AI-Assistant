import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .utils import extract_youtube_video_id

load_dotenv()

class LLMService:
    """
    Handles LLM-based responses and transcript extraction.
    """

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0.7)
        self.parser = StrOutputParser()
        self.prompt = PromptTemplate(
            input_variables=["query", "transcript"],
            template="""
            You are a helpful AI tutor. Use the video transcript to answer the student's question.
            
            Transcript: {transcript}
            
            Question: {query}
            
            Answer:
            """
        )

    def get_transcript(self, video_id: str) -> str:
        """
        Fetch YouTube transcript by video ID.
        """
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item['text'] for item in transcript])

    def chat_with_transcript(self, url: str, query: str) -> str:
        """
        Handle AI Q&A over the YouTube transcript.
        """
        video_id = extract_youtube_video_id(url)
        if not video_id:
            return "Invalid YouTube URL."

        try:
            transcript = self.get_transcript(video_id)
        except Exception as e:
            return f"Transcript not available: {str(e)}"

        chain = self.prompt | self.llm | self.parser
        return chain.invoke({"query": query, "transcript": transcript}).strip()
