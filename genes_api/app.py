from flask import Flask, jsonify, render_template_string
from processing import GeneDataProcessor


def create_app(csv_path='example_input.csv'):
    app = Flask(__name__)

    # Initialize GeneDataProcessor and load the data
    processor = GeneDataProcessor(csv_path)
    processor.process()

    # Define /genes endpoint function
    @app.route('/genes', methods=['GET'])
    def get_all_genes():
        genes = processor.get_all_genes()
        return jsonify(genes)

    # Define /genes/<gene_name> endpoint function
    @app.route('/genes/<gene_name>', methods=['GET'])
    def get_single_gene(gene_name):
        gene_record = processor.get_single_gene(gene_name)
        if gene_record is not None:
            return jsonify(gene_record)
        else:
            return jsonify({'404': 'Gene not found'}), 404

    # Define the root endpoint function
    # just a simple welcome message
    @app.route('/')
    def welcome():
        welcome_message = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Genes API</title>
        </head>
        <body>
            <h1>This is Genes API Home Page</h1>
            <p>Check out all genes under HOME/genes and specific genes under HOME/genes/&lt;gene_name&gt;</p>
        </body>
        </html>
        """
        return render_template_string(welcome_message)

    return app


if __name__ == '__main__':
    gene_app = create_app()
    gene_app.run(debug=True)
