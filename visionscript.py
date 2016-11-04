from base64 import b64encode
from os import makedirs
from os.path import join, basename
from sys import argv

import requests
import json

image_filename= 'page-004.pdf.header.jpg'
api_key= 'AIzaSyD6kpyzItHfRlJNEmRTFRF5HDdCNXMYPhQ'

def make_image_data_list(image_filenames):
    img_request = []
    ctxt = b64encode(open(image_filename, 'rb').read()).decode()
    img_request.append({
            'image': {'content': ctxt},
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 1
            }]
    })
    return img_request

def make_image_data(image_filenames):
    imgdict = make_image_data_list(image_filenames)
    return json.dumps({'requests': imgdict}).encode()


def analyze() :
    out=requests.post('https://vision.googleapis.com/v1/images:annotate', 
        data=make_image_data(image_filename),
        params={'key': api_key},
        headers={'Content-Type': 'application/json'})
    return out

if __name__ == '__main__': 
    response=analyze()

    if response.status_code != 200 or response.json().get('error'):
        print(response.text)
    else:
        for i in range(len(response.json()['responses'][0]['textAnnotations'])):
            type(i)
            t=response.json()['responses'][0]['textAnnotations'][i]['description']
            print(t, end=" ")