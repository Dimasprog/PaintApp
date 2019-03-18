from PyQt5.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent


class Scene(QGraphicsScene):

    def __init__(self, parent):
        QGraphicsScene.__init__(self)
        self.i = 0
        def sceneEventFilter(o, event):
            # print(o, event)
            # print(type(event))


            if isinstance(event, QGraphicsSceneMouseEvent):
                print("Ai umblat pe scena", self.i)
                self.i += 1
            # print("QPoint({0}, {1}) in screen coords".format(
            #     event.pos().x(), event.pos().y()))
            return False
        self.scene = QGraphicsScene(parent)

        self.scene.installEventFilter(self.scene)
        self.scene.eventFilter = sceneEventFilter

    def getScene(self):
        return self.scene;