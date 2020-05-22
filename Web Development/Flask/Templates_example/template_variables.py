from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    some_variable = 'Nirmal'
    letters = list(some_variable)
    my_dictionary = {'puppy_name': 'Sammy'}
    return render_template('variables.html',my_variable=some_variable, letters=letters,
                           my_dictionary=my_dictionary)


if __name__ == "__main__":
    app.run(debug=True)