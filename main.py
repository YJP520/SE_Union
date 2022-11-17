#
# Project : Expro_1 UI
# Time : 2022/11/12
# Author : YU.J.P
#

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
# ui文件经转换成py代码之后，导入窗体
from ui.expro_1 import Ui_MainWindow


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 调用监听函数
        self.controller()

    # 监听事件都放在这里面
    def controller(self):
        # 设置监听
        self.actionSetting.triggered.connect(self.setting)
        # 退出监听
        self.actionExit.triggered.connect(self.exit)
        # 提示监听
        self.actionTips.triggered.connect(self.tips)

    # 设置动作按钮点击事件
    def setting(self):
        QMessageBox.about(self, 'Setting', '点击了设置动作')

    # 退出动作按钮店址事件
    def exit(self):
        QMessageBox.about(self, 'Exit', '点击了退出动作')

    # 提示动作按钮店址事件
    def tips(self):
        QMessageBox.about(self, 'Tips', '点击了提示动作')


# MAIN
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 应用图标
    app.setWindowIcon(QIcon('../icon.jpg'))
    # 实例化窗口对象
    mainUI = MainWin()
    # 展示窗口
    mainUI.show()
    # 循环不退出
    sys.exit(app.exec_())
