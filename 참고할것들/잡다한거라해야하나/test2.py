# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 812)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(510, 400, 741, 201))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(20)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(19, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(34)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(540, 130, 120, 151))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 90, 16))
        self.radioButton.setObjectName("radioButton")
        self.Process1 = QtWidgets.QRadioButton(self.groupBox)
        self.Process1.setGeometry(QtCore.QRect(10, 50, 90, 16))
        self.Process1.setObjectName("Process1")
        self.Process1_2 = QtWidgets.QRadioButton(self.groupBox)
        self.Process1_2.setGeometry(QtCore.QRect(10, 80, 90, 16))
        self.Process1_2.setObjectName("Process1_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 56, 12))
        self.label_8.setObjectName("label_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(690, 130, 120, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 20, 90, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.Process1_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.Process1_3.setGeometry(QtCore.QRect(10, 50, 90, 16))
        self.Process1_3.setObjectName("Process1_3")
        self.Process1_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.Process1_4.setGeometry(QtCore.QRect(10, 80, 90, 16))
        self.Process1_4.setObjectName("Process1_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 56, 12))
        self.label_9.setObjectName("label_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(840, 130, 120, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 20, 90, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.Process1_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.Process1_5.setGeometry(QtCore.QRect(10, 50, 90, 16))
        self.Process1_5.setObjectName("Process1_5")
        self.Process1_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.Process1_6.setGeometry(QtCore.QRect(10, 80, 90, 16))
        self.Process1_6.setObjectName("Process1_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 56, 12))
        self.label_10.setObjectName("label_10")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(990, 130, 120, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 20, 90, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.Process1_7 = QtWidgets.QRadioButton(self.groupBox_4)
        self.Process1_7.setGeometry(QtCore.QRect(10, 50, 90, 16))
        self.Process1_7.setObjectName("Process1_7")
        self.Process1_8 = QtWidgets.QRadioButton(self.groupBox_4)
        self.Process1_8.setGeometry(QtCore.QRect(10, 80, 90, 16))
        self.Process1_8.setObjectName("Process1_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 56, 12))
        self.label_11.setObjectName("label_11")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(540, 20, 571, 71))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setGeometry(QtCore.QRect(100, 10, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox.setGeometry(QtCore.QRect(100, 40, 81, 22))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(370, 10, 81, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(540, 320, 271, 51))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_4.setObjectName("label_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 400, 461, 361))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(76)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 20, 461, 351))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 150, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 311, 351))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(330, 10, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_7)
        self.label_7.setGeometry(QtCore.QRect(330, 130, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(330, 70, 91, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 190, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit.setGeometry(QtCore.QRect(330, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 240, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 290, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(510, 630, 741, 131))
        self.tableWidget_4.setDragEnabled(False)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(20)
        self.tableWidget_4.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(19, item)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_4.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_4.verticalHeader().setStretchLastSection(False)
        self.groupBox_7.raise_()
        self.tableWidget.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.groupBox_6.raise_()
        self.tableWidget_3.raise_()
        self.tableWidget_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "19"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "20"))
        self.groupBox.setTitle(_translate("MainWindow", "Core 0"))
        self.radioButton.setText(_translate("MainWindow", "OFF"))
        self.Process1.setText(_translate("MainWindow", "P - Core"))
        self.Process1_2.setText(_translate("MainWindow", "E - Core"))
        self.label_8.setText(_translate("MainWindow", "0.00W"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Core 1"))
        self.radioButton_2.setText(_translate("MainWindow", "OFF"))
        self.Process1_3.setText(_translate("MainWindow", "P - Core"))
        self.Process1_4.setText(_translate("MainWindow", "E - Core"))
        self.label_9.setText(_translate("MainWindow", "0.00W"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Core 2"))
        self.radioButton_3.setText(_translate("MainWindow", "OFF"))
        self.Process1_5.setText(_translate("MainWindow", "P - Core"))
        self.Process1_6.setText(_translate("MainWindow", "E - Core"))
        self.label_10.setText(_translate("MainWindow", "0.00W"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Core 3"))
        self.radioButton_4.setText(_translate("MainWindow", "OFF"))
        self.Process1_7.setText(_translate("MainWindow", "P - Core"))
        self.Process1_8.setText(_translate("MainWindow", "E - Core"))
        self.label_11.setText(_translate("MainWindow", "0.00W"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Our Own Algorithm"))
        self.comboBox.setItemText(1, _translate("MainWindow", "FCFS"))
        self.comboBox.setItemText(2, _translate("MainWindow", "RR"))
        self.comboBox.setItemText(3, _translate("MainWindow", "SPN"))
        self.comboBox.setItemText(4, _translate("MainWindow", "SRTN"))
        self.comboBox.setItemText(5, _translate("MainWindow", "HRRN"))
        self.label.setText(_translate("MainWindow", "Algorithm :"))
        self.label_2.setText(_translate("MainWindow", "  RR :"))
        self.label_3.setText(_translate("MainWindow", "Time :"))
        self.label_4.setText(_translate("MainWindow", "Total Power Consumption :"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Process"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AT"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "BT"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "WT"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TT"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NTT"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Process"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arrival Time(AT)"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Burst Time (BT)"))
        self.label_5.setText(_translate("MainWindow", "ProcessName"))
        self.label_7.setText(_translate("MainWindow", "Burst Time"))
        self.label_6.setText(_translate("MainWindow", "Arrival Time"))
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Core 0"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Core 1"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Core 2"))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Core 3"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_4.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget_4.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget_4.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget_4.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget_4.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget_4.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget_4.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.tableWidget_4.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.tableWidget_4.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "19"))
        item = self.tableWidget_4.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "20"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
