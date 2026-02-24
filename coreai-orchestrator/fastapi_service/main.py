from fastapi import FastAPI, Depends, Header, HTTPException
from .services import AIService  # Importamos nuestra lógica
from .auth import get_current_user

app = FastAPI(title="CoreAI Processor")
#data
@app.post("/process-ai/")
async def process_ai(
    input_text: str, 
    token: str = Header(...), 
    user: dict = Depends(get_current_user)
):
    # 1. Llamamos al servicio para procesar (SRP)
    result = await AIService.process_text_task(input_text)
    
    # 2. Preparamos el reporte
    report_data = {
        "model_used": "TA",
        "input_data": input_text,
        "output_data": result,
        "execution_time": 0.5, # Simulado
        "status": "completed"
    }
    
    # 3. Llamamos al servicio para reportar (SRP)
    reported = await AIService.report_to_django(report_data, token)
    
    if not reported:
        # Podríamos loguear esto, pero no detenemos la respuesta al usuario
        print("Warning: Could not persist data in Django")

    return {
        "user_id": user["user_id"],
        "result": result,
        "persisted": reported
    }