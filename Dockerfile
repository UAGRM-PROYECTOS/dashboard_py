# Use an official Python runtime as a parent image
FROM python:3.9

# Install CMake
RUN apt-get update && \
    apt-get install -y cmake && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Expose port 8000 (adjust as needed)
EXPOSE 8000

# Run the application with Gunicorn
# CMD ["gunicorn", "-b", "0.0.0.0:9000", "dashboard.wsgi:application"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
