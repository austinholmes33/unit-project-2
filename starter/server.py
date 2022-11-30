from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    words = ["blah", "hi", "another word"]
    return render_template("index.html", words=words)

if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "localhost")