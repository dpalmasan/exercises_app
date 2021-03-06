# src/app.py

from flask import Flask
from flask import render_template
from .config import app_config
from .models import db
from .models import bcrypt

from .views.UserView import user_api as user_blueprint
from .views.RoutineView import routine_api as routine_blueprint
from .views.ExerciseView import exercise_api as exercise_blueprint
from .views.ValidateView import validate_api as validate_blueprint

from flask_cors import CORS


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    # Allow CORS. Should modify this for origin in production
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Initializing bcrypt
    bcrypt.init_app(app)

    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(routine_blueprint, url_prefix='/api/v1/routines')
    app.register_blueprint(exercise_blueprint, url_prefix='/api/v1/exercises')
    app.register_blueprint(validate_blueprint, url_prefix='/api/v1/validate')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return render_template('index.html')

    return app
