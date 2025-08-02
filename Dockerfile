# Use official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy your script into the container
COPY "Battleship Game.py" .

# Run the script when the container starts
CMD ["python", "Battleship Game.py"]
