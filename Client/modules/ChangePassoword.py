# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide6 import QtCore, QtGui, QtWidgets


class ChangePassword(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__()

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, -1, 100, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.oldPasswordEdit = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldPasswordEdit.sizePolicy().hasHeightForWidth())
        self.oldPasswordEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.oldPasswordEdit.setFont(font)
        self.oldPasswordEdit.setObjectName("oldPasswordEdit")
        self.horizontalLayout.addWidget(self.oldPasswordEdit)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.newPasswordEdit = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newPasswordEdit.sizePolicy().hasHeightForWidth())
        self.newPasswordEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.newPasswordEdit.setFont(font)
        self.newPasswordEdit.setObjectName("newPasswordEdit")
        self.horizontalLayout_2.addWidget(self.newPasswordEdit)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.confirmNewPasswordEdit = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmNewPasswordEdit.sizePolicy().hasHeightForWidth())
        self.confirmNewPasswordEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.confirmNewPasswordEdit.setFont(font)
        self.confirmNewPasswordEdit.setObjectName("confirmNewPasswordEdit")
        self.horizontalLayout_3.addWidget(self.confirmNewPasswordEdit)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnChange = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChange.sizePolicy().hasHeightForWidth())
        self.btnChange.setSizePolicy(sizePolicy)
        self.btnChange.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnChange.setFont(font)
        self.btnChange.setObjectName("btnChange")
        self.horizontalLayout_4.addWidget(self.btnChange)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 3)
        self.verticalLayout.setStretch(6, 4)
        self.verticalLayout.setStretch(7, 2)
        self.verticalLayout.setStretch(8, 10)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Old Password"))
        self.label_2.setText(_translate("Form", "New Password"))
        self.label_3.setText(_translate("Form", "Confirm New Password"))
        self.btnChange.setText(_translate("Form", "CHANGE"))
