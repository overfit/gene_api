# Genes API

The repo contains the code for a mock REST API serving gene information.

### Instructions to run

Once you have `genestack` directory on your local machine, run the following:

```
cd genestack
pip install requirements.txt
```

To run the app:

```
cd gene_api
flask run
```
This will print out the address on which the app is running, for example:

```
* Running on http://127.0.0.1:5000

```

From there, the gene endpoints can be accessed through browser under `http://127.0.0.1:5000/genes` and `http://127.0.0.1:5000/genes/<gene_name>`

### Unit tests

To execute unit tests for processing and app methods, run:

```
python -m unittest test_processing.py
```
or

```
python -m unittest test_app.py
```

 

