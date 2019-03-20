from PyQt5.QtCore import QLineF
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsLineItem, QGraphicsItem


class Scene(QGraphicsScene):

    def __init__(self, parent):
        QGraphicsScene.__init__(self)
        self.scene = QGraphicsScene(parent)
        self.scene.mousePressEvent = self.mousePressEvent
        self.firstClick = True
        self.secondClick = False
        self.firstClickPos = QCursor.pos()
        self.secondClickPos = QCursor.pos()

    def getScene(self):
        return self.scene

    def mousePressEvent(self, e):

        # X and Y is Off the Axe
        if self.firstClick:
            self.firstClickPos = QCursor.pos()
            self.firstClick = False
        else:
            self.secondClickPos = QCursor.pos()
            self.secondClick = True

        if self.secondClick:
            print(self.firstClickPos, "Prime Click")
            print(self.secondClickPos, "Second Click")


            x1 = self.firstClickPos.x()
            y1 = self.firstClickPos.y()
            x2 = self.secondClickPos.x()
            y2 = self.secondClickPos.y()
            line = QLineF(float(x1), float(y1), float(x2), float(y2))
            line_item = QGraphicsLineItem(line)
            line_item.setFlag(QGraphicsItem.ItemIsMovable, True)
            self.scene.addItem(line_item)
            self.firstClick = True
            self.secondClick = False