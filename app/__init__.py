from flask import Flask

from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    

    """
    registering the questions_bp and answers_bp blueprints
    """
    from .questions import questions_bp
    app.register_blueprint(questions_bp, url_prefix='/StackOverflow-lite/api/v1')

    from .answers import answers_bp
    app.register_blueprint(answers_bp, url_prefix='/StackOverflow-lite/api/v1')


    return app
