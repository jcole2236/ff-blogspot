# ============== Import Statements ============== #
import os

# ============== Config Class ============== #
class Config:
    SECRET_KEY = os.environ.get('FFBLOGSPOT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FFBLOGSPOT_SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('FFBLOGSPOT_EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('FFBLOGSPOT_EMAIL_PASS')
