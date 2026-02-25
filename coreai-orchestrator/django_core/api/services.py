import requests
import logging
from dataclasses import dataclass
from typing import Dict, Any, Optional
from decouple import config
from .ai_interface import AIProcessorInterface

# 1. AGREGAR esto al inicio (Tu nuevo modelo de datos)
@dataclass(frozen=True)
class AIInferenceResult:
    user_id: int
    result: str
    persisted: bool
    status: str = "completed"
    error_detail: Optional[str] = None

# 2. SUSTITUIR tu clase vieja por esta versión mejorada
class FastAPIProcessor(AIProcessorInterface):
    def __init__(self) -> None:
        # Ahora usamos config() en lugar de texto plano
        self.url: str = config('AI_PROCESSOR_URL', default="http://ai_processor:8080/analyze")
        self.timeout: int = config('AI_TIMEOUT', default=5, cast=int)

    def process(self, text: str) -> AIInferenceResult:
        """
        Observa que el Type Hint ahora dice que devolvemos 
        un objeto AIInferenceResult, no un dict.
        """
        try:
            response = requests.post(
                self.url, 
                json={"text": text}, 
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()

            # Mapeamos el JSON a la DataClass
            return AIInferenceResult(
                user_id=data.get("user_id", 0),
                result=data.get("result", ""),
                persisted=data.get("persisted", False)
            )

        except Exception as e:
            # En lugar de devolver un dict con error, devolvemos el objeto con status "error"
            return AIInferenceResult(
                user_id=0,
                result="",
                persisted=False,
                status="error",
                error_detail=str(e)
            )