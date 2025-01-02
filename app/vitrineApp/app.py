from flask import Flask, render_template
import socket
import os
import argparse

app = Flask(__name__)

# Get Odoo and PgAdmin URLs from environment variables or command-line arguments
ODOO_URL = os.environ.get('ODOO_URL', 'https://www.youtube.com/')  # Default to YouTube URL if not set
PGADMIN_URL = os.environ.get('PGADMIN_URL', 'https://www.youtube.com/')  # Default to YouTube URL if not set

@app.route("/")
def main():
    # Return the HTML template with dynamic variables
    return render_template('index.html', name=socket.gethostname(), odoo_url=ODOO_URL, pgadmin_url=PGADMIN_URL)

if __name__ == "__main__":
    print("This is a sample web application for intranet applications display.")

    # Check for Command Line Parameters to override environment variables
    parser = argparse.ArgumentParser()
    parser.add_argument('--odoo_url', required=False, help="Override Odoo URL")
    parser.add_argument('--pgadmin_url', required=False, help="Override pgAdmin URL")
    args = parser.parse_args()

    if args.odoo_url:
        print("Odoo URL from command line argument =", args.odoo_url)
        ODOO_URL = args.odoo_url  # Override environment variable with command-line argument
    elif not os.environ.get('ODOO_URL'):
        print("No command line argument or environment variable. Using default Odoo URL =", ODOO_URL)

    if args.pgadmin_url:
        print("PgAdmin URL from command line argument =", args.pgadmin_url)
        PGADMIN_URL = args.pgadmin_url  # Override environment variable with command-line argument
    elif not os.environ.get('PGADMIN_URL'):
        print("No command line argument or environment variable. Using default PgAdmin URL =", PGADMIN_URL)

    # Run the Flask app on host 0.0.0.0 and port 8085 (Docker container should map to this port)
    app.run(host="0.0.0.0", port=8085)
