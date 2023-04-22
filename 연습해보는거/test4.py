from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QTableWidget, QTableWidgetItem
from typing import List, Tuple

class ProcessorInput(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.process_label = QLabel('Process Name:', self)
        self.at_label = QLabel('Arrival Time:', self)
        self.workload_label = QLabel('Workload:', self)

        self.process_input = QLineEdit(self)
        self.at_input = QLineEdit(self)
        self.workload_input = QLineEdit(self)

        input_layout = QGridLayout()
        input_layout.addWidget(self.process_label, 0, 0)
        input_layout.addWidget(self.at_label, 1, 0)
        input_layout.addWidget(self.workload_label, 2, 0)
        input_layout.addWidget(self.process_input, 0, 1)
        input_layout.addWidget(self.at_input, 1, 1)
        input_layout.addWidget(self.workload_input, 2, 1)

        self.setLayout(input_layout)


class FCFS(QWidget):
    def __init__(self):
        super().__init__()

        self.process_input_group = QGroupBox('Process Input', self)
        self.table_group = QGroupBox('Process Schedule', self)

        self.process_input_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()

        self.process_input_layout.addWidget(self.process_input_group)
        self.process_input_layout.addWidget(self.table_group)

        self.process_input_group.setLayout(ProcessorInput(self))
        self.table_group.setLayout(QTableWidget(self))

        self.table_layout.addWidget(self.table_group)

        self.setLayout(self.table_layout)

    def add_row(self):
        table = self.table_group.layout().itemAt(0).widget()
        process = self.process_input_group.layout().itemAt(0).widget().process_input.text()
        at = int(self.process_input_group.layout().itemAt(0).widget().at_input.text())
        workload = int(self.process_input_group.layout().itemAt(0).widget().workload_input.text())

        row = table.rowCount()
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(process))
        table.setItem(row, 1, QTableWidgetItem(str(at)))
        table.setItem(row, 2, QTableWidgetItem(str(workload)))

    def schedule_processes(self):
        table = self.table_group.layout().itemAt(0).widget()

        processes = []
        for i in range(table.rowCount()):
            processes.append({
                'name': table.item(i, 0).text(),
                'at': int(table.item(i, 1).text()),
                'workload': int(table.item(i, 2).text())
            })

        processes.sort(key=lambda x: x['at'])

        current_time = 0
        for i in range(len(processes)):
            process = processes[i]
            bt = process['workload']
            wt = current_time - process['at']
            tt = wt + bt
            ntt = tt / bt

            current_time += bt

            row = table.rowCount()
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(process['name']))
            table.setItem(row, 1, QTableWidgetItem(str(process['at'])))
            table.setItem(row, 2, QTableWidgetItem(str(bt)))
            table.setItem(row, 3, QTableWidgetItem(str(wt)))
            table.setItem(row, 4, QTableWidgetItem(str(tt)))
            table.setItem(row, 5, QTableWidgetItem(str(ntt)))

if __name__ == "__main__":
    app = QApplication([])
    processor_input = ProcessorInput()
    processor_input.show()
    app.exec_()        