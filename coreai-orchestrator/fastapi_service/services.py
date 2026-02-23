import time
import httpx
import os

class AIService:
    """
    Clase encargada ÚNICAMENTE de la lógica de procesamiento de IA 
    y la comunicación con el núcleo de Django.
    """

    @staticmethod
    async def process_text_task(text: str) -> str:
        # Aquí iría la llamada real a OpenAI / HuggingFace
        # Por ahora, simulamos procesamiento
        time.sleep(0.5) 
        return f"AI Analysis Result: {text[::-1].upper()}"

    @staticmethod
    async def report_to_django(payload: dict, token: str):
        """
        Responsabilidad única: Notificar a Django sobre la tarea realizada.
        """
        django_url = os.getenv("DJANGO_API_URL", "http://web_django:8000/api/ai-queries/")
        headers = {"Authorization": f"Bearer {token}"}
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(django_url, json=payload, headers=headers)
                return response.status_code == 201
            except Exception as e:
                print(f"Error reporting to Django: {e}")
                return False