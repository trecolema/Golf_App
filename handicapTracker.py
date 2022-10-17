# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'handicapDisplayTool.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

conn = sqlite3.connect('handicapDatabase.db')
cur = conn.cursor()

class handiTracker(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 640)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 40, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(110, 100, 241, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.loadTracker()

    def loadTracker(self):

        sqlquery = "select * from handicapLog"
        #tableIterator = cur.fetchall()
        tableSize = 0
        tableRow = 0
        for row in cur.execute(sqlquery): # could not find a better one or two line solution to this
            tableSize += 1
        self.tableWidget.setRowCount(tableSize)
        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))

            tableRow += 1

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "handicap tracker"))
        self.label.setText(_translate("Form", "handicap tracker"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "handicap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = handiTracker()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


conn.commit()
