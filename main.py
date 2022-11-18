#
# Project : SE-Union
# Time : 2022/11/12 - 2022/11/18
# Author : YU.J.P
#

########################################################################################################################
import os
import sys
import time
# PYQT5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
# ui文件经转换成py代码之后，导入窗体
from expro_ui import Ui_MainWindow
# 实验 1 - 8 子窗口
from Ex1_ui import Ui_MainWindow_1
from Ex2_ui import Ui_MainWindow_2
# from Ex3_ui import Ui_MainWindow_3
# from Ex4_ui import Ui_MainWindow_4
# from Ex5_ui import Ui_MainWindow_5
# from Ex6_ui import Ui_MainWindow_6
# from Ex7_ui import Ui_MainWindow_7
# from Ex8_ui import Ui_MainWindow_8

# 导入实验2 T1 实现类
from Experiments.Ex2.Ex2_T1 import IndexSearch, WordsIndex
# 插件类
from Plug_in.Colors import Color

########################################################################################################################


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

    # 按钮事件都放在这里面
    def buttonInit(self):
        # self.pushButton.clicked.connect(self.button_push)
        # self.pushButton_2.clicked.connect(self.button)
        # self.pushButton_3.clicked.connect(self.button)
        # self.pushButton_4.clicked.connect(self.button)
        # self.pushButton_5.clicked.connect(self.button)
        # self.pushButton_6.clicked.connect(self.button)
        # self.pushButton_7.clicked.connect(self.button)
        # self.pushButton_8.clicked.connect(self.button)
        # self.pushButton_9.clicked.connect(self.button)
        pass

    # 按钮点击动作按钮店址事件
    def button_push(self):
        QMessageBox.about(self, 'Push', '查找实验并开始...')

    # 按钮点击动作按钮店址事件
    def button(self):
        QMessageBox.about(self, 'Button', '点击了按钮点动作')

########################################################################################################################


# 子窗口继承类
class child_EX1__UI(QMainWindow, Ui_MainWindow_1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

########################################################################################################################


# 子窗口继承类 EX2_T1
class child_EX2__UI(QMainWindow, Ui_MainWindow_2):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 调用监听函数
        self.controller()
        # 按钮设置
        self.buttonInit()

        # 算法实现
        # 文件路径
        self.filePath1 = 'F:/Projects/Python Pycharm/SE_Union/Data/Ex2/实验2.2_单文档查找用例.txt'
        # 既是输出文件路径 又是导入文件路径
        self.outPath1 = 'F:/Projects/Python Pycharm/SE_Union/Data/Ex2/sanguoIndex.txt'
        self.indexDic = None
        self.index_Ob = None

        # 索引查找
        self.index_Ob = None
        self.filePath2 = 'F:/Projects/Python Pycharm/SE_Union/Data/Ex2/实验2.2_单文档查找用例.txt'
        # self.filePath = 'Data/Romeo And Juliet.txt'
        # self.filePath = 'Data/sanguo.txt'
        self.outPath2 = 'F:/Projects/Python Pycharm/SE_Union/Data/Ex2/wordsIndex.txt'  # 既是输出文件路径 又是导入文件路径

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

    # 按钮事件都放在这里面
    def buttonInit(self):
        self.pushButton.clicked.connect(self.button_build)
        self.pushButton_2.clicked.connect(self.button_clear)
        self.pushButton_3.clicked.connect(self.button_build2)
        self.pushButton_4.clicked.connect(self.button_find)

    # Build按钮 动作按钮店址事件
    def button_build(self):
        self.index_Ob = WordsIndex(self.filePath1)  # 建立对象
        self.indexDic = self.index_Ob.indexDic  # 直接获取索引字典
        self.index_Ob.outputInFile(self.outPath1)  # 写入文件
        # QMessageBox.about(self, 'Build', '点击了按钮点动作')
        self.textBrowser.clear()
        # 获取索引列表 并打印
        keyList, valueList = list(self.indexDic.keys()), list(self.indexDic.values())
        for i in range(0, len(keyList)):
            self.textBrowser.append("<font color='green'>" + str(keyList[i]) + ": " +
                                    "<font color='red'>" + str(valueList[i]))  # 左对齐
            # self.textBrowser.append('\n')

    # Clear按钮 动作按钮店址事件
    def button_clear(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser.clear()

    # 按钮点击动作按钮店址事件
    def button_build2(self):
        # QMessageBox.about(self, 'Build2', '点击了按钮点动作')
        self.index_Ob = WordsIndex(self.filePath2)  # 建立对象
        self.index_Ob.outputInFile(self.outPath2)  # 写入文件

        self.textBrowser.clear()
        if os.path.exists(self.filePath2):
            buffer = open(self.filePath2, 'r', encoding='utf-8')
            for content in buffer:
                self.textBrowser.setTextColor(Qt.blue)
                self.textBrowser.insertPlainText(content)
            buffer.close()

    # 按钮点击动作按钮店址事件
    def button_find(self):
        # QMessageBox.about(self, 'Find', '点击了按钮点动作')
        self.textBrowser.clear()
        # print('# 删除原始数据...')

        # 开始搜索
        with open(self.filePath2, 'r', encoding='utf-8') as f:
            S = f.read()

        # 获取模式串
        P = self.lineEdit.text()
        print(P)
        # 异常处理 P
        print("# 关键字：" + P)
        S_len, P_len = len(S), len(P)

        # start = time.time()  # 开始计时
        indexDic = WordsIndex.inputFromFile(self.outPath2)  # 导入文件 获取索引字典
        position = WordsIndex.getPosition(P, indexDic)
        # loseTime = time.time() - start
        # print("查找用时: ", loseTime)  # 结束计时
        # print("索引位置：", position)

        if len(position) == 0:
            QMessageBox.about(self, 'ERROR', '关键词不存在o(╥﹏╥)o')
        else:
            QMessageBox.about(self, 'Tip', '关键词查找成功(*/ω＼*)')

        count = 0
        for index in position:
            while count < index:  # 普通显示
                # print(Color.black + S[count], end="")
                self.textBrowser.setTextColor(Qt.blue)
                self.textBrowser.insertPlainText(S[count])
                count += 1  # 加空格
            for i in range(0, P_len):  # 关键高亮显示
                # print(Color.green + S[count], end="")
                self.textBrowser.setTextColor(Qt.red)
                self.textBrowser.insertPlainText(S[count])
                count += 1  # 加空格
        while count < S_len:  # 普通显示
            self.textBrowser.setTextColor(Qt.blue)
            # print(Color.black + S[count], end="")
            self.textBrowser.insertPlainText(S[count])
            count += 1  # 加空格

    # 按钮点击动作按钮店址事件
    def button(self):
        QMessageBox.about(self, 'Button', '点击了按钮点动作')

########################################################################################################################


# # 子窗口继承类
# class child_EX3__UI(QMainWindow, Ui_MainWindow_3):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

########################################################################################################################


# # 子窗口继承类
# class child_EX4__UI(QMainWindow, Ui_MainWindow_4):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

########################################################################################################################


# # 子窗口继承类
# class child_EX5__UI(QMainWindow, Ui_MainWindow_5):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

########################################################################################################################


# # 子窗口继承类
# class child_EX6__UI(QMainWindow, Ui_MainWindow_6):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

########################################################################################################################


# # 子窗口继承类
# class child_EX7__UI(QMainWindow, Ui_MainWindow_7):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

########################################################################################################################


# # 子窗口继承类
# class child_EX8__UI(QMainWindow, Ui_MainWindow_8):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

########################################################################################################################


# 整合调用
class AppUI:
    def __init__(self):
        # 实例化窗口对象
        self.main_ui = Main_UI()
        # 子实验窗口
        self.child_EX1_ui = child_EX1__UI()
        self.child_EX2_ui = child_EX2__UI()
        # self.child_EX3_ui = child_EX3__UI()
        # self.child_EX4_ui = child_EX4__UI()
        # self.child_EX5_ui = child_EX5__UI()
        # self.child_EX6_ui = child_EX6__UI()
        # self.child_EX7_ui = child_EX7__UI()
        # self.child_EX8_ui = child_EX8__UI()

        # 初始化调用
        self.init()

    def init(self):
        # 显示子窗口
        # Push Button
        self.main_ui.pushButton.clicked.connect(self.main_ui.button_push)
        # EX1
        self.main_ui.pushButton_2.clicked.connect(self.child_EX1_ui.show)
        self.main_ui.actionT1.triggered.connect(self.child_EX1_ui.show)
        # EX2
        self.main_ui.pushButton_3.clicked.connect(self.child_EX2_ui.show)
        self.main_ui.actionT1_2.triggered.connect(self.child_EX2_ui.show)
        # EX3
        # self.main_ui.pushButton_4.clicked.connect(self.child_EX3_ui.show)
        # self.main_ui.actionT1_3.triggered.connect(self.child_EX3_ui.show)
        # EX4
        # self.main_ui.pushButton_5.clicked.connect(self.child_EX4_ui.show)
        # self.main_ui.actionT1_4.triggered.connect(self.child_EX4_ui.show)
        # EX5
        # self.main_ui.pushButton_6.clicked.connect(self.child_EX5_ui.show)
        # self.main_ui.actionT1_5.triggered.connect(self.child_EX5_ui.show)
        # EX6
        # self.main_ui.pushButton_7.clicked.connect(self.child_EX6_ui.show)
        # self.main_ui.actionT1_6.triggered.connect(self.child_EX6_ui.show)
        # EX7
        # self.main_ui.pushButton_8.clicked.connect(self.child_EX7_ui.show)
        # self.main_ui.actionT1_7.triggered.connect(self.child_EX7_ui.show)
        # EX8
        # self.main_ui.pushButton_9.clicked.connect(self.child_EX8_ui.show)
        # self.main_ui.actionT1_8.triggered.connect(self.child_EX8_ui.show)

########################################################################################################################


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

