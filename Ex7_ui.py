# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ex7_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_7(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 550)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(70, 70, 70); /*背景色*/\n"
"}\n"
"")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QCentralwidget{\n"
"    background-color: rgb(70, 70, 70); /*背景色*/\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 130, 81, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 85, 127); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.label.setStyleSheet("font: 25 20pt \"等线 Light\";\n"
"color: rgb(170, 255, 0)")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 130, 81, 31))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 170, 255); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 130, 81, 31))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(170, 170, 255); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 170, 581, 321))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 461, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 461, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 50, 51, 31))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 170, 0); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 90, 51, 31))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 170, 0); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 12pt \"等线\";\n"
"color: rgb(255, 0, 127)")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 10pt \"等线\";\n"
"color: rgb(170, 255, 0)")
        self.label_7.setObjectName("label_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(480, 50, 51, 31))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(170, 170, 255); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(480, 90, 51, 31))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(170, 170, 255); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.textBrowser.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.label_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 27))
        self.menubar.setStyleSheet("*{\n"
"    font-family: dengxian;\n"
"    font-size: 20px;\n"
"    color: rgb(170, 255, 127);\n"
"    background-color: rgb(70, 70, 70); /*背景色*/\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTheme = QtWidgets.QMenu(self.menuView)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/主题_theme.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuTheme.setIcon(icon)
        self.menuTheme.setObjectName("menuTheme")
        self.menuLanguage = QtWidgets.QMenu(self.menuView)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLab = QtWidgets.QMenu(self.menubar)
        self.menuLab.setObjectName("menuLab")
        self.menuEx1 = QtWidgets.QMenu(self.menuLab)
        self.menuEx1.setObjectName("menuEx1")
        self.menuEx2 = QtWidgets.QMenu(self.menuLab)
        self.menuEx2.setObjectName("menuEx2")
        self.menuEx3 = QtWidgets.QMenu(self.menuLab)
        self.menuEx3.setObjectName("menuEx3")
        self.menuEx4 = QtWidgets.QMenu(self.menuLab)
        self.menuEx4.setObjectName("menuEx4")
        self.menuEx6 = QtWidgets.QMenu(self.menuLab)
        self.menuEx6.setObjectName("menuEx6")
        self.menuEx5 = QtWidgets.QMenu(self.menuLab)
        self.menuEx5.setObjectName("menuEx5")
        self.menuEx7 = QtWidgets.QMenu(self.menuLab)
        self.menuEx7.setObjectName("menuEx7")
        self.menuEx8 = QtWidgets.QMenu(self.menuLab)
        self.menuEx8.setObjectName("menuEx8")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setStyleSheet("*{\n"
"    font-family: dengxian;\n"
"    font-size: 20px;\n"
"    color: rgb(170, 255, 127);\n"
"}")
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar_3)
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionSetting = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/设置_setting.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSetting.setIcon(icon1)
        self.actionSetting.setObjectName("actionSetting")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/退出_logout.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.actionTips = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/提示_tips-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTips.setIcon(icon3)
        self.actionTips.setObjectName("actionTips")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionappearance = QtWidgets.QAction(MainWindow)
        self.actionappearance.setObjectName("actionappearance")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/裁切_cutting-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon4)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/复制_copy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon5)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelet = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/删除_delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelet.setIcon(icon6)
        self.actionDelet.setObjectName("actionDelet")
        self.actionundo = QtWidgets.QAction(MainWindow)
        self.actionundo.setObjectName("actionundo")
        self.actionRedo_paste = QtWidgets.QAction(MainWindow)
        self.actionRedo_paste.setObjectName("actionRedo_paste")
        self.actionFind = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/查找_find.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon7)
        self.actionFind.setObjectName("actionFind")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionT1 = QtWidgets.QAction(MainWindow)
        self.actionT1.setObjectName("actionT1")
        self.actionex1 = QtWidgets.QAction(MainWindow)
        self.actionex1.setObjectName("actionex1")
        self.actionT1_2 = QtWidgets.QAction(MainWindow)
        self.actionT1_2.setObjectName("actionT1_2")
        self.actionex1_2 = QtWidgets.QAction(MainWindow)
        self.actionex1_2.setObjectName("actionex1_2")
        self.actionT1_3 = QtWidgets.QAction(MainWindow)
        self.actionT1_3.setObjectName("actionT1_3")
        self.actionex1_3 = QtWidgets.QAction(MainWindow)
        self.actionex1_3.setObjectName("actionex1_3")
        self.actionT1_4 = QtWidgets.QAction(MainWindow)
        self.actionT1_4.setObjectName("actionT1_4")
        self.actionex1_4 = QtWidgets.QAction(MainWindow)
        self.actionex1_4.setObjectName("actionex1_4")
        self.actionT1_5 = QtWidgets.QAction(MainWindow)
        self.actionT1_5.setObjectName("actionT1_5")
        self.actionex1_5 = QtWidgets.QAction(MainWindow)
        self.actionex1_5.setObjectName("actionex1_5")
        self.actionT1_6 = QtWidgets.QAction(MainWindow)
        self.actionT1_6.setObjectName("actionT1_6")
        self.actionex1_6 = QtWidgets.QAction(MainWindow)
        self.actionex1_6.setObjectName("actionex1_6")
        self.actionT1_7 = QtWidgets.QAction(MainWindow)
        self.actionT1_7.setObjectName("actionT1_7")
        self.actionex1_7 = QtWidgets.QAction(MainWindow)
        self.actionex1_7.setObjectName("actionex1_7")
        self.actionT1_8 = QtWidgets.QAction(MainWindow)
        self.actionT1_8.setObjectName("actionT1_8")
        self.actionex1_8 = QtWidgets.QAction(MainWindow)
        self.actionex1_8.setObjectName("actionex1_8")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.actionFresh = QtWidgets.QAction(MainWindow)
        self.actionFresh.setObjectName("actionFresh")
        self.actionRetro = QtWidgets.QAction(MainWindow)
        self.actionRetro.setObjectName("actionRetro")
        self.actionChinese = QtWidgets.QAction(MainWindow)
        self.actionChinese.setObjectName("actionChinese")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.menuFILE.addAction(self.actionSetting)
        self.menuFILE.addSeparator()
        self.menuFILE.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionundo)
        self.menuEdit.addAction(self.actionRedo_paste)
        self.menuEdit.addAction(self.actionDelet)
        self.menuEdit.addSeparator()
        self.menuTheme.addAction(self.actionDark)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionFresh)
        self.menuTheme.addAction(self.actionRetro)
        self.menuLanguage.addAction(self.actionChinese)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuView.addAction(self.actionappearance)
        self.menuView.addAction(self.menuTheme.menuAction())
        self.menuView.addAction(self.menuLanguage.menuAction())
        self.menuHelp.addAction(self.actionTips)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionEdit)
        self.menuHelp.addAction(self.actionAbout_2)
        self.menuEx1.addAction(self.actionT1)
        self.menuEx1.addAction(self.actionex1)
        self.menuEx2.addAction(self.actionT1_2)
        self.menuEx2.addAction(self.actionex1_2)
        self.menuEx3.addAction(self.actionT1_3)
        self.menuEx3.addAction(self.actionex1_3)
        self.menuEx4.addAction(self.actionT1_4)
        self.menuEx4.addAction(self.actionex1_4)
        self.menuEx6.addAction(self.actionT1_6)
        self.menuEx6.addAction(self.actionex1_6)
        self.menuEx5.addAction(self.actionT1_5)
        self.menuEx5.addAction(self.actionex1_5)
        self.menuEx7.addAction(self.actionT1_7)
        self.menuEx7.addAction(self.actionex1_7)
        self.menuEx8.addAction(self.actionT1_8)
        self.menuEx8.addAction(self.actionex1_8)
        self.menuLab.addAction(self.menuEx1.menuAction())
        self.menuLab.addAction(self.menuEx2.menuAction())
        self.menuLab.addAction(self.menuEx3.menuAction())
        self.menuLab.addAction(self.menuEx4.menuAction())
        self.menuLab.addAction(self.menuEx5.menuAction())
        self.menuLab.addAction(self.menuEx6.menuAction())
        self.menuLab.addAction(self.menuEx7.menuAction())
        self.menuLab.addAction(self.menuEx8.menuAction())
        self.menubar.addAction(self.menuLab.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFILE.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar_3.addAction(self.actionFind)
        self.toolBar_3.addAction(self.actionCut)
        self.toolBar_3.addAction(self.actionCopy)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.actionSetting)
        self.toolBar_3.addAction(self.actionTips)
        self.toolBar_3.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "摘要提取"))
        self.label.setText(_translate("MainWindow", "EX7 - 网页重要性"))
        self.pushButton_2.setText(_translate("MainWindow", "清屏1"))
        self.pushButton_4.setText(_translate("MainWindow", "计算"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'等线\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "顶点集数据path"))
        self.lineEdit_2.setText(_translate("MainWindow", "摘要path"))
        self.pushButton_5.setText(_translate("MainWindow", "File1"))
        self.pushButton_6.setText(_translate("MainWindow", "File2"))
        self.label_4.setText(_translate("MainWindow", "TextRank"))
        self.label_7.setText(_translate("MainWindow", "PageRank"))
        self.pushButton_8.setText(_translate("MainWindow", "输入1"))
        self.pushButton_9.setText(_translate("MainWindow", "输入2"))
        self.menuFILE.setTitle(_translate("MainWindow", "Rule"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuLab.setTitle(_translate("MainWindow", "Lab"))
        self.menuEx1.setTitle(_translate("MainWindow", "Ex1"))
        self.menuEx2.setTitle(_translate("MainWindow", "Ex2"))
        self.menuEx3.setTitle(_translate("MainWindow", "Ex3"))
        self.menuEx4.setTitle(_translate("MainWindow", "Ex4"))
        self.menuEx6.setTitle(_translate("MainWindow", "Ex6"))
        self.menuEx5.setTitle(_translate("MainWindow", "Ex5"))
        self.menuEx7.setTitle(_translate("MainWindow", "Ex7"))
        self.menuEx8.setTitle(_translate("MainWindow", "Ex8"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.actionEdit.setText(_translate("MainWindow", "Version"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTips.setText(_translate("MainWindow", "Tips"))
        self.actionAbout.setText(_translate("MainWindow", "donate"))
        self.actionappearance.setText(_translate("MainWindow", "Appearance"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelet.setText(_translate("MainWindow", "Delete"))
        self.actionundo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo_paste.setText(_translate("MainWindow", "Redo"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionT1.setText(_translate("MainWindow", "T1"))
        self.actionex1.setText(_translate("MainWindow", "ex1"))
        self.actionT1_2.setText(_translate("MainWindow", "T1"))
        self.actionex1_2.setText(_translate("MainWindow", "ex1"))
        self.actionT1_3.setText(_translate("MainWindow", "T1"))
        self.actionex1_3.setText(_translate("MainWindow", "ex1"))
        self.actionT1_4.setText(_translate("MainWindow", "T1"))
        self.actionex1_4.setText(_translate("MainWindow", "ex1"))
        self.actionT1_5.setText(_translate("MainWindow", "T1"))
        self.actionex1_5.setText(_translate("MainWindow", "ex1"))
        self.actionT1_6.setText(_translate("MainWindow", "T1"))
        self.actionex1_6.setText(_translate("MainWindow", "ex1"))
        self.actionT1_7.setText(_translate("MainWindow", "T1"))
        self.actionex1_7.setText(_translate("MainWindow", "ex1"))
        self.actionT1_8.setText(_translate("MainWindow", "T1"))
        self.actionex1_8.setText(_translate("MainWindow", "ex1"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionFresh.setText(_translate("MainWindow", "Fresh"))
        self.actionRetro.setText(_translate("MainWindow", "Retro"))
        self.actionChinese.setText(_translate("MainWindow", "Chinese"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
import dark_rc
