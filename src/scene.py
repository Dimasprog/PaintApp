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

        self.pen = QPen(QColor("#000000"), 4)

        self.origin_pos = None
        self.current_pos = None
        self.mode = None

    def _define_ui(self):
        self.quick = QQuickWidget()
        self.quick.setSource(QUrl().fromLocalFile(Scene.RIGHT_SIDEBAR_VIEW_PATH))
        self.quick.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self._root_object = self.quick.rootObject()

    def _connect_ui(self):
        self._root_object.changeColor.connect(self._change_color)
        self._root_object.setShape.connect(self._set_shape)
        self._root_object.clear.connect(self._clear)

    def mousePressEvent(self, event):
        self.origin_pos = event.scenePos()

    def mouseMoveEvent(self, event):
        self.current_pos = event.scenePos()

        if self.mode == "rectangle":
            self.draw_rectangle()
        if self.mode == "line":
            self.draw_line()
        if self.mode == "brush":
            self.draw_curve()

    def draw_rectangle(self):
        rect = QRectF(self.origin_pos, self.current_pos)
        rect_item = QGraphicsRectItem(rect)
        rect_item.setPen(self.pen)
        rect_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        if len(self.items()) > 0:
            self.clear_last_item()
        self.addItem(rect_item)

    def draw_line(self):
        line = QLineF(self.origin_pos, self.current_pos)
        line_item = QGraphicsLineItem(line)
        line_item.setPen(self.pen)
        line_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        if len(self.items()) > 0:
            self.clear_last_item()
        self.addItem(line_item)

    def draw_curve(self):
        curve = QLineF(self.origin_pos, self.current_pos)
        curve_item = QGraphicsLineItem(curve)
        curve_item.setPen(self.pen)
        curve_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.addItem(curve_item)
        self.origin_pos = self.current_pos

    def clear_last_item(self):
        self.removeItem(self.items()[len(self.items()) - 1])
        self.update()

    @pyqtSlot(str)
    def _change_color(self, color):
        self.pen = QPen(QColor(color), 4)

    @pyqtSlot(str)
    def _set_shape(self, mode):
        self.mode = mode

    @pyqtSlot()
    def _clear(self):
        if self:
            for item in self.items():
                self.removeItem(item)
                self.update()
