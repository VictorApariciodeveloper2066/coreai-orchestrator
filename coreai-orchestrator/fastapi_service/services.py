import httpx
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class AIService:
    # REEMPLAZO: Separamos las responsabilidades en métodos pequeños (< 10 líneas)
    
    @staticmethod
    async def process_text_task(text: str) -> str:
        """Simula el procesamiento de IA."""
        # En el futuro, aquí llamarás a un modelo real (OpenAI, Llama3, etc.)
        return f"Processed: {text.upper()}"

    @staticmethod
    async def report_to_django(report_data: Dict[str, Any], token: str) -> bool:
        """
        Envía el resultado a Django para persistencia.
        Responsabilidad única: Comunicación externa.
        """
        django_url = "http://web_django:8000/api/save-report/" # Moveremos esto a .env luego
        headers = {"Authorization": f"Bearer {token}"}
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(django_url, json=report_data, headers=headers, timeout=5.0)
                return response.status_code == 201
        except Exception as e:
            logger.error(f"Failed to reach Django: {e}")
            return False