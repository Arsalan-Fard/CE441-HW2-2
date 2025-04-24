
from flask import Flask, redirect, Response
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

# Use a unique path to avoid accidental triggers
REDIRECT_PATH = '/redirect_to_secret_ce441' 

@app.route(REDIRECT_PATH, methods=['GET'])
def redirect_handler():
    target_url = "http://127.0.0.1:5004/secret"
    logger.info("made it")
    print(f"Received request, redirecting to: {target_url}") 
    # Send a 302 Found redirect
    # Using Response to be explicit, but redirect() works too.
    response = Response(status=302)
    response.headers['Location'] = target_url
    return response
    # Or simply:
    # return redirect(target_url, code=302)

if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) and standard HTTP port 80
    print(f"Starting redirect server on port 80, listening for {REDIRECT_PATH}")
    app.run(host='0.0.0.0', port=80)
