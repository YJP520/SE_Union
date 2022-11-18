#
# Project : Expro_1 UI
# Time : 2022/11/12
# Author : YU.J.P
#

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
# ui文件经转换成py代码之后，导入窗体
from expro_1 import Ui_MainWindow
# 子窗口
from create_1 import Ui_MainWindow_2


# 主窗口继承类
class Main_UI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 调用监听函数
        self.controller()
        # 按钮设置
        self.buttonInit()

    # 监听事件都放在这里面
    def controller(self):
        # 设置监听
        self.actionSetting.triggered.connect(self.setting)
        # 退出监听
        self.actionExit.triggered.connect(self.exit)
        # 查找监听
        self.actionFind.triggered.connect(self.find)
        # 提示监听
        self.actionTips.triggered.connect(self.tips)

    # 按钮事件都放在这里面
    def buttonInit(self):
        self.pushButton_2.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.button)
        self.pushButton_4.clicked.connect(self.button)
        self.pushButton_5.clicked.connect(self.button)
        self.pushButton_6.clicked.connect(self.button)
        self.pushButton_7.clicked.connect(self.button)
        self.pushButton_8.clicked.connect(self.button)
        self.pushButton_9.clicked.connect(self.button)

    # 设置动作按钮点击事件
    def setting(self):
        QMessageBox.about(self, 'Setting', '点击了设置动作')

    # 查询动作按钮点击事件
    def find(self):
        QMessageBox.about(self, 'find', '点击了查找动作')

    # 退出动作按钮店址事件
    def exit(self):
        QMessageBox.about(self, 'Exit', '确定退出程序？')
        # 退出程序
        self.actionExit()

    # 提示动作按钮店址事件
    def tips(self):
        QMessageBox.about(self, 'Tips', '点击了提示动作')

    # 按钮点击动作按钮店址事件
    def button(self):
        QMessageBox.about(self, 'Button', '点击了按钮点动作')


# 子窗口继承类
class child_UI1(QMainWindow, Ui_MainWindow_2):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


# 整合调用
class AppUI:
    def __init__(self):
        # 实例化窗口对象
        self.main_ui = Main_UI()
        self.child_ui = child_UI1()
        # 初始化调用
        self.init()

    def init(self):
        # 显示子窗口
        self.main_ui.pushButton.clicked.connect(self.child_ui.show)
        self.main_ui.actionT1.triggered.connect(self.child_ui.show)
        self.main_ui.actionex1.triggered.connect(self.child_ui.show)

        self.main_ui.actionT1_2.triggered.connect(self.child_ui.show)
        self.main_ui.actionex1_2.triggered.connect(self.child_ui.show)

        self.main_ui.actionT1_3.triggered.connect(self.child_ui.show)
        self.main_ui.actionex1_3.triggered.connect(self.child_ui.show)

        self.main_ui.actionT1_4.triggered.connect(self.child_ui.show)
        self.main_ui.actionex1_4.triggered.connect(self.child_ui.show)

        self.main_ui.actionT1_5.triggered.connect(self.child_ui.show)
        self.main_ui.actionex1_5.triggered.connect(self.child_ui.show)

        self.main_ui.actionT1_6.triggered.connect(self.child_ui.show)
        self.main_ui.actionex1_6.triggered.connect(self.child_ui.show)

        self.main_ui.actionT1_7.triggered.connect(self.child_ui.show)
        self.main_ui.actionex1_7.triggered.connect(self.child_ui.show)

        self.main_ui.actionT1_8.triggered.connect(self.child_ui.show)
        self.main_ui.actionex1_8.triggered.connect(self.child_ui.show)


# MAIN
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 应用图标
    app.setWindowIcon(QIcon('icon/icon.jpg'))
    app.setApplicationDisplayName('搜素引擎实验整合 - SE Union')
    app_ui = AppUI()
    app_ui.main_ui.show()
    # 循环不退出
    sys.exit(app.exec_())

