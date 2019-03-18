from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QGraphicsScene


class Scene(QGraphicsScene):

    def __init__(self, parent):
        QGraphicsScene.__init__(self)
        self.scene = QGraphicsScene(parent)
        self.scene.mousePressEvent = self.mousePressEvent

    def getScene(self):
        return self.scene

    def mousePressEvent(self, e):
        p = QCursor.pos()
        print(p.x())
