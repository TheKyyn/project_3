# Utilisation de l'image Python
FROM python:3.9-slim

# Copie des fichiers dans le conteneur
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]
