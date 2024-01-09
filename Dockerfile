# Use a base image suitable for your application (e.g., Python, Node.js, etc.)
FROM python:3.9.1

# Set the working directory in the container
WORKDIR /marketapp

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
