# This is an official Python image from Docker Hub
FROM python:3.12-slim

# Set the route for the working directory inside the container
WORKDIR /app

# Copy all the files in my current directory to the container /app directory
COPY . /app

# Use pip to install the dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Make port 5000 available
EXPOSE 5000

# Use python to run the app.py file when the container launches
CMD ["python", "app.py"]