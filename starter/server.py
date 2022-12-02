from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html", cupcakes = get_cupcakes("cupcakes.csv"))

# @app.route("/cupcake_individual")
# def individual_cupcake():
    # return render_template("individual_cupcake.html", cupcakes = find_cupcake("cupcakes.csv", ))

@app.route("/order")
def order():
    return render_template("order.html", cupcakes = get_cupcakes("order.csv"))

@app.route("/add_cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("order.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry, cupcake not found."

if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "localhost")