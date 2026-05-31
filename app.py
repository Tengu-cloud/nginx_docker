from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():

    return {
        "x_forwarded_for":
            request.headers.get("X-Forwarded-For"),
    }

app.run(host="0.0.0.0", port=5000)