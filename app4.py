from flask import Flask, redirect, request
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Log everything (DEBUG and above)
    format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
    handlers=[
        logging.StreamHandler()  # Output to console (Docker logs)
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    logger.info("made it")
    # Redirect to the secret endpoint on localhost
    return redirect("http://127.0.0.1:5004/secret")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
