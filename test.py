from flask import Flask
from flask import render_template
from flask import jsonify
from lib.parsers import ParserFactory

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def hello():
    return render_template('index.html')

@app.route('/fetch/<sp>/<id>')
def fetch(sp, id):
    p = ParserFactory.createParser(sp)
    result = p.fetch(id)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
