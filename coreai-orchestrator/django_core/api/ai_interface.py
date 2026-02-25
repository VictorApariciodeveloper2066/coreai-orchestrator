from rest_framework.views import APIView
from rest_framework.response import Response
from .services import FastAPIProcessor

# ai_interface.py

class AIQueryView(APIView):
    processor = FastAPIProcessor()

    def post(self, request):
        user_input = request.data.get('text')
        if not user_input:
            return Response({"error": "No text provided"}, status=400)
        
        # 1. Llamada al servicio (Ahora devuelve la DataClass que creamos)
        result = self.processor.process(user_input)
        
        # 2. REEMPLAZO: Manejo de errores basado en el estado del objeto
        if result.status == "error":
            return Response({
                "error": "AI_SERVICE_ERROR",
                "details": result.error_detail
            }, status=502) # Bad Gateway: El servicio de atrás falló
        
        # 3. REEMPLAZO: Respuesta exitosa usando atributos (no llaves [''])
        # Aquí tú controlas exactamente qué nombres de campos ve el frontend
        return Response({
            "analysis_result": result.result,
            "is_persisted": result.persisted,
            "user_id": result.user_id
        }, status=200)

