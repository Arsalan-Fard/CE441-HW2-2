from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    try:
        # Make a request to the secret endpoint from the server
        response = requests.get('http://127.0.0.1:5004/secret')
        return response.text, response.status_code
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__'):
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
