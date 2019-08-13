#!/usr/bin/python

import sys
from PyQt5 import QtWidgets
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType

import ctypes
from ctypes.util import find_library

from calculator import Calculator


def main():
    # There is a known issue on Ubuntu when using PyQt OpenGL with NVidia binary drivers
    # where it will load the Mesa GL libraries instead of the NVidia GL libraries and fail to compile shaders.
    libGL = find_library("GL")
    ctypes.CDLL(libGL, ctypes.RTLD_GLOBAL)

    app = QtWidgets.QApplication([])

    qmlRegisterType(Calculator, 'Calculator', 1, 0, 'Calculator')
    engine = QQmlApplicationEngine()
    engine.load("calculator.qml")

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
