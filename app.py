from flask import Flask
import jsonify

app = Flask(__name__)

@app.route('/health-check')
def health_check():
    return jsonify("OK"), 200


