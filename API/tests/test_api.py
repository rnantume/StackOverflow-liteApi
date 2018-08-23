import unittest
import json

from app import app
# from instance.config import app_config

class QuestionsTestCase(unittest.TestCase):
    """class to represent questions test case"""

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        
        """setup test variables"""
        self.question = {'Topic':'Sample Topic', 'Description':"Sample Description"}
        self.answer = {'answer':"Sample Answer"}
        self.partial_qn = {'Topic':'Sample Topic'}

    def test_api_gets_all_questions(self):
        """Test API can get all questions (GET request)."""
        res = self.client.get('/StackOverflow-lite/api/v1/questions')
        self.assertEqual(res.status_code, 200)

    def test_add_question(self):
        """Test API can add new question"""
        res = self.client.post('/StackOverflow-lite/api/v1/questions',
                         data=json.dumps(self.question),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Sample Description', str(res.data))

    def test_api_can_post_and_get_all_questions(self):
        """Test API can get all questions (GET request and POST request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/questions', 
                    data=json.dumps(self.question),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.get('/StackOverflow-lite/api/v1/questions')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Description', str(res.data))

    def test_api_can_get_question_by_id(self):
        """Test API can get a question by using it's questionId."""
        res = self.client.post('/StackOverflow-lite/api/v1/questions',
                         data=json.dumps(self.question),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result = self.client.get(
                '/StackOverflow-lite/api/v1/questions/{}'.format(0))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Sample Description', str(res.data))

    def test_api_can_get_answers_to_question_by_id(self):
        """Test API can get answers to a question by using it's questionId."""
        res = self.client.post('/StackOverflow-lite/api/v1/questions',
                         data=json.dumps(self.question),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result = self.client.get(
                '/StackOverflow-lite/api/v1/questions/{}/answers'.format(0))
        self.assertEqual(result.status_code, 200)

    def test_api_cannot_post_question_if_Description_missing(self):
        res = self.client.post('/StackOverflow-lite/api/v1/questions',
                         data=json.dumps(self.partial_qn),content_type='application/json')
        self.assertEqual(res.status_code, 400)
  
    def tearDown(self):
        """teardown initialised variables"""
        self.question = {}
        self.answer = {}
        self.partial_qn = {}

if __name__ =='__main__':
    unittest.main()
