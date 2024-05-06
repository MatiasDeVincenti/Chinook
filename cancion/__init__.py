from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init.app(app)

@app.route('/')
def hello():
    return 'Hello, World!'