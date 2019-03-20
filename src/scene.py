from PyQt5.QtCore import QLineF
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsLineItem, QGraphicsItem


class Scene(QGraphicsScene):

    def __init__(self, parent):
        QGraphicsScene.__init__(self)
        self.firstClick = True
        self.firstClickPos = None

    def mousePressEvent(self, event):
        if self.firstClick:
            self.firstClickPos = event.scenePos()
            self.firstClick = False

    def clearLastItem(self):
        self.removeItem(self.items()[len(self.items()) - 1])
        self.update()

    def mouseMoveEvent(self, event):
        line = QLineF(self.firstClickPos, event.scenePos())
        line_item = QGraphicsLineItem(line)
        line_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        if len(self.items()) > 0:
            self.clearLastItem()
        self.addItem(line_item)
        self.firstClick = True
