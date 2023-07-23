import hejin
import jianhun
import renyin
import xiazi
import huahua
import honggou
from untils import nextGame, checkisSafe, loginGame
import otherUntils
import autoFindRoad

startFuncArr = [honggou.start, renyin.start, jianhun.start, huahua.start, xiazi.start, hejin.start]
class GameContorler:
    _index = 0
    def startFight(self):
        if self._index == len(startFuncArr):
            print('所有角色均刷图完毕')
            loginGame(False, False) # 退出游戏，不在登陆
            return
        start = startFuncArr[self._index]
        checkisSafe()
        start()
        result, num = nextGame(self._index == 2)
        if num == 1:
            self._index = self._index + 1
        self.startFight()


game = GameContorler()    
game.startFight()
