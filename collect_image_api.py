from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import xml.etree.ElementTree as XML

app = Flask(__name__)


@app.route('/api/collect', methods=['POST'])
def collect():
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    res = XML.parse('Resources.xml')
    count = res.find('count')
    name = res.find('name')
    filename = count.text + name.text + ".jpg"
    res.find('count').text = str(int(count.text) + 1)
    res.find('name').text = 'image'
    res.write('Resources.xml')
    status = cv2.imwrite(filename, img)
    response = {'message': 'image received. size={}x{}, status:{}'.format(img.shape[1], img.shape[0], status, nparr)}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


app.run(host="0.0.0.0", port=5000)
