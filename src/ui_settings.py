# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(561, 383)
        self.verticalLayout = QtWidgets.QVBoxLayout(Settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Settings)
        self.tabWidget.setObjectName("tabWidget")
        self.user_tab = QtWidgets.QWidget()
        self.user_tab.setObjectName("user_tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.user_tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.user_list = UserList(self.user_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_list.sizePolicy().hasHeightForWidth())
        self.user_list.setSizePolicy(sizePolicy)
        self.user_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.user_list.setObjectName("user_list")
        self.verticalLayout_2.addWidget(self.user_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_button = QtWidgets.QPushButton(self.user_tab)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.add_button = QtWidgets.QPushButton(self.user_tab)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.balance_label = QtWidgets.QLabel(self.user_tab)
        self.balance_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.balance_label.setObjectName("balance_label")
        self.gridLayout.addWidget(self.balance_label, 4, 0, 1, 1)
        self.username_label = QtWidgets.QLabel(self.user_tab)
        self.username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 2, 0, 1, 1)
        self.ipv4_byte_label = QtWidgets.QLabel(self.user_tab)
        self.ipv4_byte_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ipv4_byte_label.setObjectName("ipv4_byte_label")
        self.gridLayout.addWidget(self.ipv4_byte_label, 5, 0, 1, 1)
        self.ipv6_byte_label = QtWidgets.QLabel(self.user_tab)
        self.ipv6_byte_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ipv6_byte_label.setObjectName("ipv6_byte_label")
        self.gridLayout.addWidget(self.ipv6_byte_label, 6, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.user_tab)
        self.username.setPlaceholderText("")
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 2, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.user_tab)
        self.name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.password_label = QtWidgets.QLabel(self.user_tab)
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.check_now_button = QtWidgets.QPushButton(self.user_tab)
        self.check_now_button.setEnabled(True)
        self.check_now_button.setObjectName("check_now_button")
        self.horizontalLayout_2.addWidget(self.check_now_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 1, 1, 1)
        self.last_check_label = QtWidgets.QLabel(self.user_tab)
        self.last_check_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.last_check_label.setObjectName("last_check_label")
        self.gridLayout.addWidget(self.last_check_label, 7, 0, 1, 1)
        self.name = QtWidgets.QLabel(self.user_tab)
        self.name.setText("")
        self.name.setScaledContents(False)
        self.name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.id = QtWidgets.QLabel(self.user_tab)
        self.id.setText("")
        self.id.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 1, 1, 1, 1)
        self.id_label = QtWidgets.QLabel(self.user_tab)
        self.id_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.id_label.setObjectName("id_label")
        self.gridLayout.addWidget(self.id_label, 1, 0, 1, 1)
        self.balance = QtWidgets.QLabel(self.user_tab)
        self.balance.setText("")
        self.balance.setObjectName("balance")
        self.gridLayout.addWidget(self.balance, 4, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(self.user_tab)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 3, 1, 1, 1)
        self.ipv4_byte = QtWidgets.QLabel(self.user_tab)
        self.ipv4_byte.setEnabled(True)
        self.ipv4_byte.setText("")
        self.ipv4_byte.setObjectName("ipv4_byte")
        self.gridLayout.addWidget(self.ipv4_byte, 5, 1, 1, 1)
        self.ipv6_byte = QtWidgets.QLabel(self.user_tab)
        self.ipv6_byte.setText("")
        self.ipv6_byte.setObjectName("ipv6_byte")
        self.gridLayout.addWidget(self.ipv6_byte, 6, 1, 1, 1)
        self.last_check = QtWidgets.QLabel(self.user_tab)
        self.last_check.setText("")
        self.last_check.setObjectName("last_check")
        self.gridLayout.addWidget(self.last_check, 7, 1, 1, 1)
        self.md5_check_box = QtWidgets.QCheckBox(self.user_tab)
        self.md5_check_box.setObjectName("md5_check_box")
        self.gridLayout.addWidget(self.md5_check_box, 3, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.user_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        self.add_button.clicked.connect(self.user_list.add_user)
        self.delete_button.clicked.connect(self.user_list.delete_user)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "设置"))
        self.delete_button.setText(_translate("Settings", "删除"))
        self.add_button.setText(_translate("Settings", "添加"))
        self.balance_label.setText(_translate("Settings", "余额:"))
        self.username_label.setText(_translate("Settings", "账号:"))
        self.ipv4_byte_label.setText(_translate("Settings", "ipv4 流量:"))
        self.ipv6_byte_label.setText(_translate("Settings", "ipv6 流量:"))
        self.name_label.setText(_translate("Settings", "姓名:"))
        self.password_label.setText(_translate("Settings", "密码:"))
        self.check_now_button.setText(_translate("Settings", "现在检查"))
        self.last_check_label.setText(_translate("Settings", "上次检查:"))
        self.id_label.setText(_translate("Settings", "学号:"))
        self.md5_check_box.setText(_translate("Settings", "MD5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_tab), _translate("Settings", "用户"))

from user_list import UserList