import hejin
import jianhun
import renyin
import xiazi
import huahua
import honggou
from untils import nextGame, checkisSafe, checkTime, findStartGameBtn, changeRole
import otherUntils
from time import sleep
import pydirectinput
pydirectinput.FAILSAFE = 5

startFuncArr = [hejin.start, renyin.start, xiazi.start, jianhun.start, huahua.start, honggou.start]
class GameContorler:
    _index = 0
    def startFight(self):
        if self._index == len(startFuncArr) or checkTime():
            if self._index == len(startFuncArr):
                otherUntils.chatWithweixin("所有角色刷完了")
            else:
                otherUntils.chatWithweixin("到时间了")
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
except Exception as e:
    try:
        otherUntils.chatWithweixin("try except错误")
        sleep(60)
        otherUntils.shutdown()
    except:
        sleep(60)
        otherUntils.shutdown()