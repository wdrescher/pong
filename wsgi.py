from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get():
        return jsonify()

if __name__ == "__main__": 
    app.run()
