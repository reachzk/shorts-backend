# Use a base Python image
FROM python:3.10-slim

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose Render's required port
ENV PORT=10000

# Run the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
