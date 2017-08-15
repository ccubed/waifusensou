from flask import *
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/9'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/10'

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/<id>", methods=['GET'])
def contest(id):
    return "Contest"

@app.route("/create", methods=['GET'])
def create():
    return "Create a War"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="12555")