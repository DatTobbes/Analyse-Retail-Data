import requests
import json
import shutil
import os
import cv2


class Client:



    def send_to_server(self):
        """
        Sends the Document Image to PretrainedClassifier
        :param img:
        :return:
        """
        url = "http://127.0.0.1:5000/devicedata"


        data = {"data": 'Apple iPhone 7 Plus (32GB)'}
        data_json = json.dumps(data)
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=data_json, headers=headers)
        return response

if __name__ == "__main__":
    c = Client()
    print(c.send_to_server())