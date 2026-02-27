import pytest
import requests
from api.services import FastAPIProcessor

class TestFastAPIProcessor:

    def test_process_success(self, mocker):
        """Test de éxito: Verifica el mapeo correcto del JSON al objeto."""
        mock_post = mocker.patch('requests.post')
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "result": "Success from AI",
            "status": "ok"
        }

        processor = FastAPIProcessor()
        result = processor.process("Hola IA")

        # Usamos los atributos reales de tu objeto
        assert result.result == "Success from AI"
        assert result.status != "error"

    def test_process_connection_error(self, mocker):
        """Test de error: Verifica el manejo de excepciones de red."""
        mock_post = mocker.patch('requests.post')
        mock_post.side_effect = requests.exceptions.ConnectionError()

        processor = FastAPIProcessor()
        result = processor.process("Hola IA")

        # Usamos los atributos de error definidos en tu vista/interfaz
        assert result.status == "error"
        # Verificamos que el detalle del error exista (ajusta el nombre si es necesario)
        assert hasattr(result, 'error_detail')