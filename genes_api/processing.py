import pandas as pd


class GeneDataProcessor:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.gene_data = []

    # Read all data points into dataframe (all gets loaded into memory)
    # This function handles a few common 'missing data' cases
    def _load(self):

        df = pd.read_csv(self.csv_file)

        # Check if there are no records in the loaded df
        if df.empty:
            raise ValueError("The input CSV file doesn't contain any records.")

        # Check headers
        expected_columns = {'gene_id', 'gene_name', 'expression_value'}
        if not expected_columns.issubset(df.columns):
            raise ValueError(f"Invalid header in the input CSV file. Must contain: {expected_columns}")

        # Convert data types or drop rows containing values that can't be converted
        # won't handle gene_id here, it's not used in any downstream processing
        df['expression_value'] = pd.to_numeric(df['expression_value'], errors='coerce')
        df['expression_value'] = df['expression_value'].astype(float)

        # Drop rows with missing values
        df = df.dropna()
        # add warning

        # Strip whitespace from 'gene_name'
        df['gene_name'] = df['gene_name'].str.strip()

        # Drop rows containing any form of "unknown" gene name
        # this could be extended wildly, "unknown" is only exemplary
        df = df[~df['gene_name'].str.lower().eq('unknown')]

        return df

    # This is where average expressions are computed
    def process(self):
        df = self._load()
        grouped = df.groupby('gene_name')['expression_value'].mean().reset_index()
        grouped.rename(columns={'expression_value': 'average_expression'}, inplace=True)
        self.gene_data = grouped.to_dict(orient='records')

    # Returns a list of dicts
    # e.g. [{'gene_name': 'BRCA1', 'average_expression': 10.15}, ...]
    def get_all_genes(self):
        return self.gene_data

    # Returns a single dict for a given gene name
    # e.g. given 'BRCA1' as arg: {'gene_name': 'BRCA1', 'average_expression': 10.15}
    def get_single_gene(self, gene_name):
        for gene_record in self.gene_data:
            if gene_record['gene_name'] == gene_name:
                return gene_record
        return None
