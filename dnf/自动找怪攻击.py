import os
import auto
import cv2
import normal
import autoFindRoad
import common
import time
import test3
scale = 1
imgs = os.listdir('./monster/monster')

def func():
    auto.saveAndCropFunc()
    img = cv2.imread('./dnf.jpg')
    img = cv2.resize(img,(0,0),fx=scale,fy=scale)
    for item in imgs:
        template,template_size = auto.getImgInfo('./monster/monster/' + item)
        currImg, x, y = auto.search_returnPoint(img,template,template_size, 0.8)
        if x is None:
            continue
        else:
            return x, y
    return None, None
while True:
    time.sleep(1)
    x,y = func()
    if x is None:
        autoFindRoad.findRolePositionAndMoveCenter()
        continue
    normal.autoMoveRoleToGoal(x, y, 115)
    test3.autoAcctch()

