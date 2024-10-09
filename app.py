from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

def denoise_image(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21) #
    _, buffer = cv2.imencode('.jpg', dst)
    return base64.b64encode(buffer).decode('utf-8')

@app.route('/denoise', methods=['POST'])
def denoise():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['image']
    image_bytes = file.read()
    denoised_image = denoise_image(image_bytes)
    return jsonify({'denoised_image': denoised_image})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)