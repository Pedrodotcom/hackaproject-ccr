from flask import Flask, render_template
app = Flask(__name__)


@app.route('/sula')
def hello_world():
    return render_template('index.html')


@app.route('/')
def sula():
    return render_template('page_1.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/page')
def page():
    return render_template('page.html')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)