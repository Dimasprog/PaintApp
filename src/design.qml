import QtQuick 2.12
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.1


Item {

    id: main
    width: 220

    /* SIGNALS */

    signal setMode(string sMode)
    signal clearAll()
    signal changeColor(string sColor)


    /* DESIGN */
    Rectangle { id: menu
        width: parent.width
        height: parent.height
        color: "#b6c6ed"

        ColumnLayout { id: col
            spacing: 15
            anchors.horizontalCenter: parent.horizontalCenter
            Rectangle {
                Layout.preferredWidth: main.width - 10
                Layout.preferredHeight: 30
                color: "white"
                border.color: "black"

                Button { id: button1
                    x: parent.x + 1
                    y: parent.y + 1
                    width: parent.width / 6
                    height: parent.height - 2

                    background: Rectangle {
                        color: "white"
                    }

                    onClicked: {
                        chosenColor.color = "white"
                        changeColor(chosenColor.color)
                    }
                }

                Button { id: button2
                    x: button1.x + parent.width / 6
                    y: button1.y
                    width: parent.width / 6
                    height: parent.height - 2

                    background: Rectangle {
                        color: "black"
                    }

                    onClicked: {
                        chosenColor.color = "black"
                        changeColor(chosenColor.color)
                    }
                }

                Button { id: button3
                    x: button2.x + parent.width / 6
                    y: button2.y
                    width: parent.width / 6
                    height: parent.height - 2

                    background: Rectangle {
                        color: "#eeff00" // yellow
                    }

                    onClicked: {
                        chosenColor.color = "#eeff00"
                        changeColor(chosenColor.color)
                    }
                }

                Button { id: button4
                    x: button3.x + parent.width / 6
                    y: button3.y
                    width: parent.width / 6
                    height: parent.height - 2

                    background: Rectangle {
                        color: "red"
                    }

                    onClicked: {
                        chosenColor.color = "red"
                        changeColor(chosenColor.color)
                    }
                }

                Button { id: button5
                    x: button4.x + parent.width / 6
                    y: button4.y
                    width: parent.width / 6
                    height: parent.height - 2

                    background: Rectangle {
                        color: "blue"
                    }

                    onClicked: {
                        chosenColor.color = "blue"
                        changeColor(chosenColor.color)
                    }
                }

                Button { id: button6
                    x: button5.x + parent.width / 6
                    y: button5.y
                    width: parent.width / 6 - 2
                    height: parent.height - 2

                    background: Rectangle {
                        color: "#630051" // violet
                    }

                    onClicked: {
                        chosenColor.color = "#630051"
                        changeColor(chosenColor.color)
                    }
                }
            }

            Rectangle { id: rectangleShapes
                Layout.preferredWidth: main.width - 10
                Layout.preferredHeight: menu.width / 3
                color: "black"
                border.color: "black"

                Button {
                    id: buttonRectangle
                    text: "☐"
                    x: rectangleShapes.x + 1
                    y: + 1
                    width: rectangleShapes.width / 3 - 2
                    height: rectangleShapes.height - 2

                    MouseArea {
                        anchors.fill: parent
                        onClicked: setMode("Rectangle")
                    }
                }

                Button {
                    id: buttonSegment
                    text: "/"
                    x: buttonRectangle.x + rectangleShapes.width / 3
                    y: + 1
                    width: rectangleShapes.width / 3 - 2
                    height: rectangleShapes.height - 2

                    MouseArea {
                        anchors.fill: parent
                        onClicked: setMode("Segment")
                    }
                }

                Button {
                    id: buttonDrawForever
                    text: "〰"
                    x: buttonSegment.x + rectangleShapes.width / 3
                    y: + 1
                    width: rectangleShapes.width / 3 - 2
                    height: rectangleShapes.height - 2

                    MouseArea {
                        anchors.fill: parent
                        onClicked: setMode("Forever")
                    }
                }
            }

            RowLayout { id: squareDisplayColor
                Layout.alignment: Qt.AlignHCenter
                spacing: 10

                TextArea {
                    text: "Color: "
                }
                Rectangle { id: chosenColor
                    Layout.preferredWidth: 40
                    Layout.preferredHeight: 40
                    color: "black"
                    border.color: "black"
                    radius: 20
                }
            }

            Rectangle { id: clearAllButtonSection
                Layout.alignment: Qt.AlignHCenter
                Layout.preferredWidth: parent.width - 10
                Layout.preferredHeight: 30
                Button { id: clearAllBtn
                    width: parent.width
                    height: 30
                    text: "Clear All"
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: clearAll()
                }
            }
        }
    }
}