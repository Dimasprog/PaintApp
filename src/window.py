import sys
from PyQt5.QtCore import QUrl, Qt, pyqtSignal, pyqtSlot, QRectF, QLineF
from PyQt5.QtGui import QPen, QPainter, QColor
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsRectItem, \
    QGraphicsItem, QGraphicsLineItem

# Hello


class Window(QWidget):
    RIGHT_SIDEBAR_VIEW_PATH = "design.qml"

    def __init__(self):
        QWidget.__init__(self)
        self.top = 50
        self.left = 100
        self.resize(860, 520)

        self._define_ui()
        self._init_window()
        self._connect_ui()
        self.show()

    def _define_ui(self):
        self.quick = QQuickWidget()
        self.quick.setSource(QUrl().fromLocalFile(Window.RIGHT_SIDEBAR_VIEW_PATH))
        self.quick.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self._rectangle = self.quick.rootObject()
        self._line = self.quick.rootObject()
        self._clear = self.quick.rootObject()

    def _connect_ui(self):
        self._rectangle.drawRectangle.connect(self._drawRectangle)
        self._line.drawLine.connect(self._drawLine)
        self._clear.clearAll.connect(self._clearAll)

        self.quick.statusChanged.connect(self.handleStatusChange)

    def _init_window(self):
        self.scene = QGraphicsScene()

        view = QGraphicsView(self.scene, self)
        view.show()

        box_layout = QHBoxLayout()
        box_layout.addWidget(view)
        box_layout.addWidget(self.quick)
        self.setLayout(box_layout)

    def handleStatusChange(self, status):
        if status == self.quick.Error:
            [print(e.toString()) for e in self.quick.errors()]

    @pyqtSlot(str)
    def _drawRectangle(self, color):
        pen = QPen(QColor(color), 7)
        rect = QRectF(50, 50, 100, 100)
        rect_item = QGraphicsRectItem(rect)
        rect_item.setPen(pen)
        rect_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.scene.addItem(rect_item)

    @pyqtSlot(str)
    def _drawLine(self, color):
        pen = QPen(QColor(color), 7)
        line = QLineF(10, 10, 100, 100)
        line_item = QGraphicsLineItem(line)
        line_item.setPen(pen)
        line_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.scene.addItem(line_item)

    @pyqtSlot()
    def _clearAll(self):
        if self.scene:
            list = self.scene.items()
            for l in list:
                self.scene.removeItem(l)



app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

