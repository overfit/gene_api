import unittest
import pandas as pd
from processing import GeneDataProcessor


class TestGeneDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = GeneDataProcessor('test_input.csv')

    def test_load_returns_dataframe(self):
        df = self.processor._load()
        self.assertIsInstance(df, pd.DataFrame)

    def test_load_dataframe_has_expected_columns(self):
        df = self.processor._load()
        expected_columns = ['gene_id', 'gene_name', 'expression_value']
        self.assertListEqual(list(df.columns), expected_columns)

    def test_load_dataframe_has_no_missing_values(self):
        df = self.processor._load()
        self.assertFalse(df.isnull().values.any())

    def test_load_dataframe_has_expected_records(self):
        df = self.processor._load()
        self.assertEqual(len(df), 5)

    def test_process_returns_expected_results(self):
        expected_results = [
            {'gene_name': 'BRCA1', 'average_expression': 10.15},
            {'gene_name': 'BRCA2', 'average_expression': 12.7},
            {'gene_name': 'TP53', 'average_expression': 7.4}
        ]
        self.processor.process()
        gene_data = self.processor.gene_data
        self.assertEqual(gene_data, expected_results)

    # this one is almost equivalent to the previous
    # the result here is obtained by calling get_all_genes()
    def test_get_all_genes_expected_result(self):
        expected_results = [
            {'gene_name': 'BRCA1', 'average_expression': 10.15},
            {'gene_name': 'BRCA2', 'average_expression': 12.7},
            {'gene_name': 'TP53', 'average_expression': 7.4}
        ]
        self.processor.process()
        gene_data = self.processor.get_all_genes()
        self.assertEqual(gene_data, expected_results)

    def test_get_single_gene_expected_result(self):
        expected_results = {'gene_name': 'BRCA1', 'average_expression': 10.15}
        self.processor.process()
        gene_data = self.processor.get_single_gene('BRCA1')
        self.assertEqual(gene_data, expected_results)


if __name__ == '__main__':
    unittest.main()
