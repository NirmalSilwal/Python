from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    my_list = list(range(1, 6))
    phones = ['Apple', 'Samsung', 'OPPO']
    user_logged_in = True

    return render_template("control_flows.html", my_list=my_list, phones=phones, user_logged_in=user_logged_in)


if __name__ == "__main__":
    app.run(debug=True)