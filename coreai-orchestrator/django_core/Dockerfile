# Usamos una imagen de Python ligera pero completa para desarrollo
FROM python:3.12-slim

# Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Instalamos dependencias del sistema necesarias para PostgreSQL y compilación
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalamos las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# Exponemos el puerto de Django
EXPOSE 8000

# Comando para arrancar (se sobreescribirá en docker-compose para las migraciones)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]