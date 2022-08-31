from time import sleep
# import normal
import auto
import autoFindRoad
import common
# import easyocr
def saveJpg(position = None):
    if position is None:
        auto.saveAndCropFunc('dnf')
    else:
        auto.saveAndCropFunc('monster2', position)
def testF(name):
    for i in range(len(name)):
        monster4,monster4_size = auto.getImgInfo('./map/wang/' + name[i] + '.jpg')
        img,img_size = auto.getImgInfo('./dnf.jpg')
        img_,x,y = auto.search_returnPoint(img,monster4,monster4_size, 0.9)
        if x is None:
            continue
        print('命中第' + str(i+1) + '张图片')
        return x,y + 130
    # saveJpg([x + 40, y, x + 80, y + 16])
    return None, None

# saveJpg()
# testF(['1','2', '3', '4', '5'])

# 自动攻击脚本
# while 1:
#     sleep(2) 
#     saveJpg()
#     x, y = testF(['1','2', '3', '4', '5', '6', '7'])
#     if x is None:
#         print('全部未命中')
#         continue
#     normal.autoMoveRoleToGoal(x,y, 62)
#     n = 1
#     while n <= 10:
#         common.otherKeys('x')
#         n+=1

# while n <= 10:
#     saveJpg()
#     testF() 
#     sleep(2)
#     n+=1
# text = easyocr.Reader(['ch_sim', 'en'])
# shuju = text.readtext('./monster2.jpg', detail=0)
# print(shuju)
