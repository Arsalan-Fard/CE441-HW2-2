# app4.py
from flask import Flask, Response

app = Flask(__name__)

# همه‌ی مسیرها را هندل کن
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_inside(path):
    # ریدایرکت موقت به سرویس محرمانه‌‌
    return Response(
        status=302,
        headers={'Location': 'http://127.0.0.1:5004/secret'}
    )

if __name__ == '__main__':
    # app2 تنها روی پورت پیش‌فرض HTTP (۸۰) تماس می‌گیرد
    app.run(host='0.0.0.0', port=80)
