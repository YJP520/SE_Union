"""
@Project : SE-Union
@Time : 2022/11/12 - 2022/11/18
@Author : YU.J.P
@Version: 1.0
@CopyRight: YU.J.P
"""

########################################################################################################################
import os
import sys
# PYQT5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
# ui文件经转换成py代码之后，导入窗体
from expro_ui import Ui_MainWindow
# 实验 1 - 8 子窗口
from Ex1_ui import Ui_MainWindow_1
from Ex2_ui import Ui_MainWindow_2
from Ex3_ui import Ui_MainWindow_3
from Ex4_ui import Ui_MainWindow_4
from Ex5_ui import Ui_MainWindow_5
from Ex6_ui import Ui_MainWindow_6
from Ex7_ui import Ui_MainWindow_7
from Ex8_ui import Ui_MainWindow_8
# 导入实验 实现类
from Experiments.Ex1 import OrderMatch
from Experiments.Ex2 import WordsIndex
from Experiments.Ex3 import BloomFilter, Remove
from bs4 import BeautifulSoup  # 爬虫
import urllib.request  # 爬虫
import re  # 正则表达式
from Experiments.Ex4 import KShingle, KS_PRO, SimHash
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
class child_EX1_UI(QMainWindow, Ui_MainWindow_1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 监听事件
        self.controller()
        # 按钮事件
        self.buttonInit()

        # 算法实现
        # 文件路径
        self.filePath1 = 'F:/Projects/Python Pycharm/SE_Union/Data/Ex2/实验2.2_单文档查找用例.txt'
        # 既是输出文件路径 又是导入文件路径
        self.outPath1 = 'F:/Projects/Python Pycharm/SE_Union/Data/Ex2/sanguoIndex.txt'

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
        self.pushButton.clicked.connect(self.button_BF)
        self.pushButton_2.clicked.connect(self.button_KMP)
        self.pushButton_3.clicked.connect(self.button_BM)
        self.pushButton_4.clicked.connect(self.button_update)
        self.pushButton_5.clicked.connect(self.button_clear)
        self.pushButton_6.clicked.connect(self.button_selectFile)

    # 选择文件动作按钮店址事件
    def button_selectFile(self):
        # QMessageBox.about(self, 'SelectFile', '点击了提示动作')
        fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        self.filePath1 = fileName[0][0]
        # print(self.filePath1)
        self.lineEdit_2.setText(self.filePath1)

    # BF按钮 动作按钮店址事件
    def button_BF(self):
        # QMessageBox.about(self, 'BF', '点击了提示动作')
        self.textBrowser.clear()

        # 开始搜索
        with open(self.filePath1, 'r', encoding='utf-8') as f:
            S = f.read()
        # 获取模式串
        P = self.lineEdit.text()
        # 异常处理 P
        # print("# 关键字：" + P)
        S_len, P_len = len(S), len(P)

        # start = time.time()  # 开始计时
        position = OrderMatch.BruteForceStringMatchAll(S, P)
        if len(position) == 0:
            QMessageBox.about(self, 'ERROR', '关键词不存在o(╥﹏╥)o')
        else:
            QMessageBox.about(self, 'Tip', '关键词查找成功(*/ω＼*)')
        # loseTime = time.time() - start
        # print("查找用时: ", loseTime)  # 结束计时
        # print("索引位置：", position)

        count = 0
        for index in position:
            while count < index:  # 普通显示
                # print(Ex1.Color.black + S[count], end="")
                self.textBrowser.setTextColor(Qt.blue)
                self.textBrowser.insertPlainText(S[count])
                count += 1
            for i in range(0, P_len):  # 关键高亮显示
                # print(Ex1.Color.green + S[count], end="")
                self.textBrowser.setTextColor(Qt.cyan)
                self.textBrowser.insertPlainText(S[count])
                count += 1
        while count < S_len:  # 普通显示
            # print(Ex1.Color.black + S[count], end="")
            self.textBrowser.setTextColor(Qt.blue)
            self.textBrowser.insertPlainText(S[count])
            count += 1

    # KMP按钮 动作按钮店址事件
    def button_KMP(self):
        # QMessageBox.about(self, 'KMP', '点击了提示动作')
        self.textBrowser.clear()

        # 开始搜索
        with open(self.filePath1, 'r', encoding='utf-8') as f:
            S = f.read()
        # 获取模式串
        P = self.lineEdit.text()
        # 异常处理 P
        # print("# 关键字：" + P)
        S_len, P_len = len(S), len(P)

        # start = time.time()  # 开始计时
        position = OrderMatch.KMP_StringMatchAll(S, P)
        if len(position) == 0:
            QMessageBox.about(self, 'ERROR', '关键词不存在o(╥﹏╥)o')
        else:
            QMessageBox.about(self, 'Tip', '关键词查找成功(*/ω＼*)')
        # loseTime = time.time() - start
        # print("查找用时: ", loseTime)  # 结束计时
        # print("索引位置：", position)

        count = 0
        for index in position:
            while count < index:  # 普通显示
                # print(Ex1.Color.black + S[count], end="")
                self.textBrowser.setTextColor(Qt.blue)
                self.textBrowser.insertPlainText(S[count])
                count += 1
            for i in range(0, P_len):  # 关键高亮显示
                # print(Ex1.Color.green + S[count], end="")
                self.textBrowser.setTextColor(Qt.green)
                self.textBrowser.insertPlainText(S[count])
                count += 1
        while count < S_len:  # 普通显示
            # print(Ex1.Color.black + S[count], end="")
            self.textBrowser.setTextColor(Qt.blue)
            self.textBrowser.insertPlainText(S[count])
            count += 1

    # BM按钮 动作按钮店址事件
    def button_BM(self):
        # QMessageBox.about(self, 'BM', '点击了提示动作')
        self.textBrowser.clear()

        # 开始搜索
        with open(self.filePath1, 'r', encoding='utf-8') as f:
            S = f.read()
        # 获取模式串
        P = self.lineEdit.text()
        # 异常处理 P
        # print("# 关键字：" + P)
        S_len, P_len = len(S), len(P)

        # start = time.time()  # 开始计时
        position = OrderMatch.BoyerMooreStringMatch(S, P)
        if len(position) == 0:
            QMessageBox.about(self, 'ERROR', '关键词不存在o(╥﹏╥)o')
        else:
            QMessageBox.about(self, 'Tip', '关键词查找成功(*/ω＼*)')
        # loseTime = time.time() - start
        # print("查找用时: ", loseTime)  # 结束计时
        # print("索引位置：", position)

        count = 0
        for index in position:
            while count < index:  # 普通显示
                # print(Ex1.Color.black + S[count], end="")
                self.textBrowser.setTextColor(Qt.blue)
                self.textBrowser.insertPlainText(S[count])
                count += 1
            for i in range(0, P_len):  # 关键高亮显示
                # print(Ex1.Color.green + S[count], end="")
                self.textBrowser.setTextColor(Qt.red)
                self.textBrowser.insertPlainText(S[count])
                count += 1
        while count < S_len:  # 普通显示
            # print(Ex1.Color.black + S[count], end="")
            self.textBrowser.setTextColor(Qt.blue)
            self.textBrowser.insertPlainText(S[count])
            count += 1

    # Update按钮 动作按钮店址事件
    def button_update(self):
        # QMessageBox.about(self, 'Update', '点击了提示动作')
        self.textBrowser.clear()

        # 加载文件数据
        if os.path.exists(self.filePath1):
            buffer = open(self.filePath1, 'r', encoding='utf-8')
            for content in buffer:
                self.textBrowser.setTextColor(Qt.blue)
                self.textBrowser.insertPlainText(content)
            buffer.close()

    # Clear按钮 动作按钮店址事件
    def button_clear(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser.clear()


########################################################################################################################


# 子窗口继承类 EX2
class child_EX2_UI(QMainWindow, Ui_MainWindow_2):
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
        self.lineEdit_2.setText(self.filePath1)
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
        self.pushButton_6.clicked.connect(self.button_selectFile)

    # 选择文件动作按钮店址事件
    def button_selectFile(self):
        # QMessageBox.about(self, 'SelectFile', '点击了提示动作')
        fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        self.filePath1 = fileName[0][0]
        self.filePath2 = fileName[0][0]
        # print(self.filePath1)
        self.lineEdit_2.setText(self.filePath2)

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
        # print(P)
        # 异常处理 P
        # print("# 关键字：" + P)
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


# 子窗口继承类
class child_EX3_UI(QMainWindow, Ui_MainWindow_3):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 事件监听
        self.controller()
        # 按钮监听
        self.buttonInit()
        # 查看文件路径
        self.filePath = None
        self.url = 'https://www.keaitupian.cn/weimei/'  # 种子网站
        self.quantity = 1  # 爬取数量
        self.DFS_depth = 3  # DFS爬取深度
        self.imgCount = 0  # DFS照片爬取数
        self.urlCount = 0  # DFS爬取个数
        self.bf = None  # DFS布隆过滤器
        # 加载初始信息
        self.lineEdit.setText(self.url)
        self.lineEdit_3.setText(str(self.quantity))
        self.lineEdit_4.setText(str(self.DFS_depth))

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
        self.pushButton.clicked.connect(self.button_clear)
        self.pushButton_2.clicked.connect(self.button_BFS)
        self.pushButton_3.clicked.connect(self.button_DFS)
        self.pushButton_4.clicked.connect(self.button_lookOver)
        self.pushButton_5.clicked.connect(self.button_selectFile)

    # Clear按钮 动作按钮店址事件
    def button_clear(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser.clear()

    # 选择文件动作按钮店址事件
    def button_selectFile(self):
        # QMessageBox.about(self, 'SelectFile', '点击了提示动作')
        fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        self.filePath = fileName[0][0]
        # print(self.filePath1)
        self.lineEdit_2.setText(self.filePath)

    # LookOver按钮 动作按钮店址事件
    def button_lookOver(self):
        # QMessageBox.about(self, 'LookOver', '点击了按钮点动作')
        self.textBrowser.clear()

        # 加载文件数据
        if os.path.exists(self.filePath):
            buffer = open(self.filePath, 'r', encoding='utf-8')
            for content in buffer:
                self.textBrowser.setTextColor(Qt.blue)
                self.textBrowser.insertPlainText(content)
            buffer.close()

    # BFS按钮 动作按钮店址事件
    def button_BFS(self):
        # QMessageBox.about(self, 'DFS', '点击了提示动作')
        self.url = self.lineEdit.text()
        temp = self.lineEdit_3.text()
        self.quantity = int(temp)

        urlCount = 0  # 已爬网址计数器
        imgCount = 0  # 已爬图片计数器

        # 布隆过滤器
        bf = BloomFilter(self.quantity + 10)
        # 列表作队列 尾部为队首 pop():弹出最后一个,insert(0,''):开始插入一个
        urlQueue = [self.url]  # 先进先出
        # 队列不为空 爬爬爬~
        hadCount = 0
        while urlQueue:
            url = urlQueue.pop()
            # print(Color.blue + '# 正在爬取：' + url)
            self.textBrowser.setTextColor(Qt.blue)
            self.textBrowser.insertPlainText('# 正在爬取：' + url + '\n')
            bf.insert(url)  # 计入过滤器

            # 爬虫程序 - 将网页中的标题、正文、超链接、图片等元素分别提取出来，并能存放到指定的文件中；图片单独存储。
            dic = {}  # 字典
            id = urlCount  # 编号记录
            childList = []  # 子链接
            # 获取网页内容
            try:
                # 无法访问 这一句报错
                page = urllib.request.urlopen(url)
                # 接下来都是正常访问的情况
                urlCount += 1  # 网址编号++
                content = page.read().decode('UTF-8')
                # 获取编号
                dic['id'] = id
                # 获取网址
                dic['url'] = url
                # 获取标题
                dic['title'] = Remove.extract_title(content)

                # 获取图片 存储位置 : Image
                Img = re.compile(r'src="(.+?\.jpg)"')  # 正则表达式匹配图片
                imageList = re.findall(Img, content)  # 结合re正则表达式和BeautifulSoup, 仅返回超链接
                if imageList is not None:
                    newList = []
                    for index in imageList:
                        if index != '' and 'https' in index:
                            newList.append(index)
                    # print(newList)  # 奇怪的方法解决了BUG

                    # print(Color.red + "# Begin Download Image DATA...")
                    self.textBrowser.setTextColor(Qt.red)
                    self.textBrowser.insertPlainText("# Begin Download Image DATA...\n")
                    for imageUrl in newList:
                        # 打开网址，下载图片保存到本地
                        urllib.request.urlretrieve(imageUrl, '{}{}.jpg'.format('Data/Ex3/BFS/Image/', imgCount))
                        imgCount += 1  # 计数器
                    # print(Color.green + "# Download Image DATA Successfully...")
                    self.textBrowser.setTextColor(Qt.green)
                    self.textBrowser.insertPlainText("# Download Image DATA Successfully...\n")

                else:
                    # print(Color.red + "# ERROR ! No Useful URL...")
                    self.textBrowser.setTextColor(Qt.red)
                    self.textBrowser.insertPlainText("# ERROR ! No Useful URL...\n")

                # 获取html正文
                html = Remove.remove_empty_line(Remove.remove_js_css(content))
                html = Remove.remove_any_tag(html)
                html = Remove.remove_empty_line(html)
                dic['html'] = html  # 加入字典
                # print(Color.carmine, dic['html'])
                # 写入文件 'html<num>.txt'
                file_ob = open('Data/Ex3/BFS/Html/' + 'html' + str(id) + '.txt', 'w', encoding='utf-8')
                # file_ob.write(json.dumps(dic, ensure_ascii=False))
                file_ob.write(str(dic))
                file_ob.close()
                # print(Color.green + "# HTML DATA Writing Successfully...")
                self.textBrowser.setTextColor(Qt.green)
                self.textBrowser.insertPlainText("# HTML DATA Writing Successfully...\n")

                # 获取子网页
                soup = BeautifulSoup(content, 'html.parser')
                childLink = soup.find_all('a')
                # 写入文件 按编号写入
                file_ob = open('Data/Ex3/BFS/Child/' + 'childUrl' + str(urlCount) + '.txt', 'w', encoding='utf-8')
                for link in childLink:
                    child = link.get('href')
                    key = link.string
                    if key is not None and child is not None:
                        file_ob.write(key + ':' + child + '\n')
                        childList.append(child)  # 子网址列表
                file_ob.close()
                # print(Color.yellow + "# childLink " + str(urlCount) + " Writing Successfully...")
                self.textBrowser.setTextColor(Qt.yellow)
                self.textBrowser.insertPlainText("# childLink " + str(urlCount) + " Writing Successfully...\n")

            except Exception as e:
                # print(Color.red + '# 无法访问此网址...', e.args)
                self.textBrowser.setTextColor(Qt.red)
                self.textBrowser.insertPlainText('# 无法访问此网址...' + str(e.args) + '\n')
                childList = []  # 无法访问返回空

            # print(Color.carmine + '# 已爬取网站数:', urlCount, ' 图片数:', imgCount)
            self.textBrowser.setTextColor(Qt.darkRed)
            self.textBrowser.insertPlainText('# 已爬取网站数:' + str(urlCount) + ' 图片数:' + str(imgCount) + '\n')
            # 退出循环
            if urlCount >= self.quantity:
                break
            # 筛选网址
            # print(childList)
            newChildList = []
            for index in childList:
                if index != '' and 'https' in index:
                    newChildList.append(index)
            # 子网址加入队列
            if newChildList is not None:
                for index in newChildList:
                    # index 需要查重！！！
                    if bf.is_contain(index) == 0:  # 不包含
                        urlQueue.insert(0, index)
                        hadCount += 1

    # DFS按钮 动作按钮店址事件
    def button_DFS(self):
        # QMessageBox.about(self, 'BFS', '点击了提示动作')
        self.url = self.lineEdit.text()
        temp = self.lineEdit_3.text()
        self.quantity = int(temp)
        temp = self.lineEdit_4.text()
        self.DFS_depth = int(temp)
        self.bf = BloomFilter(self.quantity + 10)  # 布隆过滤器
        self.DFS_Loop(self.url, 0)  # 递归
        self.imgCount = 0  # DFS照片爬取数
        self.urlCount = 0  # DFS爬取个数

    def DFS_Loop(self, url, depth):
        """
        扩展1：利用深度优先方式抓取网页，分析比较广度和深度抓取网页的差异
        :param url: 爬取网址
        :param depth: 爬取深度
        :return: None
        """
        # 返回条件 深度 个数 条件
        if depth >= self.DFS_depth:
            return
        if self.urlCount >= self.quantity:
            return
        # 循环访问
        # print(Color.blue + '# 正在爬取：' + url)
        self.textBrowser.setTextColor(Qt.blue)
        self.textBrowser.insertPlainText('# 正在爬取：' + url + '\n')
        self.bf.insert(url)  # 计入过滤器

        # 爬取单网页
        dic = {}  # 字典
        id = self.urlCount  # 编号记录
        # 获取网页内容
        try:
            # 无法访问 这一句报错
            page = urllib.request.urlopen(url)
            # 接下来都是正常访问的情况
            self.urlCount += 1  # 网址编号++
            content = page.read().decode('UTF-8')
            # 获取编号
            dic['id'] = id
            # 获取网址
            dic['url'] = url
            # 获取标题
            dic['title'] = Remove.extract_title(content)

            # 获取图片 存储位置 : Image
            Img = re.compile(r'src="(.+?\.jpg)"')  # 正则表达式匹配图片
            imageList = re.findall(Img, content)  # 结合re正则表达式和BeautifulSoup, 仅返回超链接
            if imageList is not None:
                newList = []
                for index in imageList:
                    if index != '' and 'https' in index:
                        newList.append(index)
                # print(newList)  # 奇怪的方法解决了BUG

                # print(Color.red + "# Begin Download Image DATA...")
                self.textBrowser.setTextColor(Qt.red)
                self.textBrowser.insertPlainText("# Begin Download Image DATA...\n")
                for imageUrl in newList:
                    # 打开网址，下载图片保存到本地
                    urllib.request.urlretrieve(imageUrl, '{}{}.jpg'.format('Data/Ex3/DFS/Image/', self.imgCount))
                    self.imgCount += 1  # 计数器
                # print(Color.green + "# Download Image DATA Successfully...")
                self.textBrowser.setTextColor(Qt.green)
                self.textBrowser.insertPlainText("# Download Image DATA Successfully...\n")
            else:
                # print(Color.red + "# ERROR ! No Useful URL...")
                self.textBrowser.setTextColor(Qt.red)
                self.textBrowser.insertPlainText("# ERROR ! No Useful URL...\n")

            # 获取html正文
            html = Remove.remove_empty_line(Remove.remove_js_css(content))
            html = Remove.remove_any_tag(html)
            html = Remove.remove_empty_line(html)
            dic['html'] = html  # 加入字典
            # print(Color.carmine, dic['html'])
            # 写入文件 'html<num>.txt'
            file_ob = open('Data/Ex3/DFS/Html/' + 'html' + str(id) + '.txt', 'w', encoding='utf-8')
            # file_ob.write(json.dumps(dic, ensure_ascii=False))
            file_ob.write(str(dic))
            file_ob.close()
            # print(Color.green + "# HTML DATA Writing Successfully...")
            self.textBrowser.setTextColor(Qt.green)
            self.textBrowser.insertPlainText("# HTML DATA Writing Successfully...\n")

            # 获取子网页
            soup = BeautifulSoup(content, 'html.parser')
            childLink = soup.find_all('a')

            # 写入文件 按编号写入
            childList = []
            file_ob = open('Data/Ex3/DFS/Child/' + 'childUrl' + str(self.urlCount) + '.txt', 'w', encoding='utf-8')
            for link in childLink:
                child = link.get('href')
                key = link.string
                if key is not None and child is not None:
                    file_ob.write(key + ':' + child + '\n')
                    childList.append(child)  # 子网址列表
            file_ob.close()
            # print(Color.yellow + "# childLink " + str(self.urlCount) + " Writing Successfully...")
            self.textBrowser.setTextColor(Qt.yellow)
            self.textBrowser.insertPlainText("# childLink " + str(self.urlCount) + " Writing Successfully...\n")

        except Exception as e:
            # print(Color.red + '# 无法访问此网址...', e.args)
            self.textBrowser.setTextColor(Qt.yellow)
            self.textBrowser.insertPlainText('# 无法访问此网址...' + str(e.args) + '\n')
            childList = []  # 无法访问返回空

        # print(Color.carmine + '# 已爬取网站数:', self.urlCount, ' 图片数:', self.imgCount)
        self.textBrowser.setTextColor(Qt.darkRed)
        self.textBrowser.insertPlainText(
            '# 已爬取网站数:' + str(self.urlCount) + ' 图片数:' + str(self.imgCount) + '\n')

        # 筛选网址
        # print(childList)
        newChildList = []
        for index in childList:
            if index != '' and 'https' in index:
                newChildList.append(index)

        if newChildList is not None:
            for index in newChildList:
                # index 需要查重！！！
                if self.bf.is_contain(index) == 0:  # 不包含
                    self.DFS_Loop(index, depth + 1)  # 递归调用


########################################################################################################################


# 子窗口继承类
class child_EX4_UI(QMainWindow, Ui_MainWindow_4):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 事件监听
        self.controller()
        # 按钮监听
        self.buttonInit()
        # 查看文件路径
        self.filePath1 = None
        self.filePath2 = None
        # K-Shingle
        self.k_value = 2
        # 文本
        self.content1 = None
        self.content2 = None

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
        self.pushButton.clicked.connect(self.button_compare)
        self.pushButton_2.clicked.connect(self.button_clear1)
        self.pushButton_3.clicked.connect(self.button_clear2)
        self.pushButton_4.clicked.connect(self.button_calculate_kshingle)
        self.pushButton_5.clicked.connect(self.button_selectFile1)
        self.pushButton_6.clicked.connect(self.button_selectFile2)
        self.pushButton_7.clicked.connect(self.button_calculate_simhash)
        self.pushButton_8.clicked.connect(self.button_input1)
        self.pushButton_9.clicked.connect(self.button_input2)

    # Clear1按钮 动作按钮店址事件
    def button_clear1(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser.clear()

    # Clear2按钮 动作按钮店址事件
    def button_clear2(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser_2.clear()

    # 选择文件1动作按钮店址事件
    def button_selectFile1(self):
        # QMessageBox.about(self, 'SelectFile', '点击了提示动作')
        fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        self.filePath1 = fileName[0][0]
        # print(self.filePath1)
        self.lineEdit.setText(self.filePath1)
        # 加载文件数据
        with open(self.filePath1, 'r', encoding='utf-8') as f:
            self.content1 = f.read()
        f.close()
        self.textBrowser.setTextColor(Qt.black)
        self.textBrowser.insertPlainText(self.content1)

    # 选择文件2动作按钮店址事件
    def button_selectFile2(self):
        # QMessageBox.about(self, 'SelectFile', '点击了提示动作')
        fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        self.filePath2 = fileName[0][0]
        # print(self.filePath1)
        self.lineEdit_2.setText(self.filePath2)
        # 加载文件数据
        with open(self.filePath2, 'r', encoding='utf-8') as f:
            self.content2 = f.read()
        f.close()
        self.textBrowser_2.setTextColor(Qt.black)
        self.textBrowser_2.insertPlainText(self.content2)

    # input1按钮 动作按钮店址事件
    def button_input1(self):
        # QMessageBox.about(self, 'LookOver', '点击了按钮点动作')
        self.textBrowser.clear()
        self.content1 = self.lineEdit.text()
        # 加载文件数据
        self.textBrowser.setTextColor(Qt.black)
        self.textBrowser.insertPlainText(self.content1)

    # input2按钮 动作按钮店址事件
    def button_input2(self):
        # QMessageBox.about(self, 'LookOver', '点击了按钮点动作')
        self.textBrowser_2.clear()
        self.content2 = self.lineEdit_2.text()
        # 加载文件数据
        self.textBrowser_2.setTextColor(Qt.black)
        self.textBrowser_2.insertPlainText(self.content2)

    # calculate kshingle 按钮 动作按钮店址事件
    def button_calculate_kshingle(self):
        # QMessageBox.about(self, 'calculate_kshingle', '点击了按钮点动作')
        temp = self.lineEdit_3.text()
        value = int(temp)
        if value > 0:
            self.k_value = value
        similarity = KShingle.getSimilarity(self.content1, self.content2, self.k_value)
        # 加载相似度
        self.lineEdit_4.setText("%.2f" % similarity)

    # compare 按钮 动作按钮店址事件
    def button_compare(self):
        # QMessageBox.about(self, 'compare', '点击了按钮点动作')
        self.textBrowser.clear()
        self.textBrowser_2.clear()

        list1 = KS_PRO.cutWords(self.content1)
        wordsList1 = []
        for index in list1:
            if index not in "，。《》、？；：‘”【{】}、|=+-——）（*&……%￥#@！ ,<.>/?\'\";:[{]}=+-_)(*&^%$#@!":
                wordsList1.append(index)
        # print(Color.green, wordsList1)

        list2 = KS_PRO.cutWords(self.content2)
        wordsList2 = []
        for index in list2:
            if index not in "，。《》、？；：‘”【{】}、|=+-——）（*&……%￥#@！ ,<.>/?\'\";:[{]}=+-_)(*&^%$#@!":
                wordsList2.append(index)
        # print(Color.carmine, wordsList2)

        commonWords = set(wordsList1) & set(wordsList2)
        # print(Color.blue, commonWords)

        for index in list1:
            if index in commonWords:
                # print(Color.green + index, end='')
                self.textBrowser.setTextColor(Qt.green)
                self.textBrowser.insertPlainText(index)
            else:
                # print(Color.black + index, end='')
                self.textBrowser.setTextColor(Qt.black)
                self.textBrowser.insertPlainText(index)

        # print("\n")
        for index in list2:
            if index in commonWords:
                # print(Color.red + index, end='')
                self.textBrowser_2.setTextColor(Qt.red)
                self.textBrowser_2.insertPlainText(index)
            else:
                # print(Color.black + index, end='')
                self.textBrowser_2.setTextColor(Qt.black)
                self.textBrowser_2.insertPlainText(index)

        # K_value = 2
        # print(Color.red, cls.getSimilarity(content1, content2, K_value))
        similarity = KS_PRO.getSimilarity_list(wordsList1, wordsList2)
        # print(Color.red, '\nsimilarity =', similarity)
        self.lineEdit_4.setText("%.2f" % similarity)

    # calculate simhash 按钮 动作按钮店址事件
    def button_calculate_simhash(self):
        # QMessageBox.about(self, 'calculate_simhash', '点击了按钮点动作')
        similarity = SimHash.getSimHash(self.content1, self.content2)
        # 加载相似度
        self.lineEdit_4.setText("%d" % similarity)


########################################################################################################################


# 子窗口继承类
class child_EX5_UI(QMainWindow, Ui_MainWindow_5):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 事件监听
        self.controller()
        # 按钮监听
        self.buttonInit()
        # 查看文件路径
        self.filePath1 = None
        # 文本
        self.content1 = None

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
        self.pushButton.clicked.connect(self.button_compare)
        self.pushButton_2.clicked.connect(self.button_clear1)
        self.pushButton_3.clicked.connect(self.button_clear2)
        self.pushButton_4.clicked.connect(self.button_calculate_kshingle)
        self.pushButton_5.clicked.connect(self.button_selectFile1)
        self.pushButton_6.clicked.connect(self.button_selectFile2)
        self.pushButton_7.clicked.connect(self.button_calculate_simhash)
        self.pushButton_8.clicked.connect(self.button_input1)
        self.pushButton_9.clicked.connect(self.button_input2)

    # Clear1按钮 动作按钮店址事件
    def button_clear1(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser.clear()

    # Clear2按钮 动作按钮店址事件
    def button_clear2(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser_2.clear()

    # 选择文件1动作按钮店址事件
    def button_selectFile1(self):
        QMessageBox.about(self, 'SelectFile', '点击了提示动作')
        # fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        # self.filePath1 = fileName[0][0]
        # # print(self.filePath1)
        # self.lineEdit.setText(self.filePath1)
        # # 加载文件数据
        # with open(self.filePath1, 'r', encoding='utf-8') as f:
        #     self.content1 = f.read()
        # f.close()
        # self.textBrowser.setTextColor(Qt.black)
        # self.textBrowser.insertPlainText(self.content1)

    # 选择文件2动作按钮店址事件
    def button_selectFile2(self):
        QMessageBox.about(self, 'SelectFile', '点击了提示动作')

    # input1按钮 动作按钮店址事件
    def button_input1(self):
        QMessageBox.about(self, 'LookOver', '点击了按钮点动作')

    # input2按钮 动作按钮店址事件
    def button_input2(self):
        QMessageBox.about(self, 'LookOver', '点击了按钮点动作')

    # calculate kshingle 按钮 动作按钮店址事件
    def button_calculate_kshingle(self):
        QMessageBox.about(self, 'calculate_kshingle', '点击了按钮点动作')

    # compare 按钮 动作按钮店址事件
    def button_compare(self):
        QMessageBox.about(self, 'compare', '点击了按钮点动作')

    # calculate simhash 按钮 动作按钮店址事件
    def button_calculate_simhash(self):
        QMessageBox.about(self, 'calculate_simhash', '点击了按钮点动作')

########################################################################################################################


# 子窗口继承类
class child_EX6_UI(QMainWindow, Ui_MainWindow_6):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 事件监听
        self.controller()
        # 按钮监听
        self.buttonInit()
        # 查看文件路径
        self.filePath1 = None
        # 文本
        self.content1 = None

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
        self.pushButton.clicked.connect(self.button_compare)
        self.pushButton_2.clicked.connect(self.button_clear1)
        self.pushButton_3.clicked.connect(self.button_clear2)
        self.pushButton_4.clicked.connect(self.button_calculate_kshingle)
        self.pushButton_5.clicked.connect(self.button_selectFile1)
        self.pushButton_6.clicked.connect(self.button_selectFile2)
        self.pushButton_7.clicked.connect(self.button_calculate_simhash)
        self.pushButton_8.clicked.connect(self.button_input1)
        self.pushButton_9.clicked.connect(self.button_input2)

    # Clear1按钮 动作按钮店址事件
    def button_clear1(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser.clear()

    # Clear2按钮 动作按钮店址事件
    def button_clear2(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser_2.clear()

    # 选择文件1动作按钮店址事件
    def button_selectFile1(self):
        QMessageBox.about(self, 'SelectFile', '点击了提示动作')
        # fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        # self.filePath1 = fileName[0][0]
        # # print(self.filePath1)
        # self.lineEdit.setText(self.filePath1)
        # # 加载文件数据
        # with open(self.filePath1, 'r', encoding='utf-8') as f:
        #     self.content1 = f.read()
        # f.close()
        # self.textBrowser.setTextColor(Qt.black)
        # self.textBrowser.insertPlainText(self.content1)

    # 选择文件2动作按钮店址事件
    def button_selectFile2(self):
        QMessageBox.about(self, 'SelectFile', '点击了提示动作')

    # input1按钮 动作按钮店址事件
    def button_input1(self):
        QMessageBox.about(self, 'LookOver', '点击了按钮点动作')

    # input2按钮 动作按钮店址事件
    def button_input2(self):
        QMessageBox.about(self, 'LookOver', '点击了按钮点动作')

    # calculate kshingle 按钮 动作按钮店址事件
    def button_calculate_kshingle(self):
        QMessageBox.about(self, 'calculate_kshingle', '点击了按钮点动作')

    # compare 按钮 动作按钮店址事件
    def button_compare(self):
        QMessageBox.about(self, 'compare', '点击了按钮点动作')

    # calculate simhash 按钮 动作按钮店址事件
    def button_calculate_simhash(self):
        QMessageBox.about(self, 'calculate_simhash', '点击了按钮点动作')

########################################################################################################################


# 子窗口继承类
class child_EX7_UI(QMainWindow, Ui_MainWindow_7):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 事件监听
        self.controller()
        # 按钮监听
        self.buttonInit()
        # 查看文件路径
        self.filePath1 = None
        # 文本
        self.content1 = None

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
        self.pushButton.clicked.connect(self.button_compare)
        self.pushButton_2.clicked.connect(self.button_clear1)
        self.pushButton_3.clicked.connect(self.button_clear2)
        self.pushButton_4.clicked.connect(self.button_calculate_kshingle)
        self.pushButton_5.clicked.connect(self.button_selectFile1)
        self.pushButton_6.clicked.connect(self.button_selectFile2)
        self.pushButton_7.clicked.connect(self.button_calculate_simhash)
        self.pushButton_8.clicked.connect(self.button_input1)
        self.pushButton_9.clicked.connect(self.button_input2)

    # Clear1按钮 动作按钮店址事件
    def button_clear1(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser.clear()

    # Clear2按钮 动作按钮店址事件
    def button_clear2(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser_2.clear()

    # 选择文件1动作按钮店址事件
    def button_selectFile1(self):
        QMessageBox.about(self, 'SelectFile', '点击了提示动作')
        # fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        # self.filePath1 = fileName[0][0]
        # # print(self.filePath1)
        # self.lineEdit.setText(self.filePath1)
        # # 加载文件数据
        # with open(self.filePath1, 'r', encoding='utf-8') as f:
        #     self.content1 = f.read()
        # f.close()
        # self.textBrowser.setTextColor(Qt.black)
        # self.textBrowser.insertPlainText(self.content1)

    # 选择文件2动作按钮店址事件
    def button_selectFile2(self):
        QMessageBox.about(self, 'SelectFile', '点击了提示动作')

    # input1按钮 动作按钮店址事件
    def button_input1(self):
        QMessageBox.about(self, 'LookOver', '点击了按钮点动作')

    # input2按钮 动作按钮店址事件
    def button_input2(self):
        QMessageBox.about(self, 'LookOver', '点击了按钮点动作')

    # calculate kshingle 按钮 动作按钮店址事件
    def button_calculate_kshingle(self):
        QMessageBox.about(self, 'calculate_kshingle', '点击了按钮点动作')

    # compare 按钮 动作按钮店址事件
    def button_compare(self):
        QMessageBox.about(self, 'compare', '点击了按钮点动作')

    # calculate simhash 按钮 动作按钮店址事件
    def button_calculate_simhash(self):
        QMessageBox.about(self, 'calculate_simhash', '点击了按钮点动作')

########################################################################################################################


# 子窗口继承类
class child_EX8_UI(QMainWindow, Ui_MainWindow_8):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 事件监听
        self.controller()
        # 按钮监听
        self.buttonInit()
        # 查看文件路径
        self.filePath1 = None
        # 文本
        self.content1 = None

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
        self.pushButton.clicked.connect(self.button_compare)
        self.pushButton_2.clicked.connect(self.button_clear1)
        self.pushButton_3.clicked.connect(self.button_clear2)
        self.pushButton_4.clicked.connect(self.button_calculate_kshingle)
        self.pushButton_5.clicked.connect(self.button_selectFile1)
        self.pushButton_6.clicked.connect(self.button_selectFile2)
        self.pushButton_7.clicked.connect(self.button_calculate_simhash)
        self.pushButton_8.clicked.connect(self.button_input1)
        self.pushButton_9.clicked.connect(self.button_input2)

    # Clear1按钮 动作按钮店址事件
    def button_clear1(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser.clear()

    # Clear2按钮 动作按钮店址事件
    def button_clear2(self):
        # QMessageBox.about(self, 'Clear', '点击了按钮点动作')
        self.textBrowser_2.clear()

    # 选择文件1动作按钮店址事件
    def button_selectFile1(self):
        QMessageBox.about(self, 'SelectFile', '点击了提示动作')
        # fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        # self.filePath1 = fileName[0][0]
        # # print(self.filePath1)
        # self.lineEdit.setText(self.filePath1)
        # # 加载文件数据
        # with open(self.filePath1, 'r', encoding='utf-8') as f:
        #     self.content1 = f.read()
        # f.close()
        # self.textBrowser.setTextColor(Qt.black)
        # self.textBrowser.insertPlainText(self.content1)

    # 选择文件2动作按钮店址事件
    def button_selectFile2(self):
        QMessageBox.about(self, 'SelectFile', '点击了提示动作')

    # input1按钮 动作按钮店址事件
    def button_input1(self):
        QMessageBox.about(self, 'LookOver', '点击了按钮点动作')

    # input2按钮 动作按钮店址事件
    def button_input2(self):
        QMessageBox.about(self, 'LookOver', '点击了按钮点动作')

    # calculate kshingle 按钮 动作按钮店址事件
    def button_calculate_kshingle(self):
        QMessageBox.about(self, 'calculate_kshingle', '点击了按钮点动作')

    # compare 按钮 动作按钮店址事件
    def button_compare(self):
        QMessageBox.about(self, 'compare', '点击了按钮点动作')

    # calculate simhash 按钮 动作按钮店址事件
    def button_calculate_simhash(self):
        QMessageBox.about(self, 'calculate_simhash', '点击了按钮点动作')

########################################################################################################################


# 整合调用
class AppUI:
    def __init__(self):
        # 实例化窗口对象
        self.main_ui = Main_UI()
        # 子实验窗口
        self.child_EX1_ui = child_EX1_UI()
        self.child_EX2_ui = child_EX2_UI()
        self.child_EX3_ui = child_EX3_UI()
        self.child_EX4_ui = child_EX4_UI()
        self.child_EX5_ui = child_EX5_UI()
        self.child_EX6_ui = child_EX6_UI()
        self.child_EX7_ui = child_EX7_UI()
        self.child_EX8_ui = child_EX8_UI()

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
        self.main_ui.pushButton_4.clicked.connect(self.child_EX3_ui.show)
        self.main_ui.actionT1_3.triggered.connect(self.child_EX3_ui.show)
        # EX4
        self.main_ui.pushButton_5.clicked.connect(self.child_EX4_ui.show)
        self.main_ui.actionT1_4.triggered.connect(self.child_EX4_ui.show)
        # EX5
        self.main_ui.pushButton_6.clicked.connect(self.child_EX5_ui.show)
        self.main_ui.actionT1_5.triggered.connect(self.child_EX5_ui.show)
        # EX6
        self.main_ui.pushButton_7.clicked.connect(self.child_EX6_ui.show)
        self.main_ui.actionT1_6.triggered.connect(self.child_EX6_ui.show)
        # EX7
        self.main_ui.pushButton_8.clicked.connect(self.child_EX7_ui.show)
        self.main_ui.actionT1_7.triggered.connect(self.child_EX7_ui.show)
        # EX8
        self.main_ui.pushButton_9.clicked.connect(self.child_EX8_ui.show)
        self.main_ui.actionT1_8.triggered.connect(self.child_EX8_ui.show)


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
