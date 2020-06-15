from flask import Flask, render_template
app = Flask(__name__)


@app.route('/sula')
def hello_world():
    return render_template('index.html')


@app.route('/')
def sula():
    return render_template('page_1.html')


@app.route('/charts')
def charts():
    return render_template('charts.html')


@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/tables')
def tables():
    return render_template('tables.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/page')
def page():
    return render_template('page.html')


@app.route('/rewards')
def rewards():
    return render_template('rewards.html')


@app.route('/stretch')
def stretch():
    return render_template('stretch.html')


@app.route('/camera')
def camera():
    return render_template('camera.html')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)