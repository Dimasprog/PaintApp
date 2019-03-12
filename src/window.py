import sys
from PyQt5.QtCore import QUrl, Qt, pyqtSignal
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGraphicsView, QGraphicsScene


class Window(QWidget):
    RIGHT_SIDEBAR_VIEW_PATH = "design.qml"

    clearAll = pyqtSignal()

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

    def _connect_ui(self):
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

    def _clearAll(self):
        print("Done!")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

