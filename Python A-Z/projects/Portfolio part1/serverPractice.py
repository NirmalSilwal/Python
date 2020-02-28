from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('./index.html',name=username, post_id=post_id)

@app.route('/blog')
def my_blog():
    return 'I will start to write blog soon! '

@app.route('/blog/2020/dogs')
def my_blog2():
    return 'latest dog blog '