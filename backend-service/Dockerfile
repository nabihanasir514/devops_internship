# ---------- Stage 1: Builder ----------
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .

# Create a non-root user
RUN useradd -m appuser

# Switch to non-root user
USER appuser

EXPOSE 5002

CMD ["python", "app.py"]
