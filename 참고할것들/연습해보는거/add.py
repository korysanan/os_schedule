from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QGroupBox, QGridLayout, QVBoxLayout

class ProcessorInput(QWidget):
    def __init__(self):
        super().__init__()

        # 그룹박스
        self.group_box = QGroupBox("프로세서 정보 입력")

        # 프로세서 이름 입력 라벨 및 라인 에디트
        self.processor_name_label = QLabel("프로세서 이름")
        self.processor_name_edit = QLineEdit()

        # AT 입력 라벨 및 라인 에디트
        self.at_label = QLabel("AT")
        self.at_edit = QLineEdit()

        # Workload 입력 라벨 및 라인 에디트
        self.workload_label = QLabel("Workload")
        self.workload_edit = QLineEdit()

        # 추가 버튼
        self.add_button = QPushButton("추가")
        self.add_button.clicked.connect(self.add_row)

        # 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["프로세서 이름", "AT", "Workload"])

        # 레이아웃 설정
        grid = QGridLayout()
        grid.addWidget(self.processor_name_label, 0, 0)
        grid.addWidget(self.processor_name_edit, 0, 1)
        grid.addWidget(self.at_label, 1, 0)
        grid.addWidget(self.at_edit, 1, 1)
        grid.addWidget(self.workload_label, 2, 0)
        grid.addWidget(self.workload_edit, 2, 1)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addWidget(self.add_button)

        self.group_box.setLayout(vbox)

        vbox_main = QVBoxLayout()
        vbox_main.addWidget(self.group_box)
        vbox_main.addWidget(self.table)

        self.setLayout(vbox_main)

    def add_row(self):
        processor_name = self.processor_name_edit.text()
        at = self.at_edit.text()
        workload = self.workload_edit.text()

        # 테이블 위젯에 행 추가
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # 입력받은 값으로 셀 채우기
        self.table.setItem(row_position, 0, QTableWidgetItem(processor_name))
        self.table.setItem(row_position, 1, QTableWidgetItem(at))
        self.table.setItem(row_position, 2, QTableWidgetItem(workload))

        # 라인 에디트 초기화
        self.processor_name_edit.clear()
        self.at_edit.clear()
        self.workload_edit.clear()

if __name__ == "__main__":
    app = QApplication([])
    processor_input = ProcessorInput()
    processor_input.show()
    app.exec_()