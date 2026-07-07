import unittest
from app import finggu_app
from app.models import FingguApiPerformance
from app.services.performance_service import finggu_get_performance_metrics

class TestPerformanceService(unittest.TestCase):
    def setUp(self):
        self.app = finggu_app.test_client()
        self.app.testing = True

    def test_get_performance_metrics(self):
        response = self.app.get('/api/performance')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
