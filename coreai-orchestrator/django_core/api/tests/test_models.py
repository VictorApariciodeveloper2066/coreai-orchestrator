import pytest
from django.contrib.auth.models import User
from api.models import AIQuery
from django.core.exceptions import ValidationError
from django.db import IntegrityError

@pytest.mark.django_db
class TestAIQueryModel:

    def test_create_query_success(self):
        """Prueba que un modelo válido se guarda correctamente."""
        user = User.objects.create_user(username="testuser")
        query = AIQuery.objects.create(
            user=user,
            prompt="¿Qué es SOLID?",
            status=AIQuery.Status.COMPLETED
        )
        assert query.id is not None
        assert query.status == "COMPLETED"

    def test_query_requires_user(self):
        """Prueba de Integridad: No debe permitirse una consulta sin usuario."""
        with pytest.raises(IntegrityError):
            AIQuery.objects.create(prompt="Prompt sin dueño")

    def test_default_status_is_pending(self):
        """Prueba de Regla de Negocio: Toda consulta nace como PENDING."""
        user = User.objects.create_user(username="newuser")
        query = AIQuery.objects.create(user=user, prompt="Test prompt")
        assert query.status == AIQuery.Status.PENDING