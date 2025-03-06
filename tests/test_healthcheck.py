import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class HealthCheckTest(unittest.TestCase):
    def test_healthy_endpoint(self):
        response = client.get("/healthy")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})
