FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

COPY ../data/border_alerts.json .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8001"]

