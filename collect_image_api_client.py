import requests
import cv2
import glob, os
from tkinter import *
from tkinter.filedialog import askdirectory

addr: str = 'http://localhost:5000'
url = addr + '/api/collect'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

root = Tk().withdraw()
# filename = askopenfilename(initialdir="/", title="Select file",
#                            filetypes=[("jpeg files", "*.jpg")])

directory = askdirectory()
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        filename = os.path.join(directory, filename)
        img = cv2.imread(filename)
        _, img_encoded = cv2.imencode('.jpg', img)
        # status = cv2.imwrite('/images/img.jpg', img)
        response = requests.post(url, data=img_encoded.tostring(), headers=headers)
        print(response.text)


