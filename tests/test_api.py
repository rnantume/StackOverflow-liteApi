import unittest
import json

from app import create_app

class QuestionsTestCase(unittest.TestCase):
    """class to represent questions test case"""

    def test_create_app(self):
        app = create_app(config_name="testing")


    def setUp(self):
        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        
    def test_api_can_get_all_questions(self):
        """Test API can get all questions (GET request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/questions',
                             data=json.dumps({"Topic":"Sample Topic", "Description":"Sample Description"}),
                             content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.get('/StackOverflow-lite/api/v1/questions')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Description', str(res.data))

    def test_add_question(self):
        """Test API can add new question"""
        res = self.client.post('/StackOverflow-lite/api/v1/questions', 
                    data=json.dumps({"Topic":"Sample Topic", "Description":"Sample Description"}),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Sample Description', str(res.data))
    
    def test_api_can_get_question_by_id(self):
        """Test API can get a question by using it's questionId."""
        res = self.client.post('/StackOverflow-lite/api/v1/questions', 
                    data=json.dumps({"Topic":"Sample Topic", "Description":"Sample Description"}),
                    content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result_in_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        result = self.client.get(
                '/StackOverflow-lite/api/v1/questions/{}'.format(result_in_json['questionId']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Sample Description', str(result.data))

if __name__=='__main__':
    unittest.main()
