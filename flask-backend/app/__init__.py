from flask import Flask
import os
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .config import Config
from .models import db
from flask_migrate import Migrate
from .seeds import seed_commands


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app,db)
app.cli.add_command(seed_commands)

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
