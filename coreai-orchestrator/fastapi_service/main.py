import logging
from fastapi import FastAPI, Depends, Header, HTTPException, Body
from pydantic import BaseModel, Field
from typing import Dict, Any
from .services import AIService 
from .auth import get_current_user


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="CoreAI Processor")

class AIRequest(BaseModel):
    text: str = Field(..., min_length=1, description="El texto a procesar por la IA")

class AIResponse(BaseModel):
    user_id: int
    result: str
    persisted: bool

@app.post("/process-ai/", response_model=AIResponse)
async def process_ai(
    request_data: AIRequest, 
    token: str = Header(...), 
    user: dict = Depends(get_current_user)
):
    # 1. Ejecutar la tarea (Abstracción)
    result_text = await AIService.process_text_task(request_data.text)
    
    # 2. Disparar el reporte (Delegación)
    # Nota: No necesitamos armar el JSON aquí, la vista solo coordina.
    is_saved = await AIService.report_to_django(
        {"user": user["user_id"], "content": result_text}, 
        token
    )
    
    return {
        "user_id": user["user_id"],
        "result": result_text,
        "persisted": is_saved
    }