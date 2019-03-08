import QtQuick 2.12
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.0

Item {
    id: main
    width: 220

    /* SIGNALS */


    /* DESIGN */

    Rectangle { id: menu
        width: 220
        height: main.height
        color: "#4da6ff"

        Column { id: col
            spacing: 15
            anchors.centerIn: parent
        }
    }
}