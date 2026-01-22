FROM python:3.12-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python -m compileall .

FROM python:3.12-slim as runtime
WORKDIR /app
COPY --from=builder /app /app
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser
ENV PYTHONUNBUFFERED=1
CMD ["python", "app/main.py"]