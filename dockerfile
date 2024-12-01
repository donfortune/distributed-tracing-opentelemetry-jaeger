FROM python:3.9-slim #optimized image

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Run the application
CMD ["python", "app.py"]
