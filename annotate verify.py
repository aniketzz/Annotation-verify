#-------------------------------------------------------------------------------
# Name:        Annotation Verifyer
#
# Purpose:     Verify the annotation done using the annotation.txt file. The
#              format supported is (filename, xmin, ymin, xmax, ymax, class_name)
#
# Author:      Aniket
#
# Created:     26-09-2020
#-------------------------------------------------------------------------------


import imutils
import numpy as np
import os
import cv2

path = "D:/variance.ai/faster-rcnn/"
text_path = path + "pose_all.txt"
count = 0
with open(text_path,'r') as f:
    print("Reading Text file")
    for line in f:
        line_split = line.strip().split(',')
        (filename,x1,y1,x2,y2,class_name) = line_split
        if filename[:1] == '"':
            filename = filename[26:]
            class_name = class_name[:-1]
        else:
            filename = filename[25:]
        #print(filename)920
        try:
            im=cv2.imread(path+"Val/"+filename)

            cv2.rectangle(im, (int(x1), int(y1)), (int(x2), int(y2)),(0, 255, 0), 2)
            cv2.putText(im, class_name, (int(x1),int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX,0.75, (25, 155, 205), 2)
            im = imutils.resize(im, width=400) ## just to fit in the screen. can be changed according to your screen size
            cv2.imshow("data",im)
            cv2.waitKey(0)
            count+=1
            #break
        except:
            pass
print(count,": Data Done")
cv2.destroyAllWindows()