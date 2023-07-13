import requests
from PIL import Image
import io

# Definir la URL del servicio Flask
url = 'http://7c97-34-85-149-35.ngrok-free.app/ocr'

# Cargar la imagen desde un archivo
image_path = 'prueba.jpg'  # Reemplaza con la ruta correcta de tu imagen
image_file = open(image_path, 'rb')

# Crear los datos para enviar en la solicitud
files = {'image': image_file}

# Realizar la solicitud POST
response = requests.post(url, files=files)

# Verificar la respuesta
if response.status_code == 200:
    # Imprimir el texto extraído
    data = response.json()
    print('Texto extraído:', data['text'])
else:
    print('Error en la solicitud:', response.text)