from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/perfume")
def about():
    return render_template("perfume.html")


@app.route("/address")
def contacts():
    return render_template("address.html")


if __name__ == "__main__":
    app.run(debug=True)