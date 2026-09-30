FROM python:3.11-slim
LABEL name = "Airlines project"
WORKDIR /app
COPY requirements.txt .
# -r tells pip to read all packages listed inside requirements.txt
RUN pip install -r requirements.txt  
COPY . .
EXPOSE 5000
CMD ["python","app.py"]

