# Import external dependencies

You can create a virtual environment if necessary. Then run the following code to import
all neccessary external dependencies:

	pip install -r requirements.txt

Now, you are ready to work with the platform.

# Run the API

Run the following code:
	python code/mysimbdp-daas.py

You can interact with the API on a web browser via this link:
	http://127.0.0.1:5000/

To find a certain record:
```apps``` -> ```GET``` -> ```Try it out``` -> Input date DD-MM-YYYY and country name -> ```Execute```

# Ingest data with the API
Run the example following code:  

	python code/from_comsumer-producer_to_daas.py --server_address=http://127.0.0.1:5000/

 
# Ingest data directly to the database
Run the example following code:  

	python code/from_comsumer-producer_to_daas.py --n_concurrence=5 --record=True --n_shards=3	