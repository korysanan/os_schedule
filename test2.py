from PyQt5 import QtCore, QtGui, QtWidgets
from FCFS_Scheduling import FCFS

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.groupBox_5 = QtWidgets.QGroupBox(self)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 361, 61))

        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(270, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.runSelectedComboBox)

        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setGeometry(QtCore.QRect(100, 10, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Option 1")
        self.comboBox.addItem("FCFS")
        self.comboBox.addItem("Option 3")
        self.comboBox.addItem("Option 4")
        self.comboBox.addItem("Option 5")
        self.comboBox.addItem("Option 6")

    def runSelectedComboBox(self):
        selectedOption = self.comboBox.currentText()
        if selectedOption == "FCFS":
            FCFS()
        # 선택된 comboBox 실행 코드 작성
        print(f"Selected option: {selectedOption}")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec_()