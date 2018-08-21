import unittest
import json

from app import create_app
# from instance.config import app_config

class QuestionsTestCase(unittest.TestCase):
    """class to represent questions test case"""

    def test_create_app(self):
        app = create_app(config_name="testing")


    def setUp(self):
        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        
        """setup test variables"""
#         self.question = {'Topic':'Sample Topic', 'Description':"Sample Description"}
#         self.answer = {'answer':"Sample Answer", 'accepted':True}
#         self.partial_qn = {'Topic':'Sample Topic'}

    def test_hello(self):
        """Test API can get hello function"""
        res = self.client.get('/hello')
        self.assertEqual(res.status_code, 200)

    def test_api_can_get_all_questions(self):
        """Test API can get all questions (GET request)."""
        res = self.client.get('StackOverflow-lite/api/v1/questions')
        self.assertEqual(res.status_code, 200)

if __name__=='__main__':
    unittest.main()
