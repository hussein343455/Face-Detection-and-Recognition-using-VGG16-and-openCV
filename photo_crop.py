import cv2
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from PIL import Image
###########################################################
person=["Kevin Hart" ,"ben_afflek" ,"dwayne_johnson" ,"elton_john" ,"jerry_seinfeld", "madonna" , "mindy_kaling", "Ryan Reynolds"]
#21 21 19 21 21 18 22 22
i=0
nonn=0
namex=""
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
###########################################################

#--------------------------name images to (ben affleck) and number them------------------
#returns (path + directory of all image)
# if not os.path.exists("5-celebrity-faces-dataset/train/ben_afflek2"):
#     os.makedirs('5-celebrity-faces-dataset/train/ben_afflek2')
# def changeName(img,name):
#     img = img.convert('RGB')
#     namex = name.split("k\\", 2)
#     if not os.path.exists("dwayne_johnson" + str(i) + ".jpg"):
#         img.save(str(namex[0]) + "k2/dwayne_johnson" + str(i) + ".jpg")
#     return namex
#--------------------------ends------------------
for k in person:
    path = "5-celebrity-faces-dataset/val/" + k
    if not os.path.exists(path):
        os.makedirs(path)
    for name in glob.glob(path+"B/*"):
        img = cv2.imread(name)
        namex = name.split("B\\", 2)
        faces = faceCascade.detectMultiScale(img, 1.16, 5)
        smiles = smile_cascade.detectMultiScale(img, 1.3, 20)
        eyes = eye_cascade.detectMultiScale(img, 1.3, 1)
        for (x, y, w, h) in faces:
            imgResults = img[y:y + h, x:x + w]
            face_img = Image.fromarray(imgResults)
            face_img.save((str(namex[0]) + "/"+k+ str(i) + ".jpg"))
            i+= 1
    i = 0

cv2.waitKey(0)