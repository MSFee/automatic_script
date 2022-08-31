from sys import flags
from time import sleep
import cv2
from PIL import ImageGrab
import numpy as np
import common
scale = 1

def getImgInfo(img_address):
    template = cv2.imread(img_address)
    template = cv2.resize(template, (0, 0), fx=scale, fy=scale)
    template_size= template.shape[:2]
    return template, template_size

template,template_size = getImgInfo('./pic/role.jpg')
roleLeft,roleLeft_size = getImgInfo('./pic/role-left.jpg')
roleRight,roleRight_size = getImgInfo('./pic/role-right.jpg')
door,door_size = getImgInfo('./pic/door.jpg')
close_door,close_door_size = getImgInfo('./pic/close_door.jpg')
taskDoor,taskDoor_size = getImgInfo('./pic/emergency_door.jpg')

# 根据图片地址判断两张图片的位置
def getImg1AndImg2(address1, address2, threshold = 0.6):
    addressImg1,addressImg1_size = getImgInfo(address1)
    addressImg2,addressImg2_size = getImgInfo(address2)
    img,x,y = search_returnPoint(addressImg1, addressImg2, addressImg2_size, threshold)
    if x is None:
        return 0, 0
    return x, y


# 截图方法
def saveAndCropFunc(address = 'dnf', cropPosition = [0,0,800,600]):
    img = ImageGrab.grab()
    x,y,crop_x,crop_y = cropPosition
    region = img.crop((x,y,crop_x,crop_y))
    region.save(address + '.jpg')

#找图 返回最近似的点
def search_returnPoint(img,template,template_size, threshold = 0.6):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_ = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_gray, template_,cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    # res大于70%
    loc = np.where(result >= threshold)
    # 使用灰度图像中的坐标对原始RGB图像进行标记
    point = ()
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + template_size[1], pt[1] + + template_size[0]), (7, 249, 151), 2)
        point = pt
    if point==():
        return None,None,None
    return img,point[0]+ template_size[1] /2,point[1]

def getRoleAndDoor(isTaskDoor = False, flag = 0):
    saveAndCropFunc()
    img = cv2.imread('./dnf.jpg')
    img = cv2.resize(img,(0,0),fx=scale,fy=scale)
    try:
        if flag == 1:
            img_,x_,y_ = search_returnPoint(img,roleRight,roleRight_size)
        elif flag == 2:
            img_,x_,y_ = search_returnPoint(img,roleLeft,roleLeft_size)
        else:
            img_,x_,y_ = search_returnPoint(img,template,template_size)
        if x_ is None:
            if flag == 0:
               return getRoleAndDoor(isTaskDoor, 1)
            elif flag == 1:
               return getRoleAndDoor(isTaskDoor, 2)
            else:
                return False, False
        if isTaskDoor is True:
            door_,door_x,door_y = search_returnPoint(img,taskDoor,taskDoor_size)
        else:
            door_,door_x,door_y = search_returnPoint(img,door,door_size)
        x_distance = door_x - x_
        y_distance = door_y - y_ - 150
        return x_distance / 200, y_distance / 200
    except Exception as e:
        return None,None

# 获取角色当前在地图中的位置
def getRoleCurrPosition(flag = 0):
    saveAndCropFunc()
    if flag == 0:
        role,role_size = getImgInfo('./pic/role.jpg')
    elif flag == 1:
        role,role_size = getImgInfo('./pic/role-left.jpg')
    else:
        role,role_size = getImgInfo('./pic/role-right.jpg')
    img,img_size = getImgInfo('./dnf.jpg')
    img_,x,y = search_returnPoint(img,role,role_size)
    if x != None:
        return x, y + 161
    elif flag > 4:
        return 0,0
    else:
        if flag == 1:
            return getRoleCurrPosition(flag + 1)
        elif flag == 2:
            return getRoleCurrPosition(flag + 1)
        else:
            return getRoleCurrPosition(flag + 1)

# 获取角色到地图纵向距离
def getRoleAndMiddle(cropPosition = [0,0,800,600]):
    sleep(0.5)
    saveAndCropFunc('dnf', cropPosition)
    img,img_size = getImgInfo('./dnf.jpg')
    img_,x,y = search_returnPoint(img,template,template_size)
    img_2,x_2,y_2 = search_returnPoint(img,close_door,close_door_size)
    if y is None:
        return 0
    if y_2 is None:
        return 0
    y_2 += 20
    y += 173 # 称号到角色脚的距离
    return y_2 - y

# 判断当前小地图是否符合预期
def judgeMap(mapName, isPre = False):
    saveAndCropFunc('dnf')
    if isPre is True:
        map,map_size = getImgInfo('./map/wangMap/'+ mapName +'.jpg')
    else:
        map,map_size = getImgInfo('./map/wang/'+ mapName +'.jpg')
    img,img_size = getImgInfo('./dnf.jpg')
    img_,x,y = search_returnPoint(img, map, map_size, 0.89)
    if x is None:
        return False
    else:
        return True

# 查找当前地图是否爆出史诗装备
def checkHasEpic():
    saveAndCropFunc('dnf')
    monster4,monster4_size = getImgInfo('./others_pic/epic.jpg')
    img,img_size = getImgInfo('./dnf.jpg')
    img_,x,y = search_returnPoint(img,monster4,monster4_size, 0.8)
    if x is None:
        return False
    return True

# 判断当前地图是否产生紧急任务
def checkHasTask():
    saveAndCropFunc('dnf')
    monster4,monster4_size = getImgInfo('./pic/emergency_door.jpg')
    img,img_size = getImgInfo('./dnf.jpg')
    img_,x,y = search_returnPoint(img,monster4,monster4_size, 0.7)
    if x is None:
        return 0, 0
    return x, y

# 判断是否走到分解机附近
def checkHasMachine():
    saveAndCropFunc()
    img,img_size = getImgInfo('./dnf.jpg')
    machine,machine_size = getImgInfo('./others_pic/machine.jpg')
    curr, x, y = search_returnPoint(img,machine,machine_size, 0.9)
    if x is None:
        return False
    else:
        return True