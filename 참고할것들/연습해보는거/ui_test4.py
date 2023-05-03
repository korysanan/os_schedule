from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QLineEdit, QTableWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create tableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Process", "AT", "BT", "WT", "TT", "NTT"])

        # Create lineEdits
        self.process_edit = QLineEdit(self)
        self.process_edit.setPlaceholderText("Process Name")
        self.process_edit.move(50, 50)

        self.arrival_edit = QLineEdit(self)
        self.arrival_edit.setPlaceholderText("Arrival Time")
        self.arrival_edit.move(50, 75)

        self.workload_edit = QLineEdit(self)
        self.workload_edit.setPlaceholderText("Workload")
        self.workload_edit.move(50, 100)

        # Create Run button
        self.run_button = QPushButton("Run", self)
        self.run_button.move(50, 125)
        self.run_button.clicked.connect(self.run_fcfs)

        # Set central widget
        self.setCentralWidget(self.tableWidget)

    def run_fcfs(self):
        # Get processes from lineEdits
        process_name = str(self.process_edit.text())
        arrival_time = int(self.arrival_edit.text())
        workload = int(self.workload_edit.text())

        process = []
        # Add process to list of processes
        process.append((process_name, arrival_time, workload))

        # Calculate values using FCFS algorithm
        n = len(process)
        wt = [0] * n
        tt = [0] * n
        for i in range(1, n):
            wt[i] = process[i - 1][2] + wt[i - 1]
        for i in range(n):
            tt[i] = process[i][2] + wt[i]
        ntt = [round(tt[i] / process[i][2], 2) for i in range(n)]

        # Add values to tableWidget
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(process[i][0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(process[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(process[i][2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(wt[i])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(tt[i])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(ntt[i])))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()