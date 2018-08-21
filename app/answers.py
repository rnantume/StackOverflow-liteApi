"""contains various routes for the answers endpoints"""

from flask import request, jsonify, Blueprint, abort
from flask_restful import (reqparse, Resource, inputs, fields,
                            Api, marshal)

from .models import Answer

answer_fields = {
    'answerId': fields.String,
    'answer': fields.String,
    'accepted': fields.Boolean,
    'datetimeCreated': fields.DateTime,
    'comments': fields.List(cls_or_instance=fields.Raw)
}

class AnswerList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('answer', type=str, required=True, 
                            nullable=False, help="answer cannot be null or none",
                            location = ['form', 'json']
                            )   
        self.reqparse.add_argument('accepted', choices=('True','False'),
                            default=False, store_missing=True, location = ['form', 'json']
                            )
        super().__init__()
    
    def post(self, questionId):
        """
        adding an answer to a specific question using questionId
        """
        try:
            answers = Answer.get_question_answers(questionId)
        except TypeError:
            abort(404, "message = question {} doesnot exist".format(questionId))
        else:
            args = self.reqparse.parse_args()
            new_answer = Answer(**args).add_answer(questionId)
            """
            serializing the response with JSON
            """
            return {'Your answer': [marshal(new_answer, answer_fields)]},201

answers_bp = Blueprint('answers', __name__)
ans_api = Api(answers_bp)

ans_api.add_resource(AnswerList,
    '/questions/<string:questionId>/answers',
    endpoint='answers')

