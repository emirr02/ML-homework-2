FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Assuming an app.py exists or will exist, otherwise this is a placeholder generic command
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
