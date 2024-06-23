import unittest
import json
from app import create_app


class TestGeneAPI(unittest.TestCase):
    def setUp(self):
        app = create_app(csv_path='test_input.csv')
        self.client = app.test_client()
        self.client.testing = True

    def test_get_all_genes(self):
        response = self.client.get('/genes')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        expected_data = [
            {"gene_name": "BRCA1", "average_expression": 10.15},
            {"gene_name": "BRCA2", "average_expression": 12.7},
            {"gene_name": "TP53", "average_expression": 7.4}
        ]
        self.assertEqual(data, expected_data)

    def test_get_single_gene(self):
        response = self.client.get('/genes/BRCA1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        expected_data = {"gene_name": "BRCA1", "average_expression": 10.15}
        self.assertEqual(data, expected_data)

    def test_get_single_gene_not_found(self):
        response = self.client.get('/genes/Unknown')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode('utf-8'))
        expected_data = {"404": "Gene not found"}
        self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()
