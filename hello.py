from flask import Flask
import socket

app = Flask(__name__)

hostname = socket.gethostname()

@app.after_request
def inject_hostname(response):
    # Inject the hostname into the headers
    response.headers['X-Server-Hostname'] = hostname
    return response

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
