# django_core/tests/test_sanity.py

def test_basic_arithmetic():
    """
    Test de nivel 0: Verificar que Pytest está configurado.
    Principio Senior: 'Test simple primero, complejidad después'.
    """
    expected = 2
    actual = 1 + 1
    
    # Usamos assert simple de Pytest (más legible que self.assertEqual)
    assert actual == expected, f"Error: se esperaba {expected} pero se obtuvo {actual}"