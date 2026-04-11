# Base layer
FROM python:3.9.6-slim
#Working Dir
WORKDIR /app
#Installing the requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt