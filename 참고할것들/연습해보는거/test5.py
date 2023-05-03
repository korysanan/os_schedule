from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QSpinBox, QPushButton, QTableWidget, QTableWidgetItem
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpinBox to TableWidget Example")

        # Create a central widget and set a layout for it
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        # Create a SpinBox and add it to the layout
        self.spin_box = QSpinBox()
        self.layout.addWidget(self.spin_box, 0, 0)

        # Create a button and add it to the layout
        self.button = QPushButton("Square and Add to Table")
        self.button.clicked.connect(self.add_to_table)
        self.layout.addWidget(self.button, 0, 1)

        # Create a TableWidget and add it to the layout
        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Squared Value"])
        self.layout.addWidget(self.table, 1, 0, 1, 2)

    def add_to_table(self):
        value = self.spin_box.value()
        squared_value = value ** 2
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count + 1)
        self.table.setItem(row_count, 0, QTableWidgetItem(str(squared_value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())