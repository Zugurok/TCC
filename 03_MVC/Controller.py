from View import *
from Model import *
import sys


class Controller:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self._model = Methods
        self._view = Main()
        self.init()

    def init(self):
        self._view.show()
        return sys.exit(self.app.exec_())


if __name__ == '__main__':
    c = Controller()
    c.init()
