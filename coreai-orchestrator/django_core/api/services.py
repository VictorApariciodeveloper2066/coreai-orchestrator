import requests
import logging
from typing import Dict, Any, Union
from decouple import config  # Librería estándar para manejar .env
from .ai_interface import AIProcessorInterface

# Configuración de Logging profesional (Regla de Oro: No print)
logger = logging.getLogger(__name__)

class FastAPIProcessor(AIProcessorInterface):
    """
    Service responsible for communicating with the FastAPI AI Processor.
    Implements AIProcessorInterface to maintain decoupling.
    """

    def __init__(self) -> None:
        # Extraemos la URL del .env. Si no existe, lanzamos error en tiempo de inicio.
        self.url: str = config('AI_PROCESSOR_URL', default="http://ai_processor:8080/analyze")

    def process(self, text: str) -> Dict[str, Any]:
        """
        Sends text to the AI Processor and returns a structured dictionary.
        
        :param text: Raw text to be analyzed.
        :return: Dictionary with results or error key.
        """
        payload: Dict[str, str] = {"text": text}
        
        try:
            # Añadimos timeout explícito para evitar colgar el worker de Django
            response = requests.post(
                self.url, 
                json=payload, 
                timeout=config('AI_TIMEOUT', default=5, cast=int)
            )
            response.raise_for_status()
            
            # Type Hinting: Nos aseguramos de que lo que retorna es un dict
            result: Dict[str, Any] = response.json()
            return result

        except requests.exceptions.RequestException as e:
            # Logging profesional con contexto
            logger.error(f"Error communicating with AI Processor at {self.url}: {str(e)}")
            return {"error": "AI_SERVICE_UNAVAILABLE", "details": str(e)}