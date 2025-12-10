import unittest
from perspective_core import app

class TestCore(unittest.TestCase):
    def test_verticals(self):
        with app.test_client() as client:
            response = client.get('/api/verticals')
            self.assertEqual(response.status_code, 200)