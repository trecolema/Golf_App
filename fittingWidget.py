# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fittingTool.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from multiprocessing.sharedctypes import Value
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

from sympy import deg


conn = sqlite3.connect('fitting.db')
cur = conn.cursor()
#cur.execute("drop table fittingLog")
cur.execute('create table if not exists fittingLog (userName text, userHeight real, wtFmeasurement real, clubLength text, lieAngle text)')
cur.execute('create unique index if not exists idx_userName on fittingLog (userName)')

class fToolWin(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.heightLabel = QtWidgets.QLabel(Form)
        self.heightLabel.setGeometry(QtCore.QRect(20, 90, 121, 41))
        self.heightLabel.setObjectName("heightLabel")
        self.heightLineEdit = QtWidgets.QLineEdit(Form)
        self.heightLineEdit.setGeometry(QtCore.QRect(190, 100, 171, 31))
        self.heightLineEdit.setObjectName("heightLineEdit")
        self.submitBtn = QtWidgets.QPushButton(Form, clicked = lambda: self.show_tool())
        self.submitBtn.setGeometry(QtCore.QRect(260, 230, 121, 51))
        self.submitBtn.setObjectName("submitBtn")
        self.wtFLineEdit = QtWidgets.QLineEdit(Form)
        self.wtFLineEdit.setGeometry(QtCore.QRect(190, 160, 171, 31))
        self.wtFLineEdit.setObjectName("wtFLineEdit")
        self.wtFmeasurementLabel = QtWidgets.QLabel(Form)
        self.wtFmeasurementLabel.setGeometry(QtCore.QRect(10, 160, 161, 21))
        self.wtFmeasurementLabel.setObjectName("wtFmeasurementLabel")
        self.wtFLabel2 = QtWidgets.QLabel(Form)
        self.wtFLabel2.setGeometry(QtCore.QRect(20, 170, 161, 41))
        self.wtFLabel2.setObjectName("wtFLabel2")
        self.nameLabel = QtWidgets.QLabel(Form)
        self.nameLabel.setGeometry(QtCore.QRect(50, 40, 141, 31))
        self.nameLabel.setObjectName("nameLabel")
        self.nameLineEdit = QtWidgets.QLineEdit(Form)
        self.nameLineEdit.setGeometry(QtCore.QRect(190, 40, 171, 31))
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def show_tool(self):
            userName = self.nameLineEdit.text()
            userHeight = self.heightLineEdit.text()
            userWtF = self.wtFLineEdit.text()

            estLength = ""
            estAngle = ""
            try:
                if float(userHeight) < 58:
                    estLength = "-2 inches"
                elif float(userHeight) >= 58 and float(userHeight) <= 60:
                    estLength = "-1.5 inches"
                elif float(userHeight) >= 60  and float(userHeight) <= 62:
                    estLength = "-1 inch"
                elif float(userHeight) >= 62  and float(userHeight) <= 64:
                    estLength = "-1/2 inch"
                elif float(userHeight) >= 64  and float(userHeight) <= 67:
                    estLength = "-1/4 inch"
                elif float(userHeight) >= 67  and float(userHeight) < 73:
                    estLength = "standard"
                elif float(userHeight) >= 73  and float(userHeight) <= 74:
                    estLength = "+1/4 inch"
                elif float(userHeight) >= 75  and float(userHeight) < 76:
                    estLength = "+1/2 inch"
                elif float(userHeight) >= 76  and float(userHeight) <= 78:
                    estLength = "+1 inch"
                elif float(userHeight) >= 79  and float(userHeight) <= 80:
                    estLength = "+1 1/2 inch"
                elif float(userHeight) >= 80:
                    estLength = "+2 inch"
                else:
                    estLength = "error measurements dont make sense"
            except ValueError:
                estLength = "error measurements dont make sense"

            try:
                if float(userWtF) <= 26:
                    estAngle = "3 deg flat"
                elif float(userWtF) > 26 and float(userWtF) <= 29:
                    estAngle = "2 deg flat"
                elif float(userWtF) > 29 and float(userWtF) <= 33:
                    estAngle = "1 deg flat"
                elif float(userWtF) > 33 and float(userWtF) <= 36:
                    estAngle = "standard"
                elif float(userWtF) > 36 and float(userWtF) <= 39:
                    estAngle = "1 deg upright"
                elif float(userWtF) > 39 and float(userWtF) <= 42:
                    estAngle = "2 deg upright"
                elif float(userWtF) >= 43:
                    estAngle = "3 deg upright"            
                else:
                    estAngle = "error measurements dont make sense" 

                cur.execute("replace into fittingLog values (?,?,?,?,?)", (userName,userHeight,userWtF,estLength, estAngle))
                conn.commit()
                msg = QMessageBox()
                msg.setWindowTitle("fitting")
                msg.setText(f"standard club length is mesured by standard 7 iron (37 inches)\nestimated club length: {estLength} \nestimated lie angle: {estAngle} ")
                x = msg.exec_()

            except ValueError:
                    estAngle = "valueError"


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "fitting tool"))
        self.heightLabel.setText(_translate("Form", "enter height in inches"))
        self.submitBtn.setText(_translate("Form", "sumbit"))
        self.wtFmeasurementLabel.setText(_translate("Form", "enter wrist to floor measurement"))
        self.wtFLabel2.setText(_translate("Form", "typically between 42\" and 25\""))
        self.nameLabel.setText(_translate("Form", "enter name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = fToolWin()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())