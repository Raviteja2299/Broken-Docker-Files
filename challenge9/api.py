from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Docker"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=os.getenv("PORT"))
