from flask import Flask

app = Flask(__name__)


@app.route('/')  # 127.0.0.1:5000
def index():
    return "<h1>Hello Puppy</h1>"


@app.route('/information') # 127.0.0.1:5000/information
def info():
    return "<h1>Puppies are cute</h1>"


@app.route('/puppy/<name>')
def puppy(name):
    # return f'<h1>This is a page for {name}</h1>'
    return f'<h1>upper case: {name.upper()}</h1>'


if __name__ == "__main__":
    app.run()