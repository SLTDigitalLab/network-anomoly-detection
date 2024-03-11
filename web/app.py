from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/4g')
def index():
    return render_template('4g.html')

@app.route('/ont')
def index():
    return render_template('ont.html')

@app.route('/hello')
def hello():
    return 'Hello, World!'