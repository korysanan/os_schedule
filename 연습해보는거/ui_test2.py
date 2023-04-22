from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Button Example')
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(50, 50, 200, 30)
        
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(50, 90, 200, 30)
        
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(50, 130, 200, 30)
        
        self.button = QPushButton('Press Me', self)
        self.button.setGeometry(50, 170, 200, 30)
        self.button.clicked.connect(self.on_button_click)
        
        self.show()
        
    def on_button_click(self):
        if not all([self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()]):
            QMessageBox.warning(self, 'Warning', 'Please enter values in all three fields.')
            return
        
        # Your code goes here
        print('All line edits have values')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())