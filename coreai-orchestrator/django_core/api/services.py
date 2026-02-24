import requests
from .ai_interface import AIProcessorInterface

class FastAPIProcessor(AIProcessorInterface):
    def __init__(self, endpoint_url="http://ai_processor:8080/analyze"):
        self.url = endpoint_url

    def process(self, text: str) -> dict:
        try:
            response = requests.post(self.url, json={"text": text}, timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}