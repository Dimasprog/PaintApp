from PyQt5.QtWidgets import QGraphicsScene


class Scene(QGraphicsScene):

    def __init__(self, parent):
        QGraphicsScene.__init__(self)

        def sceneEventFilter(o, e):
            print(o, e)
            return False
        self.scene = QGraphicsScene(parent)

        self.scene.installEventFilter(self.scene)
        self.scene.eventFilter = sceneEventFilter

    def getScene(self):
        return self.scene;