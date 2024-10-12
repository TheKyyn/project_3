import unittest
import json
from app import app

class BigDataAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_data(self):
        response = self.app.get('/data?category=example')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_add_data(self):
        response = self.app.post('/data', 
                                 data=json.dumps({"data_value": "UnitTest Value", "category": "UnitTest Category"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'Data added successfully')

if __name__ == '__main__':
    unittest.main()
