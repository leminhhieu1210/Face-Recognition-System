import cv2
import sys
import argparse

vidcap = cv2.VideoCapture('E:\IT\Python\AI4E\cw2\inputvid\Vinh.mp4')
success, image = vidcap.read()
success = True
count = 0

while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 500))    # added this line, 500 = 2fps
    success, image = vidcap.read()
    cv2.imwrite("hieu%d.jpg" % count, image)     # save frame as JPEG file
    count = count + 1