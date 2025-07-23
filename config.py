import os

class Config:
    # Use DATABASE_URL from environment (Render will provide this)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:ShrK.postgres@localhost/dhaniya_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Use SECRET_KEY from environment for security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-in-production'
    
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size