## 🎯 Objetivo
Establecer la base de pruebas automatizadas para el orquestador y resolver problemas de acoplamiento detectados en la arquitectura de Django.

## 🛠️ Cambios Realizados
### Django Core
- **Testing:** Configuración de `pytest` y `pytest-django`. 
- **Mocking:** Implementación de tests de integración para `FastAPIProcessor` simulando respuestas de red.
- **Refactor:** Creación de `interfaces.py` para romper importaciones circulares entre vistas y servicios.
- **Lazy Loading:** Implementación de carga perezosa de servicios en `AIQueryView`.

### FastAPI Processor
- **Testing:** Configuración inicial de `pytest` y `pytest-asyncio`.
- **Estabilidad:** Corrección de versiones en `requirements.txt` (Django 5.1.6).

## 🚦 Cómo Probar
1. Levantar contenedores: `docker compose up -d --build`
2. Ejecutar tests en Django: `docker compose exec web_django pytest .`
3. Ejecutar tests en FastAPI: `docker compose exec ai_processor pytest .`

## 📸 Evidencia
- [X] Django Tests: 2 passed.
- [X] FastAPI Tests: 1 passed.