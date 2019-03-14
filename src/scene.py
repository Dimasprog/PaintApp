import sys
from PyQt5.QtWidgets import QGraphicsScene


class Scene(QGraphicsScene):

    def __init__(self, parent):
        # def sceneEventFilter(o, e):
        #     print(o, e)
        #     return False

        QGraphicsScene.__init__(self)
        self.scene = QGraphicsScene(parent)
        self.scene.installEventFilter(self)

        # self.scene.eventFilter = sceneEventFilter

    def eventFilter(self, source, event):
        print(event)
        print(source)

        return False