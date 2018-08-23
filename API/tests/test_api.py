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
  
    def tearDown(self):
        """teardown initialised variables"""
        self.question = {}
        self.answer = {}
        self.partial_qn = {}

if __name__ =='__main__':
    unittest.main()
