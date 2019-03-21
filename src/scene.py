from PyQt5.QtCore import pyqtSlot, QUrl, QLineF, QRectF
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsLineItem, QGraphicsItem, QGraphicsRectItem


class Scene(QGraphicsScene):
    RIGHT_SIDEBAR_VIEW_PATH = "design.qml"

    def __init__(self):
        QGraphicsScene.__init__(self)
        self._define_ui()
        self._connect_ui()

        self.color = "#000000"
        self.pen = QPen(QColor(self.color), 4)

        self.originPos = None
        self.currentPos = None

        self.default = "Default"
        self.mode = self.default
        self.die = False

    def _define_ui(self):
        self.quick = QQuickWidget()
        self.quick.setSource(QUrl().fromLocalFile(Scene.RIGHT_SIDEBAR_VIEW_PATH))
        self.quick.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self._rootObject = self.quick.rootObject()

    def _connect_ui(self):
        self._rootObject.changeColor.connect(self._changeColor)
        self._rootObject.setMode.connect(self._setMode)
        self._rootObject.clearAll.connect(self._clearAll)

    @pyqtSlot(str)
    def _changeColor(self, color):
        self.color = color
        self.pen = QPen(QColor(self.color), 4)


    @pyqtSlot(str)
    def _setMode(self, mode):
        self.mode = mode

    @pyqtSlot()
    def _clearAll(self):
        if self:
            for item in self.items():
                self.removeItem(item)
                self.die = False
                self.update()

    def clearLastItem(self):
        self.removeItem(self.items()[len(self.items()) - 1])
        self.update()

    def mousePressEvent(self, event):
        self.originPos = event.scenePos()

    def mouseMoveEvent(self, event):
        self.currentPos = event.scenePos()

        if self.die:
            print("Rest in Peace")
        else:
            if self.mode == "Segment":
                self.drawSegment()
            if self.mode == "Rectangle":
                self.drawRect()
            if self.mode == "Forever":
                self.drawForever()

    def mouseReleaseEvent(self, event):
        self.die = True

    def drawRect(self):
        rect = QRectF(self.originPos, self.currentPos)
        rect_item = QGraphicsRectItem(rect)
        rect_item.setPen(self.pen)
        rect_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        if len(self.items()) > 0:
            self.clearLastItem()
        self.addItem(rect_item)

    def drawSegment(self):
        line = QLineF(self.originPos, self.currentPos)
        line_item = QGraphicsLineItem(line)
        line_item.setPen(self.pen)
        line_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        if len(self.items()) > 0:
            self.clearLastItem()
        self.addItem(line_item)

    def drawForever(self):
        line = QLineF(self.originPos, self.currentPos)
        line_item = QGraphicsLineItem(line)
        line_item.setPen(self.pen)
        line_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.addItem(line_item)
        self.originPos = self.currentPos
