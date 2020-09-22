from flask import Flask, jsonify
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
auth = HTTPDigestAuth()

@auth.get_password
def get_pw(username):
    if username == 'vcu':
        return "rams"
    return None

@app.route("/", methods=['GET'])
@auth.login_required
def get():
        return jsonify()

if __name__ == "__main__": 
    app.run()
