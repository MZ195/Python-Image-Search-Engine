# import the necessary packages
from color_descriptor import ColorDescriptor
from searcher import Searcher
import cv2

from flask import Flask, request, jsonify
import os
import uuid

app = Flask(__name__)


@app.route('/upload/', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join("files/", f_name))

        encoded_imges = []
        cd = ColorDescriptor((8, 12, 3))
        # load the query image and describe it
        query = cv2.imread(f"files/{f_name}")
        features = cd.describe(query)
        # perform the search
        searcher = Searcher("index.csv")
        results = searcher.search(features)
        for i in range(len(results)):
            encoded_imge = {}
            encoded_imge["key"] = i
            encoded_imge["image"] = results[i][1]
            encoded_imges.append(encoded_imge)

        result = jsonify({'result': encoded_imges})
        result.headers.add('Access-Control-Allow-Origin', '*')

        os.remove(f"files/{f_name}")

        return result


if __name__ == '__main__':
    app.run(debug=True, port=7070)
