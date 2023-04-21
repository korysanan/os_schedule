import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LineEdit to TableWidget')
        self.setGeometry(200, 200, 500, 500)

        # QLineEdit 생성
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText('Type something here')

        # QPushButton 생성
        self.button = QPushButton('Add to Table', self)
        self.button.clicked.connect(self.add_to_table)

        # QTableWidget 생성
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(['Data'])

        # QVBoxLayout, QHBoxLayout 생성
        v_box = QVBoxLayout()
        h_box = QHBoxLayout()
        h_box.addWidget(self.lineEdit)
        h_box.addWidget(self.button)
        v_box.addLayout(h_box)
        v_box.addWidget(self.table)

        # QWidget 생성
        widget = QWidget()
        widget.setLayout(v_box)
        self.setCentralWidget(widget)

    def add_to_table(self):
        # QLineEdit에서 텍스트 가져오기
        text = self.lineEdit.text()

        # QTableWidget에 행 추가
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

        # QTableWidgetItem으로 데이터 추가
        item = QTableWidgetItem(text)
        self.table.setItem(row_count, 0, item)

        # QLineEdit 초기화
        self.lineEdit.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())