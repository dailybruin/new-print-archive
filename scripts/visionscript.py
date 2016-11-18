from base64 import b64encode

import requests
import json

image_filename= 'C:/Users/Andrew/Documents/dailybruin/archive/page-004.pdf.header.jpg' # file name goes here
api_key= 'AIzaSyD6kpyzItHfRlJNEmRTFRF5HDdCNXMYPhQ'                                     # API key goes here

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

def extract_y(data) :
    try:
        out=data['boundingPoly']['vertices'][1]['y']
    except KeyError:
        print("ERROR", end='\n')
        return 0
    return out

def sort(data) :        # main problem: what if the dates are on the same y coordinate as another string?
    out = sorted(data.json()['responses'][0]['textAnnotations'], key=extract_y)
    return out;

if __name__ == '__main__': 
    response=analyze()
    if response.status_code != 200 or response.json().get('error'):
        print(response.text)
    else:
        data=sort(response)
        for i in range(1, len(data)) :
            # the first element in the json is all lines of text in the json, separated by a \n. Delete the '1,' in the range()
            # if you need the first element.
            t=data[i]['description']
            print(t, end="\n")
