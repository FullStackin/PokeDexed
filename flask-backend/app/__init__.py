from flask import Flask
import os
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

@app.route("/")
def index():
    return "hello world"
