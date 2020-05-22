from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form_index.html')


@app.route('/signup')
def signup_form():
    return render_template('signup.html')


@app.route('/thankyou')
def thank_you():
    Firstname = request.args.get('first')
    Lastname = request.args.get('last')
    return render_template('thankyou.html', first=Firstname, last=Lastname)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)