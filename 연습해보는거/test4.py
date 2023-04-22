from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets for process input
        self.process_name_edit = QLineEdit()
        self.arrival_time_edit = QLineEdit()
        self.workload_edit = QLineEdit()
        self.add_process_button = QPushButton("Add Process")
        self.add_process_button.clicked.connect(self.add_process)

        # Create table widget for process data
        self.process_table = QTableWidget()
        self.process_table.setColumnCount(3)
        self.process_table.setHorizontalHeaderLabels(["Process Name", "Arrival Time", "Workload"])

        # Create table widget for FCFS results
        self.fcfs_table = QTableWidget()
        self.fcfs_table.setColumnCount(6)
        self.fcfs_table.setHorizontalHeaderLabels(["Process", "AT", "BT", "WT", "TT", "NTT"])

        # Add widgets to layout
        process_input_layout = QHBoxLayout()
        process_input_layout.addWidget(QLabel("Process Name:"))
        process_input_layout.addWidget(self.process_name_edit)
        process_input_layout.addWidget(QLabel("Arrival Time:"))
        process_input_layout.addWidget(self.arrival_time_edit)
        process_input_layout.addWidget(QLabel("Workload:"))
        process_input_layout.addWidget(self.workload_edit)
        process_input_layout.addWidget(self.add_process_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(process_input_layout)
        main_layout.addWidget(self.process_table)
        main_layout.addWidget(self.fcfs_table)

        self.setLayout(main_layout)

    def add_process(self):
        # Get input values from line edits
        process_name = self.process_name_edit.text()
        arrival_time = self.arrival_time_edit.text()
        workload = self.workload_edit.text()

        # Add process data to process table
        row_position = self.process_table.rowCount()
        self.process_table.insertRow(row_position)
        self.process_table.setItem(row_position, 0, QTableWidgetItem(process_name))
        self.process_table.setItem(row_position, 1, QTableWidgetItem(arrival_time))
        self.process_table.setItem(row_position, 2, QTableWidgetItem(workload))

        # Calculate FCFS values
        if row_position == 0:
            wt = 0
            tt = int(workload)
            ntt = 1
        else:
            previous_row = row_position - 1
            previous_tt = int(self.fcfs_table.item(previous_row, 4).text())
            previous_at = int(self.fcfs_table.item(previous_row, 1).text())
            previous_bt = int(self.fcfs_table.item(previous_row, 2).text())
            current_at = int(arrival_time)
            if current_at > previous_tt:
                wt = 0
            else:
                wt = previous_tt - current_at
            tt = wt + int(workload)
            ntt = tt / int(workload)

        # Add calculated values to FCFS table
        self.fcfs_table.insertRow(row_position)
        self.fcfs_table.setItem(row_position, 0, QTableWidgetItem(process_name))
        self.fcfs_table.setItem(row_position, 1, QTableWidgetItem(arrival_time))
        self.fcfs_table.setItem(row_position, 2, QTableWidgetItem(workload))
        self.fcfs_table.setItem(row_position, 3, QTableWidgetItem(str(wt)))
        self.fcfs_table.setItem(row_position, 4, QTableWidgetItem(str(tt)))
        self.fcfs_table.setItem(row_position, 5, QTableWidgetItem(str(ntt)))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()