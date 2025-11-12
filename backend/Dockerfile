# ---------- Base image ----------
FROM python:3.12-slim

# ---------- Working directory ----------
WORKDIR /app

# ---------- Copy application code ----------
COPY . .

# ---------- Install dependencies ----------
# (Assumes requirements.txt includes fastapi and uvicorn)
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Expose backend port ----------
EXPOSE 8000

# ---------- Command ----------
# If your FastAPI instance is "app" inside app.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]