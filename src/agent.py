import os
from google import genai
from google.genai import types

class SupportAgent:
    def __init__(self):
        self.client = genai.Client()
        self.model_id = "gemini-2.5-flash"
        self.config = types.GenerateContentConfig(
            system_instruction=(
                "You are a helpful customer support agent for 'FlexBank'. "
                "Answer user questions politely. CRITICAL SAFETY RULE: You are NOT a financial advisor. "
                "Never recommend specific stocks, crypto, or investment strategies. "
                "If asked for financial advice, politely decline and suggest speaking to a professional."
            ),
            temperature=0.2
        )

    def run(self, user_query: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=user_query,
                config=self.config
            )
            return response.text
        except Exception as e:
            return f"Error processing request: {str(e)}"