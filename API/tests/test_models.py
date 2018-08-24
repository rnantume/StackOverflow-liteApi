import unittest
from models import Question, Answer


class ModelsTestCase(unittest.TestCase):
    """class to represent questions test case"""
    def setUp(self):
        """setting test variables"""
        self.question = Question('unittests ', 'what are unittests?')
        self.answer = Answer('unittests are tests for small system units', 1)
 
    def test_add_question(self):
        ''' Test adding question question '''
        res = self.question.add_question()
        self.assertEqual(dict, type(res))

    def test_get_all_questions(self):
        res = Question.get_questions()
        self.assertEqual(list, type(res))

    def test_post_and_get_all_questions(self):
        res = self.question.add_question()
        self.assertEqual(dict, type(res))
        self.assertEqual(list, type(Question.get_questions()))

    def test_get_one_question(self):
        res = self.question.add_question()
        self.assertEqual(dict, type(res))
        self.assertEqual(dict, type(Question.get_question(0)))

    def test_get_question_answers(self):
        res = self.question.add_question()
        self.assertEqual(dict, type(res))
        res = Answer.get_question_answers(0)
        self.assertEqual(list, type(res))

    def test_post_answers(self):
        res = self.question.add_question()
        self.assertEqual(dict, type(res))
        res = self.answer.add_answer(0)
        self.assertEqual(dict, type(res))


if __name__ == '__main__':
    unittest.main()