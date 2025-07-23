#!/usr/bin/env python3
"""
WSGI entry point for Dhaniya Board Flask application
"""
import os
from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # This will only run if the script is executed directly
    # Not when imported by Gunicorn
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
