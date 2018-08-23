from flask import Flask, Blueprint

import models
from resources.questions import questions_bp
from resources.answers import answers_bp

# from instance.config import app_config

app = Flask(__name__)
# app.config.from_object(app_config[config_name])
# app.config.from_pyfile('config.py')

    """
    registering the questions_bp and answers_bp blueprints
    """
    app.register_blueprint(questions_bp, url_prefix='/StackOverflow-lite/api/v1')
    app.register_blueprint(answers_bp, url_prefix='/StackOverflow-lite/api/v1')
