FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install numpy
RUN pip install numpy

# Copy your game file into the container
COPY battleship_game.py .

# Run the game when the container starts
CMD ["python", "battleship_game.py"]