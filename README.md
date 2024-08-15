# flask-hello-world
basic hello world Flask app

## Running
Pull down the image with something like:

`docker pull ghcr.io/cliffeh/flask-hello-world:v1`

(See: https://github.com/cliffeh/flask-hello-world/pkgs/container/flask-hello-world).

Then run it with:

`docker run -dp 5000:5000 --rm ghcr.io/cliffeh/flask-hello-world:v1`
