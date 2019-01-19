# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FBLA\Notery\Admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from addBookDialog import addBookDialog
from removeBookDialog import dropBookDialog
from BookStorage import BookStorageViewer
from UserManage import UserManage

class Ui_Admin(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName("self")
        self.resize(950, 580)
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.centralWidget)
        self.storageView = BookStorageViewer()
        self.verticalLayout.addWidget(self.storageView)
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setIconSize(QtCore.QSize(60, 60))
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_add_book = QtWidgets.QAction(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rsc/rsc/E-books-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_book.setIcon(icon)
        self.action_add_book.setObjectName("action_add_book")
        self.action_manage_students = QtWidgets.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/rsc/rsc/manage_students_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_manage_students.setIcon(icon1)
        self.action_manage_students.setObjectName("action_manage_students")
        self.action_report = QtWidgets.QAction(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/rsc/rsc/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_report.setIcon(icon2)
        self.action_report.setObjectName("action_report")
        self.action_delete = QtWidgets.QAction(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/rsc/rsc/trash_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_delete.setIcon(icon3)
        self.action_delete.setObjectName("action_delete")
        self.action_star = QtWidgets.QAction(self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/rsc/rsc/star_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_star.setIcon(icon4)
        self.action_star.setObjectName("action_star")
        self.action_settings = QtWidgets.QAction(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/rsc/rsc/settings_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_settings.setIcon(icon5)
        self.action_settings.setObjectName("action_settings")
        self.action_add_record = QtWidgets.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/rsc/rsc/add_record_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_record.setIcon(icon6)
        self.action_add_record.setObjectName("action_add_record")
        self.action_edit_record = QtWidgets.QAction(self)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/rsc/rsc/E-books-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_record.setIcon(icon7)
        self.action_edit_record.setObjectName("action_edit_record")
        self.toolBar.addAction(self.action_add_book)
        self.toolBar.addAction(self.action_edit_record)
        self.toolBar.addAction(self.action_star)
        self.toolBar.addAction(self.action_manage_students)
        self.toolBar.addAction(self.action_report)
        self.toolBar.addAction(self.action_settings)
        self.toolBar.addAction(self.action_delete)
        #self.toolBar.actionTriggered[self.action_add_book].connect(self.AddBookButtonClicked)


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def addBookButtonClicked(self):
        addDialog = addBookDialog(self)
        addDialog.add_book_success_signal.connect(self.storageView.searchButtonClicked)
        addDialog.show()
        addDialog.exec_()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Notery"))
        self.toolBar.setWindowTitle(_translate("self", "toolBar"))
        self.action_add_book.setText(_translate("self", "Add Book"))
        self.action_manage_students.setText(_translate("self", "Manage Students"))
        self.action_report.setText(_translate("self", "Report"))
        self.action_delete.setText(_translate("self", "Delete"))
        self.action_star.setText(_translate("self", "Star"))
        self.action_settings.setText(_translate("self", "Settings"))
        self.action_add_record.setText(_translate("self", "Add Record"))
        self.action_edit_record.setText(_translate("self", "Edit Record"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./rsc/ereader.png"))
    mainWindow = Ui_Admin()
    mainWindow.show()
    sys.exit(app.exec_())

