import Calculator 1.0
import QtQuick 2.5
import QtQuick.Window 2.0

Window {
    id: window
    visible: true
    width: 320
    height: 480

    Calculator {
        id: calc
    }

    Rectangle {
        id: resultArea
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        height: parent.height * 3 / 8 - 10
        border.color: "white"
        border.width: 1
        color: "#46a2da"
        Text {
            id: resultText
            anchors.leftMargin: buttons.implicitMargin
            anchors.rightMargin: buttons.implicitMargin
            anchors.fill: parent
            horizontalAlignment: Text.AlignRight
            verticalAlignment: Text.AlignVCenter
            text: ""
            color: "white"
            font.pixelSize: window.height * 3 / 32
            font.family: "Open Sans Regular"
            fontSizeMode: Text.Fit
        }
    }

    Item {
        id: buttons
        anchors.top: resultArea.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        property real implicitMargin: {
            var ret = 0;
            for (var i = 0; i < visibleChildren.length; ++i) {
                var child = visibleChildren[i];
                ret += (child.implicitMargin || 0);
            }
            return ret / visibleChildren.length;
        }

         Repeater {
            id: operations
            model: ["÷", "×", "+", "-"]
            Button {
                y: 0
                x: index * width
                width: parent.width / 4
                height: parent.height / 5
                color: pressed ? "#5caa15" : "#80c342"
                text: modelData
                fontHeight: 0.4
                onClicked: { calc.change_operator(text) }
            }
        }

         Repeater {
            id: digits
            model: ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", ".", "C"]
            Button {
                x: (index % 3) * width
                y: Math.floor(index / 3 + 1) * height
                width: parent.width / 4
                height: parent.height / 5
                color: pressed ? "#d6d6d6" : "#eeeeee"
                text: modelData
                onClicked: { resultText.text = calc.change_number(text) }
            }
        }

         Button {
            id: resultButton
            x: 3 * width
            y: parent.height / 5
            textHeight: y - 2
            fontHeight: 0.4
            width: parent.width / 4
            height: y * 4
            color: pressed ? "#e0b91c" : "#face20"
            text: "="
            onClicked: {
                resultText.text = calc.calculation()
            }
        }
    }
}