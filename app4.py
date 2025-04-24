from flask import Flask, redirect

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect("http://127.0.0.1:5004/secret")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
