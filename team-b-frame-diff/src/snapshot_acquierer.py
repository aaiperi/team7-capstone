import requests
import urllib
import json
from korean_romanizer.romanizer import Romanizer
import cv2
import numpy as np
import warnings as warn
from datetime import datetime

# ---------------CHANGE THIS-------------------
# Set geographical latitude bounds
MIN_Y=36.48135
MAX_Y=36.5843

# Set geographical longtitude bounds
MIN_X=126.756
MAX_X=126.7936

# --------------DO NOT CHANGE THIS-----------------
# Image size settings
TARGET_H=480
TARGET_W=720

key = "404e9bfaf2cf45a68770cfaf84e1cd03"
url=f"https://openapi.its.go.kr:9443/cctvInfo?apiKey={key}&type=ex&cctvType=1&minX={MIN_X}&maxX={MAX_X}&minY={MIN_Y}&maxY={MAX_Y}&getType=json"

print("Requesting ITS JSON")
response=urllib.request.urlopen(url)
json_str=response.read().decode("utf-8")
json_obj=json.loads(json_str)
data=json_obj['response']['data']

print(f"Got JSON for area: X: {MIN_X} {MAX_X}; Y: {MIN_Y} - {MAX_Y}")
for camera in data:
    name=camera['cctvname']
    r = Romanizer(name)
    name=r.romanize()
    name=name.replace(" ", "_")
    name=name.replace(".", "-")

    print(f"Processing camera: {name}")

    print("Requesting video...")
    url=camera['cctvurl']
    capture=cv2.VideoCapture(url)
    ret, frame1=capture.read()
    ret, frame2=capture.read()


    h, w, _ = frame1.shape
    if h < TARGET_H or w < TARGET_W:
        warn.warn(f"Image: {name} is too small to fit into (480,720) SKIPPING.")
        continue
    elif h > TARGET_H or w > TARGET_W:
        print("NOTE: Resolution: {h}x{w} was out of bounds for target {TARGET_H}x{TARGET_W}, cropping...")
        center_y, center_x = h//2, w//2;
        start_x = center_x - (TARGET_W // 2)
        end_x = center_x + (TARGET_W // 2)
        start_y = center_y - (TARGET_H // 2)
        end_y = center_y + (TARGET_H // 2)
        frame1 = frame1[start_y:end_y, start_x:end_x]
        frame2 = frame2[start_y:end_y, start_x:end_x]

    print("Computing difference...")
    diff = cv2.absdiff(frame1, frame2)
    diff_img=cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    print("Saving images...")
    now=datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    cv2.imwrite(f"./output/diffs/{name}_{now}_diff.png", diff_img)
    cv2.imwrite(f"./output/frames/{name}_{now}_frame.png", frame2)
