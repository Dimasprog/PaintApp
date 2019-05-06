import QtQuick 2.12
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.1

Rectangle {
    id: main
    width: 220
    color: "#b6c6ed"

    property int shapeRectSize: main.width / 3 - 10

    signal changeColor(string colorName)
    signal setShape(string shape)
    signal clear()

    function getColor(index) {
        if (index == 0)
            return "red"
        if (index == 1)
            return "black"
        if (index == 2)
            return "blue"
        if (index == 3)
            return "purple"
        if (index == 4)
            return "green"
        if (index == 5)
            return "yellow"
    }

    Column {
        spacing: 20
        anchors.horizontalCenter: parent.horizontalCenter

        Rectangle {
            id: spanRect
            color: main.color
            height: 1
            width: 10
        }

        Rectangle {
            id: colorPicker
            width: main.width - 20
            height: 30
            color: "white"

            ListView {
                id: listView
                anchors.fill: parent
                model: 6
                orientation: ListView.Horizontal

                delegate: Rectangle {
                    width: colorPicker.width / 6
                    height: colorPicker.height
                    color: getColor(index)

                    MouseArea {
                        anchors.fill: parent
                        hoverEnabled: true
                        onEntered: parent.opacity =  0.4
                        onExited: parent.opacity =  1
                        onClicked: {
                            chosenColor.color = parent.color
                            changeColor(chosenColor.color)
                        }
                    }
                }
            }
        }

        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            spacing: 5

            Rectangle {
                id: buttonRectangle
                color: "black"
                width: shapeRectSize
                height: buttonRectangle.width
                border.width: 2

                Image {
                    anchors.centerIn: parent
                    sourceSize.width: parent.width - 2
                    sourceSize.height: parent.height - 2
                    source: "img/square.png"
                }

                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onEntered: parent.border.color = main.color
                    onPressed: parent.border.color = "red"
                    onReleased: parent.border.color = "black"
                    onExited: parent.border.color = "black"
                    onClicked: setShape("rectangle")
                }
            }

            Rectangle {
                id: buttonLine
                color: "black"
                width: shapeRectSize
                height: buttonLine.width

                Image {
                    anchors.centerIn: parent
                    sourceSize.width: parent.width - 2
                    sourceSize.height: parent.height - 2
                    source: "img/line.png"
                }

                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onEntered: parent.border.color = main.color
                    onPressed: parent.border.color = "red"
                    onReleased: parent.border.color = "black"
                    onExited: parent.border.color = "black"
                    onClicked: setShape("line")
                }
            }

            Rectangle {
                id: buttonBrush
                color: "black"
                width: shapeRectSize
                height: buttonBrush.width

                Image {
                    anchors.centerIn: parent
                    sourceSize.width: parent.width - 2
                    sourceSize.height: parent.height - 2
                    source: "img/brush.png"
                }

                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onEntered: parent.border.color = main.color
                    onPressed: parent.border.color = "red"
                    onReleased: parent.border.color = "black"
                    onExited: parent.border.color = "black"
                    onClicked: setShape("brush")
                }
            }
        }

        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            spacing: 5

            TextArea {
                text: "Color: "
                font.pixelSize: 20
                color: "black"
            }

            Rectangle {
                id: chosenColor
                width: 40
                height: 40
                color: "black"
                border.color: "black"
                radius: 20
            }
        }

        Rectangle {
            anchors.horizontalCenter: parent.horizontalCenter
            width: 140
            height: 40
            color: "#c4c4c4"
            border.color: "black"

            Text {
                anchors.centerIn: parent
                text: qsTr("Clear")
                font.pixelSize: 20
            }

            MouseArea {
                anchors.fill: parent
                hoverEnabled: true
                onEntered: parent.width = 136
                onExited: parent.width = 140
                onClicked: clear()
            }
        }
    }
}