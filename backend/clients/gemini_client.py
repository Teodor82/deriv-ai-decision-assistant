"""Gemini LLM Client - Reusable async client for Google Gemini API."""
import os
from typing import Optional
import asyncio
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


class GeminiClient:
    """Client for interacting with Google Gemini API."""
    
    _instance: Optional["GeminiClient"] = None
    
    def __new__(cls):
        """Singleton pattern for client reusability."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Initialize Gemini client."""
        if self._initialized:
            return
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        self._initialized = True
    
    async def generate(self, prompt: str) -> str:
        """Generate text from a prepared prompt using Gemini.

        This method is intentionally simple: it accepts a prompt string and
        returns the model output. Prompt construction and any domain logic
        should live outside this class.
        """
        try:
            # genai client may be blocking; run in a thread to avoid blocking event loop
            return await asyncio.to_thread(self._sync_generate, prompt)
        except Exception as e:
            return f"Error generating content: {str(e)}"

    def _sync_generate(self, prompt: str) -> str:
        """Synchronous call into genai library; extracted for thread execution."""
        response = self.model.generate_content(prompt)
        return getattr(response, "text", str(response))
