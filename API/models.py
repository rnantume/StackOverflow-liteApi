import uuid
import datetime

questions = []

class Question():
    """ 
    class to represent question model
    """
    def __init__(self, Topic, Description):
        self.questionId = len(questions)
        self.Topic = Topic
        self.Description = Description
        self.datetimeCreated = datetime.datetime.now()
        self.answers = []


    @staticmethod
    def get_questions():
        """
        :return: all questions in memory
        """
        if questions:
            return questions 

    def add_question(self):
        """
        method to add a new question
        :return: question created(dict)
        """
        new_question = {
            'questionId': self.questionId,
            'Topic': self.Topic,
            'Description': self.Description,
            'datetimeCreated': self.datetimeCreated,
            'answers': self.answers
        }
        questions.append(new_question)
        return new_question

    @staticmethod
    def get_question(questionId):
        """
        method to get a specific question by questionId
        :param questionId: Question id
        :return: question (dict) or none
        """
        for question in questions:
            if question['questionId']== questionId:
                return question


class Answer():
    """
    class to represent answer model
    """

    @staticmethod
    def get_question_answers(questionId):
        """
        method to get all answers about a question
        :param questionId: for question whose answers to return
        :return: answers(list) or question is none
        """
        for question in questions:
            if question['questionId']== questionId:
                return question['answers']
    