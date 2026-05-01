from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    print("השרת מתחיל לרוץ...")
    app.run(port=5000)