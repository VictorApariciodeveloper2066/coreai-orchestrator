from rest_framework.views import APIView
from rest_framework.response import Response

class AIQueryView(APIView):
    """
    Vista de Django que maneja las consultas. 
    Nivel Senior: No importamos el servicio arriba para evitar el ciclo.
    """
    def get_processor(self):
        # Importación "Lazy" (perezosa) para romper el Import Circular
        from .services import FastAPIProcessor
        return FastAPIProcessor()

    def post(self, request):
        user_input = request.data.get('text')
        if not user_input:
            return Response({"error": "No text provided"}, status=400)
        
        processor = self.get_processor()
        result = processor.process(user_input)
        
        # Manejo profesional del resultado basado en el objeto (Día 3)
        if result.status == "error":
            return Response({"error": result.error_detail}, status=502)

        return Response({
            "analysis": result.result,
            "success": result.persisted
        })