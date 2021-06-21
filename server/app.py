from flask import Flask, request, jsonify
import os
import uuid
import io
from base64 import encodebytes
from PIL import Image

app = Flask(__name__)


def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r')  # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG')  # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode(
        'ascii')  # encode as base64
    return encoded_img


@app.route('/upload/', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join("files/", f_name))

        input_files = os.listdir('../images')[:5]
        encoded_imges = []
        for i in range(len(input_files)):
            encoded_imge = {}
            encoded_imge["key"] = i
            encoded_imge["image"] = input_files[i]
            encoded_imges.append(encoded_imge)

        result = jsonify({'result': encoded_imges})
        result.headers.add('Access-Control-Allow-Origin', '*')

        return result


app.run(debug=True, port=7070)
