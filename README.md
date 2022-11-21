# similar-faqs

Check out the live demo here

https://huggingface.co/spaces/Shamima/similar-faqs

## Usage
Install dependencies `pip install -r requirements.txt`

To run the server locally, run `uvicorn main:app --reload`.

## To build and test a Docker image, run:

* `docker build -t dlapi .` to build the container.
  * If you're not running on 64-bit linux, instead run `docker buildx build --platform linux/amd64 -t dlapi .`.  This will build the image using the correct architecture for Azure.
* `docker run -d --name dlapi -p 80:80 dlapi` to run the container.
* `docker ps` to view the container information.
* Run `docker logs` to see logs from the container.  You should see `Uvicorn running on http://0.0.0.0:80`.  If you don't see this, wait a bit and try running `docker logs` again.
* Visit `127.0.0.1` or `localhost` to see the API server.  Visit `localhost/docs` to see API docs.
* Run `docker stop dlapi` to stop the container.
