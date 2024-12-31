# Use python 3.6-alpine as the base image
FROM python:3.6-alpine

# Set the working directory inside the container
WORKDIR /opt

# Install the Flask module
RUN pip install Flask

# Copy the vitrine-app repository into the container (if you need it)
COPY vitrine-app /opt/vitrine-app

# Set environment variables for Odoo and pgAdmin URLs
ENV ODOO_URL=http://odoo_url
ENV PGADMIN_URL=http://pgadmin_url

# Expose port 8080 for the Flask app
EXPOSE 8080

# Set the entrypoint to run the app.py (you can adjust the path if necessary)
ENTRYPOINT ["python", "/opt/vitrine-app/app.py"]

