# app4.py
from flask import Flask, Response

app = Flask(__name__)

# همه‌ی مسیرها را هندل کن
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_inside(path):
    print(f"[+] Listening on port {port}")

    # ریدایرکت موقت به سرویس محرمانه‌‌
    return Response(
        status=302,
        headers={'Location': 'http://127.0.0.1:5004/secret'}
    )

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))  # Fallback to 10000 if PORT is not set
    app.run(host="0.0.0.0", port=port)


