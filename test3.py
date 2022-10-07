from time import sleep
import os
import auto
import common
from PIL import Image

imgs = os.listdir('./skill_img/gui_qi')
monster_imgs = os.listdir('./monster/monster')

def getSkillImg():
  auto.saveAndCropFunc('skill', [299,533,515, 594])
  img = Image.open('./skill.jpg')
  s = []
  s.append(['q', 'w', 'e', 'r', 't', 'v', 'ctrl'])
  s.append(['a', 's', 'd', 'f', 'g', 'h', 'alt'])
  for j in range(2):
    for i in range(7):
      region = img.crop([30 * i + i,30 * j, 30 + i + 30 * i, 30 + 30 * j])
      region.save('./skill_img/hua_hua/' + s[j][i] + '.jpg')


def autoAcctch():
  auto.saveAndCropFunc()
  for item in imgs:
    x, y = auto.getImg1AndImg2('./skill_img/gui_qi/' + item, './dnf.jpg', 0.85)
    if x != 0:
      keyBoy = item.split('.')
      common.otherKeys(keyBoy[0])
      break
while True:
  sleep(1)
  autoAcctch()