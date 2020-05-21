from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>go to puppy/name and see the result</h1>"


@app.route('/puppy/<name>')
def translation(name):
    return f"<h1>Puppy name is: {name[:-1]+'iful'}</h1>" if name[-1] == 'y' else f"<h1>Puppy name is: {name+'y'}</h1>"


if __name__ == "__main__":
    app.run(debug=True)