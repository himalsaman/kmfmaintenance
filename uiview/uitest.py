from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from Control.maintenanceLogic import getAllCustomerNotHaveMaintenance

my_array = [getAllCustomerNotHaveMaintenance()]

def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        tablemodel = MyTableModel(my_array, self)
        tableview = QTableView()
        tableview.setModel(tablemodel)

        layout = QVBoxLayout(self)
        layout.addWidget(tableview)
        self.setLayout(layout)

class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata[0])

    def columnCount(self, parent):
        return len(self.arraydata)

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.column()][index.row()])

if __name__ == "__main__":
    main()