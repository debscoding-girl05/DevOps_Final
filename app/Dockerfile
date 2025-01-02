# Use the official Python image from Docker Hub
FROM python:3.6-alpine

# Set the working directory in the container
WORKDIR /opt

# Create the requirements.txt file directly in the image
RUN echo "Flask==1.1.4" > requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . /opt/

# Expose the port Flask runs on
EXPOSE 8085

# Set environment variables (can be overwritten by Docker Compose)
ENV ODOO_URL=http://localhost:8069
ENV PGADMIN_URL=http://localhost:8082

# Run the Flask application
ENTRYPOINT ["python", "/opt/vitrine-app/app.py"]
