FROM python:3.11-slim
LABEL name = "Airlines project"
WORKDIR /app
RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade setuptools wheel jaraco.context \
    && pip install --no-cache-dir -r requirements.txt
# --no-cache-dir isn't what fixes the CVEs, but it's a good Docker practice because it avoids retaining pip's download cache inside the image.
# -r tells pip to read all packages listed inside requirements.txt

COPY . .
EXPOSE 5000
CMD ["python","app/app.py"]

