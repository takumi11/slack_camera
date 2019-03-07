# -*- coding: utf-8 -*-

import sys
import os
import time
import cv2
import requests
from datetime import datetime
from slackbot.bot import respond_to

# botのトークン
TOKEN = 'xxxx-xxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx'

# 写真を撮る


@respond_to('部屋')
def takepicture_func(message):
    ImagePath = './Image/image.jpg'

    # 写真の撮影(webカメラ)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

    if cap.isOpened() is False:
        print("can not open camera")
        sys.exit()

    time.sleep(1)
    ret, frame = cap.read()
    cv2.imwrite(ImagePath, frame)
    cap.release()

    # 画像のアップロード

    # 投稿先のchannelのID
    CHANNEL = 'xxxxxxxx'
    TITLE = datetime(*time.localtime(os.path.getctime(ImagePath))[:6])
    files = {'file': open(ImagePath, 'rb')}
    param = {
        'token': TOKEN,
        'channels': CHANNEL,
        'filename': "image.jpg",
        'initial_comment': "いまの様子です",
        'title': TITLE
    }
    requests.post(url="https://slack.com/api/files.upload",
                  params=param, files=files)


@respond_to('こんにちは')
def mention_func(message):
    message.send('こんにちは')
