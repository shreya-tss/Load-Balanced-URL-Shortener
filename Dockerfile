# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app and install dependencies
COPY app.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose port used by Flask
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

