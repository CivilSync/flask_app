from flask import Flask

app = Flask(__name__)

VERSION = "2.0"

@app.route("/")
def hello():
    return f"Hello, World! (version {VERSION})"

if __name__ == "__main__":
    app.run(debug=True)
