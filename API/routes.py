
"""contains various routes for the questions endpoints"""

from flask import request, jsonify, Blueprint, abort
from flask_restful import (reqparse, Resource, fields, inputs, Api,
                            marshal)

import models


question_fields = {
    'Url': fields.Url(absolute=True, scheme='http'),
    'questionId': fields.String,
    'Topic': fields.String,
    'Description': fields.String,
    'datetimeCreated': fields.DateTime,
    'answers': fields.List(cls_or_instance=fields.Raw) 
}

class QuestionList(Resource):
    """
    Shows a list of all questions, and lets one POST to add new question
    """
    
    def get(self):
        """
        get all questions
        """
        questions = models.Question.get_questions()
        if questions:
            """serializing the response with JSON"""
            return {'Questions': [marshal(question,question_fields)
                                for question in questions]},200
        else:
            return {'Message': 'No Questions Found'},200

    
questions_bp = Blueprint('routes', __name__)
qn_api = Api(questions_bp)

qn_api.add_resource(QuestionList,
    '/questions',
    endpoint='questions'

