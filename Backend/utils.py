import re

def extract_youtube_video_id(youtube_url: str) -> str:
    """
    Extracts YouTube video ID from URL.
    Supports both full URLs and shortened links.
    """
    match = re.search(r"(?:v=|youtu\.be/)([^&\n?#]+)", youtube_url)
    return match.group(1) if match else None
