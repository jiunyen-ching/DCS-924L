import cv2
import requests
import numpy as np
from datetime import datetime
import os

# Text settings
font          = cv2.FONT_HERSHEY_SIMPLEX
coord         = (5,40)
fontScale     = 0.65
fontColor     = (0,255,0)
lineThickness = 2

def stamp(img,timestamp):
    cv2.putText(img,timestamp,
                coord,
                font,
                fontScale,
                fontColor,
                lineThickness)

def create_dir(YMD, HMS):
    DAY_DIR = os.path.join('/path/to/your/directory', YMD) # create parent dir with "YMD" as name
    HOUR_DIR = os.path.join(DAY_DIR, HMS[0:2]) # create folder with "hour" as name

    if not os.path.exists(DAY_DIR):
        os.mkdir(DAY_DIR)
    if not os.path.exists(HOUR_DIR):
        os.mkdir(HOUR_DIR)

    return(HOUR_DIR)

r = requests.get('http://<your_ip_address_here>/video/mjpg.cgi', auth=('<your_username_here>','<your_password_here>'), stream=True)
if(r.status_code == 200):
    bytes = bytes()
    for chunk in r.iter_content(chunk_size=1024):
        bytes += chunk # grow bytes as needed
        a = bytes.find(b'\xff\xd8') # find start marker
        b = bytes.find(b'\xff\xd9') # find end marker

        if a != -1 and b != -1: # if both markers are found, this is a valid JPG
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

            currenttime = datetime.now()
            timestamp_realtime = currenttime.strftime("%Y/%m/%d - %H:%M:%S:%f")
            YMD = currenttime.strftime('%Y%m%d') # year-month-day
            HMS = currenttime.strftime('%H%M%S_%f') # hour-minute-second

            # Check if directory exists, otherwise create it
            HOUR_DIR = create_dir(YMD, HMS)

            # Create filename for frame
            # filename = os.path.join(HOUR_DIR, HMS + '.png') # ~500 kb per file
            filename = os.path.join(HOUR_DIR, HMS + '.jpg') #  ~75 kb per file

            # Apply timestamp to frame
            stamp(img,timestamp_realtime)

            # Save timestamped frame
            cv2.imwrite(filename,img)

            # cv2.imshow('img', img)
            # if cv2.waitKey(1) == 27:
            #     exit(0)

            print('writing', timestamp_realtime)
else:
    print("Received unexpected status code {}".format(r.status_code))
