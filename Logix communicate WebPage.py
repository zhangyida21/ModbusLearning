# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\test\PyQt5\PyLogixDemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from pylogix import PLC


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\test\PyQt5\PyLogixDemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\test\PyQt5\PyLogixDemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 90, 161, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 221, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 140, 161, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 130, 221, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 180, 161, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 180, 221, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 230, 161, 31))
        self.label_4.setObjectName("label_4")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 230, 221, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 340, 161, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 449, 161, 31))
        self.label_6.setObjectName("label_6")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 350, 221, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(20, 450, 221, 41))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(20, 400, 221, 41))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(20, 500, 221, 41))
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(420, 490, 161, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 400, 161, 31))
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 330, 741, 231))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 371, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 20, 381, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_9 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_9.setGeometry(QtCore.QRect(150, 30, 221, 21))
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 72, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 60, 121, 16))
        self.label_10.setObjectName("label_10")
        self.textEdit_10 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_10.setGeometry(QtCore.QRect(150, 60, 131, 21))
        self.textEdit_10.setObjectName("textEdit_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 330, 72, 15))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(290, 320, 91, 16))
        self.label_12.setObjectName("label_12")
        self.textEdit_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(270, 350, 131, 31))
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(270, 400, 131, 31))
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_13.setGeometry(QtCore.QRect(270, 450, 131, 31))
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_14.setGeometry(QtCore.QRect(270, 500, 131, 31))
        self.textEdit_14.setObjectName("textEdit_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.textEdit.raise_()
        self.label_2.raise_()
        self.textEdit_2.raise_()
        self.label_3.raise_()
        self.textEdit_3.raise_()
        self.label_4.raise_()
        self.textEdit_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.textEdit_5.raise_()
        self.textEdit_6.raise_()
        self.textEdit_7.raise_()
        self.textEdit_8.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.groupBox_3.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.textEdit_11.raise_()
        self.textEdit_12.raise_()
        self.textEdit_13.raise_()
        self.textEdit_14.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "读取标签"))
        self.label.setText(_translate("MainWindow", "Tag01 Dsplay"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Tag02 Dsplay"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Tag03 Dsplay"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Tag04 Dsplay"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "TagWrite01 Dsplay"))
        self.label_6.setText(_translate("MainWindow", "TagWrite03 Dsplay"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "TagWrite04 Dsplay"))
        self.label_8.setText(_translate("MainWindow", "TagWrite02 Dsplay"))
        self.groupBox.setTitle(_translate("MainWindow", "TagWrite"))
        self.groupBox_2.setTitle(_translate("MainWindow", "TagRead"))
        self.groupBox_3.setTitle(_translate("MainWindow", "设备信息"))
        self.label_9.setText(_translate("MainWindow", "IPAddress"))
        self.label_10.setText(_translate("MainWindow", "ControllerSlot"))
        self.label_11.setText(_translate("MainWindow", "TagName"))
        self.label_12.setText(_translate("MainWindow", "WriteValue"))
        self.textEdit_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "写入标签"))





class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Bind the button click event to the get_plc_info method
        self.pushButton.clicked.connect(self.get_plc_info)
        self.pushButton_2.clicked.connect(self.Write_plc_info)


    def update_label(self, tag_value, label):
        # print(f"Updating label with value: {tag_value.Value} and status: {tag_value.Status}")
        if tag_value.Status == 'Success':
            label.setText(f"Tag Value: {tag_value.Value}")
        else:
            label.setText(f"Failed to read tag ({tag_value}).")


    # def Write_plc_info(self):
    #     WriteTag01 = self.textEdit_5.toPlainText()
    #     WriteTag02 = self.textEdit_7.toPlainText()
    #     WriteTag03 = self.textEdit_6.toPlainText()
    #     WriteTag04 = self.textEdit_8.toPlainText()
    #
    #     WriteTagValue01 = self.textEdit_11.toPlainText()
    #     WriteTagValue02 = self.textEdit_12.toPlainText()
    #     WriteTagValue03 = self.textEdit_13.toPlainText()
    #     WriteTagValue04 = self.textEdit_14.toPlainText()
    #     try:
    #         with PLC() as comm:
    #             comm.IPAddress = self.textEdit_9.toPlainText()
    #             comm.ProcessorSlot = int(self.textEdit_10.toPlainText())  # 确保转换为整数
    #
    #             WriteTag01Value = comm.Write(WriteTag01, int(WriteTagValue01))  # 假设 ReadTag01 是标签的名称
    #             WriteTag02Value = comm.Write(WriteTag02, int(WriteTagValue02))
    #             WriteTag03Value = comm.Write(WriteTag03, int(WriteTagValue03))
    #             WriteTag04Value = comm.Write(WriteTag04, int(WriteTagValue04))
    #
    #             self.update_label(WriteTag01Value, self.label_5)
    #             self.update_label(WriteTag02Value, self.label_8)
    #             self.update_label(WriteTag03Value, self.label_6)
    #             self.update_label(WriteTag04Value, self.label_7)
    #
    #     except Exception as e:
    #         self.label.setText(f"Error: {str(e)}")

    def Write_plc_info(self):
        try:
            # # Collect tag names and values from the UI
            # write_data = [
            #     (self.textEdit_5.toPlainText(), int(self.textEdit_11.toPlainText())),  # Tag 1
            #     (self.textEdit_7.toPlainText(), int(self.textEdit_12.toPlainText())),  # Tag 2
            #     (self.textEdit_6.toPlainText(), int(self.textEdit_13.toPlainText())),  # Tag 3
            #     (self.textEdit_8.toPlainText(), int(self.textEdit_14.toPlainText()))  # Tag 4
            # ]

            # 检查并过滤空数据的 write_data
            # write_data = [
            #     [self.textEdit_5.toPlainText(), int(self.textEdit_11.toPlainText())],  # Tag 1
            #     [self.textEdit_7.toPlainText(), int(self.textEdit_12.toPlainText())],  # Tag 2
            #     [self.textEdit_6.toPlainText(), int(self.textEdit_13.toPlainText())],  # Tag 3
            #     [self.textEdit_8.toPlainText(), int(self.textEdit_14.toPlainText())]  # Tag 4
            # ]

            def safe_int(text):
                try:
                    return int(text)
                except ValueError:
                    return 0  # 或者设定一个默认值

            write_data = [
                [self.textEdit_5.toPlainText(), safe_int(self.textEdit_11.toPlainText())],  # Tag 1
                [self.textEdit_7.toPlainText(), safe_int(self.textEdit_12.toPlainText())],  # Tag 2
                [self.textEdit_6.toPlainText(), safe_int(self.textEdit_13.toPlainText())],  # Tag 3
                [self.textEdit_8.toPlainText(), safe_int(self.textEdit_14.toPlainText())]  # Tag 4
            ]

            # write_data = [data for data in write_data if all(data) and isinstance(data[0], str)]

            write_data = [data for data in write_data if data[0] and isinstance(data[0], str)]

            # Start communication with the PLC
            with PLC() as comm:
                comm.IPAddress = self.textEdit_9.toPlainText()
                # comm.ProcessorSlot = int(self.textEdit_10.toPlainText())

                # Write all data at once
                write_results = comm.Write(write_data)



                # Update the respective labels with the write results
                self.update_label(write_results[0], self.label_5)  # For WriteTag01
                self.update_label(write_results[1], self.label_8)  # For WriteTag02
                self.update_label(write_results[2], self.label_6)  # For WriteTag03
                self.update_label(write_results[3], self.label_7)  # For WriteTag04

        except Exception as e:

            print(self.label.setText(f"Error: {str(e)}"))



    def get_plc_info(self):
        # Get the user input from textEdit (which is assumed to be the tag name)


            try:
                # Collect tag names from the textEdit fields
                tagList = [
                    self.textEdit.toPlainText(),  # ReadTag01
                    self.textEdit_2.toPlainText(),  # ReadTag02
                    self.textEdit_3.toPlainText(),  # ReadTag03
                    self.textEdit_4.toPlainText()  # ReadTag04
                ]

                with PLC() as comm:
                    comm.IPAddress = self.textEdit_9.toPlainText()
                    # comm.ProcessorSlot = int(self.textEdit_10.toPlainText())

                    # Read all tags at once
                    responses = comm.Read(tagList)

                    # Update labels with the corresponding read values
                    self.update_label(responses[0], self.label)
                    self.update_label(responses[1], self.label_2)
                    self.update_label(responses[2], self.label_3)
                    self.update_label(responses[3], self.label_4)

            except Exception as e:
                self.label.setText(f"Error: {str(e)}")

        # ReadTag01 = self.textEdit.toPlainText()
        # ReadTag02 = self.textEdit_2.toPlainText()
        # ReadTag03 = self.textEdit_3.toPlainText()
        # ReadTag04 = self.textEdit_4.toPlainText()
        #
        #
        #
        # try:
        #     with PLC() as comm:
        #         comm.IPAddress = self.textEdit_9.toPlainText()
        #         comm.ProcessorSlot = int(self.textEdit_10.toPlainText())  # 确保转换为整数
        #
        #         # 读取标签值
        #         ReadTag01Value = comm.Read(ReadTag01)
        #         ReadTag02Value = comm.Read(ReadTag02)
        #         ReadTag03Value = comm.Read(ReadTag03)
        #         ReadTag04Value = comm.Read(ReadTag04)
        #
        #         self.update_label(ReadTag01Value, self.label)
        #         self.update_label(ReadTag02Value, self.label_2)
        #         self.update_label(ReadTag03Value, self.label_3)
        #         self.update_label(ReadTag04Value, self.label_4)
        #
        # except Exception as e:
        #     self.label.setText(f"Error: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # 显示窗口
    sys.exit(app.exec_())

# 192.168254.139
