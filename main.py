from flask import Flask, render_template, request
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/generate_qr", methods=['GET'])
def print_url():
    url = request.args.get("url")
    
    # Generar QR
    qr = qrcode.make(url)
    
    # Convertir a base64
    buffered = BytesIO() # BytesIO reserva un espacio de memoria RAM y lo usa como almacenamiento
    qr.save(buffered)
    qr_base64 = base64.b64encode(buffered.getvalue()).decode()
    
    return render_template('url.html', url=url, qr_base64=qr_base64)

if __name__ == '__main__':
    app.run(debug=True)