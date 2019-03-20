import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGraphicsView

from scene import Scene


class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.top = 50
        self.left = 100
        self.resize(860, 520)
        self._init_window()
        self.show()

    def _init_window(self):
        self.scene = Scene()
        self.view = QGraphicsView(self.scene, self)
        self.view.setSceneRect(0, 0, 1, 1)

        box_layout = QHBoxLayout()
        box_layout.addWidget(self.view)
        box_layout.addWidget(self.scene.quick)
        self.setLayout(box_layout)

    def handleStatusChange(self, status):
        if status == self.quick.Error:
            [print(e.toString()) for e in self.quick.errors()]


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
