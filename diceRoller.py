import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bomby's Dice Roller")
        self.buttonD4 = QtWidgets.QPushButton("Roll D4")
        self.buttonD6 = QtWidgets.QPushButton("Roll D6")
        self.buttonD8 = QtWidgets.QPushButton("Roll D8")
        self.buttonD10 = QtWidgets.QPushButton("Roll D10")
        self.buttonD12 = QtWidgets.QPushButton("Roll D12")
        self.buttonD20 = QtWidgets.QPushButton("Roll D20")
        self.buttonD100 = QtWidgets.QPushButton("Roll D100")
        self.text = QtWidgets.QLabel("<h1>Roll Dice</h1>",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.buttonD4)
        self.layout.addWidget(self.buttonD6)
        self.layout.addWidget(self.buttonD8)
        self.layout.addWidget(self.buttonD10)
        self.layout.addWidget(self.buttonD20)
        self.layout.addWidget(self.buttonD100)
        self.min = 0
        self.max = 10
        self.buttonD4.clicked.connect(self.roll4)
        self.buttonD6.clicked.connect(self.roll6)
        self.buttonD8.clicked.connect(self.roll8)
        self.buttonD10.clicked.connect(self.roll10)
        self.buttonD20.clicked.connect(self.roll20)
        self.buttonD100.clicked.connect(self.roll100)

    @QtCore.Slot()
    def roll4(self):
        self.text.setText("<h1>" + str(random.randint(1,4)) + "</h1>")
    def roll6(self):
        self.text.setText("<h1>" + str(random.randint(1,6)) + "</h1>")
    def roll8(self):
        self.text.setText("<h1>" + str(random.randint(1,8)) + "</h1>")
    def roll10(self):
        self.text.setText("<h1>" + str(random.randint(1,10)) + "</h1>")
    def roll12(self):
        self.text.setText("<h1>" + str(random.randint(1,12)) + "</h1>")
    def roll20(self):
        self.text.setText("<h1>" + str(random.randint(1,20)) + "</h1>")
    def roll100(self):
        self.text.setText("<h1>" + str(random.randint(1,100)) + "</h1>")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec())