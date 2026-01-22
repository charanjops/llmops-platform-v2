# syntax=docker/dockerfile:1
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python -m compileall .

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
RUN addgroup --gid 1001 appgroup && adduser --uid 1001 --gid 1001 --disabled-password --gecos "" appuser
USER 1001
ENV PYTHONUNBUFFERED=1
CMD ["python", "app/main.py"]