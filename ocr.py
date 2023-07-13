from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import pytesseract
from PIL import Image
app = Flask(__name__)
@app.route('/ocr', methods=['POST'])
def ocr():
    # Verificar que se haya enviado un archivo
    if 'image' not in request.files:
        return jsonify({'error': 'No se envió ninguna imagen'})

    # Obtener el archivo enviado
    image_file = request.files['image']

    # Leer la imagen y realizar OCR
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)

    # Devolver el texto extraído
    return jsonify({'text': text})
if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()