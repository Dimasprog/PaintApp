import QtQuick 2.12
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3

Item {
    id: main
    width: 220

    /* SIGNALS */


    /* DESIGN */

    Rectangle { id: menu
        width: 220
        height: main.height
        color: "#fffa9e"

        ColumnLayout { id: col
            Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
            spacing: 15
            /*
            anchors.centerIn: parent
            */

            Rectangle {
                Layout.alignment: Qt.AlignCenter
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
                }

                Button { id: button2
                    x: button1.x + parent.width / 6
                    y: button1.y
                    width: parent.width / 6
                    height: parent.height - 2

                    background: Rectangle {
                        color: "black"
                        opacity: enabled ? 1 : 0.3
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
                }

                Button { id: button4
                    x: button3.x + parent.width / 6
                    y: button3.y
                    width: parent.width / 6
                    height: parent.height - 2

                    background: Rectangle {
                        color: "red"
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
                }

                Button { id: button6
                    x: button5.x + parent.width / 6
                    y: button5.y
                    width: parent.width / 6 - 2
                    height: parent.height - 2

                    background: Rectangle {
                        color: "#630051" // violet
                    }
                }
            }

            Rectangle {
                Layout.alignment: Qt.AlignCenter
                Layout.preferredWidth: main.width - 10
                Layout.preferredHeight: menu.width / 3
                color: "white"
                border.color: "black"
            }
            Button {
                Layout.alignment: Qt.AlignCenter
                text: "asdv"
            }

        }
    }
}