
"""contains various routes for the questions endpoints"""

from flask import request, jsonify, Blueprint, abort
from flask_restful import (reqparse, Resource, fields, Api,
                            marshal)

from .models import Question


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
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Topic', type=str, required=True, 
                            nullable=False, help="Topic cannot be null or none",
                            location = ['form', 'json']
                            )
        self.reqparse.add_argument('Description', type=str, required=True, 
                            nullable=False, help="Description cannot be null or none",
                            location = ['form', 'json']
                            )
        super().__init__()

    def get(self):
        """
        get all questions
        """
        questions = Question.get_questions()
        if questions:
            """serializing the response with JSON"""
            return {'Questions': [marshal(question,question_fields)
                                for question in questions]},200
        else:
            return {'Message': 'No Questions Found'},200

    def post(self):
        """
        create a new question
        """
        args = self.reqparse.parse_args()
        new_question = Question(**args).add_question()
        """serializing the response with JSON"""
        return {'Your Question':[marshal(new_question, question_fields)]},201


class Question(Resource):
    def get(self, questionId):
        """
        get a specific question
        """
        question = Question.get_question(questionId)
        if question:
            return {'Your question': [marshal(question,question_fields)]}, 200
        else:
            abort(404, "question {} doesnot exist".format(questionId))

questions_bp = Blueprint('questions', __name__)
qn_api = Api(questions_bp)

qn_api.add_resource(QuestionList,
    '/questions',
    endpoint='questions')

qn_api.add_resource(Question,
    '/questions/<string:questionId>',
    endpoint='questions')