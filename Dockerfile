FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl wget gnupg \
    libnss3 libatk-bridge2.0-0 libgtk-3-0 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 libgbm1 \
    libasound2 libpangocairo-1.0-0 libpango-1.0-0 \
    libxshmfence1 libxfixes3 libdrm2 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN pip install playwright

RUN playwright install chromium

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]