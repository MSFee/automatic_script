import hejin
import jianhun
import renyin
import xiazi
import huahua
from untils import nextGame
import autoFindRoad

startFuncArr = [renyin.start, jianhun.start, huahua.start, xiazi.start, hejin.start]
class GameContorler:
    _index = 1
    def startFight(self):
        if self._index == startFuncArr.__len__:
            print('所有角色均刷图完毕')
            return
        start = startFuncArr[self._index]
        start()
        result, num = nextGame()
        if num == 1:
            self._index = self._index + 1
        self.startFight()


game = GameContorler()       
game.startFight()