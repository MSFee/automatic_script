import hejin
import jianhun
import renyin
import xiazi
import huahua
import honggou
from untils import nextGame, checkisSafe, checkTime, checkHasCloseBtn
import otherUntils
import autoFindRoad
import auto
from time import sleep
import common
import pydirectinput
pydirectinput.FAILSAFE = 5

startFuncArr = [honggou.start, renyin.start, jianhun.start, huahua.start, xiazi.start, hejin.start]
class GameContorler:
    _index = 2
    def startFight(self):
        if self._index == len(startFuncArr) or checkTime():
            otherUntils.shutdown()
            return
        start = startFuncArr[self._index]
        checkisSafe()
        start()
        result, num = nextGame()
        if num == 1:
            self._index = self._index + 1
        self.startFight()


game = GameContorler()    
try:
    game.startFight()
except:
    sleep(60)
    otherUntils.shutdown()