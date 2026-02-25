from rest_framework.views import APIView
from rest_framework.response import Response
from .services import FastAPIProcessor

class AIQueryView(APIView):
    # Inyectamos la dependencia a través de un atributo de clase o constructor
    processor = FastAPIProcessor()

    def post(self, request):
        user_input = request.data.get('text')
        if not user_input:
            return Response({"error": "No text provided"}, status=400)
        
        # La vista no sabe CÓMO se procesa, solo que el objeto tiene un método .process()
        result = self.processor.process(user_input)
        
        return Response(result)