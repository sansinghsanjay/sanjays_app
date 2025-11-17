# ---------- Base image ----------
FROM nginx:alpine

# ---------- Working directory ----------
WORKDIR /usr/share/nginx/html

# ---------- Copy frontend files ----------
# Copy your index.html, CSS, JS, assets, etc.
COPY . /usr/share/nginx/html

# ---------- Expose port ----------
EXPOSE 80

# ---------- Command ----------
# Nginx runs automatically as the container's entrypoint