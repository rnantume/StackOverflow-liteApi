from flask import Flask, Blueprint


app = Flask(__name__,instance_relative_config=True)

app.config['DEBUG'] = True

from .routes import questions_bp
"""
registering the questions_bp and answers_bp blueprints
"""
app.register_blueprint(questions_bp)


