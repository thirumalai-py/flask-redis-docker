# Stage 1: Build
FROM python:3.12-slim AS build
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py /app

# Stage 2: Run the application
FROM python:3.12-slim
WORKDIR /app
COPY --from=build /app /app
EXPOSE 5000
CMD ["python", "app.py"]
