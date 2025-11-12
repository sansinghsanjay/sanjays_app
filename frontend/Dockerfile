# ---------- Base image ----------
FROM python:3.12-slim

# ---------- Environment setup ----------
# Prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ENABLECORS=false \
    STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=true \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0

# ---------- Working directory ----------
WORKDIR /app

# ---------- Copy application code ----------
COPY . .

# ---------- Install dependencies ----------
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Streamlit configuration ----------
# Create Streamlit config directory and file
RUN mkdir -p /root/.streamlit && \
    echo "\
[server]\n\
headless = true\n\
port = 8501\n\
enableCORS = false\n\
enableXsrfProtection = true\n\
" > /root/.streamlit/config.toml

# ---------- Expose internal port ----------
# Note: the EC2 instance / Jenkins will map it to 127.0.0.1:8501 externally
EXPOSE 8501

# ---------- Command ----------
CMD ["streamlit", "run", "app.py"]
