# Instructions
In this exercise you will experiment with different ways of deploying the exported model for
online and offline inference.

# Preliminary step
First we need to fetch the production model. We are going to save it into the ``model``
directory:

```bash
wandb artifact get genre_classification_prod/model_export:prod --root model
```

# Offline (batch) inference
Let's run inference on the test set. 

## Steps
1. Use the W&B CLI to download the ``genre_classification_prod/data_test.csv:latest`` artifact
   locally (``wandb artifact get``...)
   
2. Use ``mlflow models predict ...`` to perform batch inference on it
   > Remember to use ``-m model`` to specify the directory where you stored the artifact
   
# Online inference
Here we use the model for online prediction exposing the model as a REST API.

1. Let's start the API using ``mlflow models serve ...`` 
   > HINT: remember that we saved the model into the ``model`` directory
   The API is now ready to perform inference.

2. Open Jupyter in another terminal, and in a notebook use the ``requests`` library
   to interrogate the API and do inference on the provided ``data_sample.json``:
   ```python
   import requests
   import json
   
   with open("data_sample.json") as fp:
       data = json.load(fp)
   
   results = requests.post("http://localhost:5000/invocations", json=data)
   
   print(results.json())
   ```
   
## Bonus: docker deployment
You can also use docker to build an image and then deploy to a Cloud provider 
(AWS, GCP, Azure...). Expose port 5000 of that machine to the world, and you will be able to
use your model from whenever as a simple API call.

1. Create the docker image:
   ```bash
   mlflow models build-docker -m model -n "genre_classification"
   ```
   This will take a few minutes (of course, you need docker installed)

2. Follow the procedure for your Cloud provider of choice to deploy a Docker image

3. Open port 5000 on the machine hosting the image

4. Use requests to interrogate that machine, by using the snippet we used earlier and substituting
   ``http://localhost:5000/invocations`` with ``[url to the deployed machine]:5000/invocations``