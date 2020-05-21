from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f"<h1>hello puppy</h1>"


@app.route('/puppy/<name>')   # http://127.0.0.1:5000/puppy/kukur
def information(name):
    return f"<h2>String at 100th index is {name[100]}</h2>"


if __name__ == "__main__":
    app.run(debug=True)
