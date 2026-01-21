FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENV PYTHONPATH=/app
ENV APP_DB_PATH=/tmp/app.db

EXPOSE 8000

CMD ["python", "app/api.py"]
