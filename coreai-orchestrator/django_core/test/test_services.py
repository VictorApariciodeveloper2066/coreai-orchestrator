# django_core/tests/test_services.py
import pytest
from unittest.mock import patch
from api.services import FastAPIProcessor, AIInferenceResult

@patch('api.services.requests.post')
def test_fastapi_processor_success(mock_post):
    """
    Test de Integración Mockeado.
    Sustituimos la llamada real a la red por una respuesta controlada.
    """
    # 1. REEMPLAZAR la respuesta real por un Mock
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "user_id": 1,
        "result": "TEST OK",
        "persisted": True
    }

    processor = FastAPIProcessor()
    result = processor.process("Hola mundo")

    # 2. Verificar que el contrato se cumple
    assert isinstance(result, AIInferenceResult)
    assert result.result == "TEST OK"
    assert result.status == "completed"

# import pytest
# from unittest.mock import patch
# from api.services import FastAPIProcessor, AIInferenceResult

# @patch('api.services.requests.post')
# def test_fastapi_processor_success(mock_post):
#     # Simulamos respuesta exitosa de FastAPI
#     mock_post.return_value.status_code = 200
#     mock_post.return_value.json.return_value = {
#         "user_id": 99,
#         "result": "Clean Code is Awesome",
#         "persisted": True
#     }

#     processor = FastAPIProcessor()
#     result = processor.process("Cualquier texto")

#     # Verificamos que nuestro código mapeó bien los datos a la DataClass
#     assert result.user_id == 99
#     assert result.result == "Clean Code is Awesome"
#     assert result.status == "success" # O el status que hayas definido por defecto