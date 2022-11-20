#
# Crawler Edited by Pycharm.
# Time : 2022/10/14
# Author : YU.J.P
#

"""
    版本: V1.0
    基本功能:
        - 中文分词

    实验要求:
        利用jieba分词对读入的一篇中文文本进行分词，统计每个单词出现的次数和位置；
            （注：也可以使用其他的分词工具包，如 KAnalyzer， ICTCLAS，Paoding、MMSEG4J等）
        读入一篇给定的中文文本，采用最大匹配法进行中文分词（正向和逆向）
        扩展内容1：对实验一的sanguo.txt进行分词，并计算每个词出现的次数，利用matplotlib包画图展示
        扩展内容2：将最大匹配法结果和jieba等分词工具包的结果进行比较

"""

import jieba
import jieba.analyse
from matplotlib import pyplot as plt

from Plug_in.Colors import Color


# -------------------------------------------------------------------------------------------------------------

# 用jieba分词对读入的一篇中文文本进行分词，统计每个单词出现的次数和位置；
class Statistic:
    def __init__(self):
        pass

    @classmethod
    def JiebaWords(cls, content, topk=10):
        """
        :param content: 文本
        :param topk: 高频词个数
        :return: 词频列表
        """
        # 分隔符
        divideChar = ['，', "。", "、", "！", "？", "的", "在", "了", "于"]
        # 分词列表
        split_words = list(x for x in jieba.cut(content, cut_all=False) if x not in divideChar)
        # 统计词 字典
        dic = {}  # 字典
        for word in split_words:
            dic[word] = dic.get(word, 0) + 1
        # 字典排序
        return sorted(dic.items(), key=lambda x: x[1], reverse=True)[:topk]  # get top 10

    @classmethod
    def BoyerMooreStringMatch(cls, S, P):
        """
        BoyerMooreStringMatch
        :param S: 文本内容
        :param P: 匹配串
        :return: 索引位置
        """
        position = []  # 索引列表
        S_len, P_len = len(S), len(P)
        if P_len == 0:
            return 0
        last = {}
        for index in range(P_len):  # 以P中字符为键索引为值创建字典
            last[P[index]] = index
        # 初始化索引辅助变量，使得P最右侧字符和S索引P_len - 1处对齐
        end, P_end = P_len - 1, P_len - 1
        while end < S_len:
            if S[end] == P[P_end]:
                if P_end == 0:  # 判断是否连续完成了len(P)次成功匹配
                    position.append(end)  # 记录结果
                    end += P_len  # 更新位置 继续比较
                else:  # 继续从右向左比对P和S对齐位置字符相同
                    end -= 1
                    P_end -= 1
            else:  # 坏字符原则 好后缀原则
                index = last.get(S[end], -1)  # 找到返回索引 没找到返回-1
                if index < P_end:  # S[end]不存在P中，即index = -1时，该条件及其操作依然成立
                    end += P_len - (index + 1)
                if index > P_end:
                    end += P_len - P_end
                P_end = P_len - 1  # 重新从右开始对P和S进行匹配
        return position

    @classmethod
    def BMWords(cls, content, wordsDic):
        wordsPos = {}
        for index, v in wordsDic:
            wordsPos[index] = cls.BoyerMooreStringMatch(content, index)
        return wordsPos

    @classmethod
    def testJieba(cls):
        """
        用jieba分词对读入的一篇中文文本进行分词，统计每个单词出现的次数和位置；
        :return: None
        """
        content = None
        file_name = 'Data/实验五 分词jieba.txt'
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()

        print(Color.red, "# 任务一 : jieba分词统计[前20个高频词]")
        wordsDic = cls.JiebaWords(content, 20)  # 统计词频
        wordsPos = cls.BMWords(content, wordsDic)  # 统计索引
        # 打印词频
        print(Color.yellow, '\n# 打印词频:')
        for key, value in wordsDic:
            print(Color.carmine, '[', end='')
            print(Color.blue, key, Color.green, ":", value, end='')
            print(Color.carmine, '],', end='')
        # 打印索引
        print(Color.yellow, '\n# 打印索引:')
        for key, value in wordsPos.items():
            print(Color.red, '[', end='')
            print(Color.blue, key, Color.green, ":", value, end='')
            print(Color.red, '],', end='')


# -------------------------------------------------------------------------------------------------------------
# 读入一篇给定的中文文本，采用最大匹配法进行中文分词（正向和逆向）
class leftMax:
    def __init__(self, dict_path):
        self.dictionary = set()  # 定义字典
        self.maximum = 0  # 最大匹配长度

        with open(dict_path, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line) > self.maximum:
                    self.maximum = len(line)

    def cut(self, content):
        result = []
        length = len(content)
        index = 0
        while length > 0:
            word = None
            for size in range(self.maximum, 0, -1):
                if length - size < 0:
                    continue
                piece = content[index:index + size]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    length -= size
                    index += size
                    break
            if word is None:
                length -= 1
                result.append(content[index])
                index += 1
        return result


def test1():
    print(Color.green, "正匹配：")
    content = '研究生命的起源'
    tokenizer = leftMax('Data/30wdict_utf8.txt')
    print(Color.blue, tokenizer.cut(content))


# -------------------------------------------------------------------------------------------------------------

class rightMax:
    def __init__(self, dict_path):
        self.dictionary = set()  # 定义字典
        self.maximum = 0  # 最大匹配长度

        with open(dict_path, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line) > self.maximum:
                    self.maximum = len(line)

    def cut(self, content):
        result = []
        index = len(content)
        while index > 0:
            word = None
            for size in range(self.maximum, 0, -1):
                if index - size < 0:
                    continue
                piece = content[(index - size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            if word is None:
                index -= 1
                result.append(content[(index - 1):index])
        return result[::-1]  # 由于append为添加至末尾，故需反向打印


def test2():
    print(Color.green, "逆向匹配：")
    content = '研究生命的起源'
    tokenizer = rightMax('Data/30wdict_utf8.txt')
    print(Color.blue, tokenizer.cut(content))


# -------------------------------------------------------------------------------------------------------------

def doubleMax(content, path):
    left = leftMax(path)
    right = rightMax(path)

    leftMatch = left.cut(content)
    rightMatch = right.cut(content)

    # 返回分词数较少者
    if len(leftMatch) != len(rightMatch):
        if len(leftMatch) < len(rightMatch):
            return leftMatch
        else:
            return rightMatch
    else:  # 若分词数量相同，进一步判断
        leftsingle = 0
        rightsingle = 0
        isEqual = True  # 用以标志结果是否相同
        for i in range(len(leftMatch)):
            if leftMatch[i] != rightMatch[i]:
                isEqual = False
            # 统计单字数
            if len(leftMatch[i]) == 1:
                leftsingle += 1
            if len(rightMatch[i]) == 1:
                rightsingle += 1
        if isEqual:
            return leftMatch
        if leftsingle < rightsingle:
            return leftMatch
        else:
            return rightMatch


def test3():
    # content = "北京大学生前来应聘算法工程师岗位"
    content = '研究生命的起源'
    print(doubleMax(content, 'Data/30wdict_utf8.txt'))


# -------------------------------------------------------------------------------------------------------------

class Sanguo:

    @classmethod
    def cutSan(cls, sanTxt):
        cut_san = list(jieba.cut(sanTxt))
        print(cut_san)

        dic = dict()
        excludes = ['大军', '荆州', '将军', '却说', '二人', '不可', '不能', '如此', '商议', '如何', '主公', '军士', '左右',
                    '军马', '引兵', '次日', '大喜', '天下', '东吴', '于是', '今日', '不敢', '魏兵', '陛下', '一人', '都督',
                    '人马', '不知', '汉中', '只见', '众将', '后主', '蜀兵', '上马', '大叫', '太守', '此人', '夫人', '先主',
                    '后人', '背后', '城中', '天子', '一面', '何不', '忽报', '先生', '百姓', '何故', '然后', '先锋', '不如',
                    '赶来']

        for i in cut_san:
            if not i in excludes:
                if i == '孟德' or i == '丞相':
                    i = '曹操'
                elif i == '玄德' or i == '玄德曰':
                    i = '刘备'
                elif i == '孔明' or i == '孔明曰':
                    i = '诸葛亮'
                elif i == '关公':
                    i = '关羽'
                if len(i) > 1:
                    if not dic.get(i):
                        dic[i] = 0
                    dic[i] += 1

        sort_User = sorted(dic.items(), key=lambda t: t[1], reverse=True)
        return sort_User

    # 绘图 直方图
    @classmethod
    def showResult(cls, content,  topN):
        data = cls.cutSan(content)
        # print(data[:topN])

        X = range(topN)
        y = list()
        labels = list()
        for i in data[:topN]:
            labels.append(i[0])
            y.append(i[1])
        # print(y)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 引入加载字体名
        plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
        plt.bar(X, y)
        plt.xticks(X, labels)
        plt.title('三国人数统计')
        plt.xlabel('英雄人物')
        plt.ylabel('次数')
        plt.show()

# -------------------------------------------------------------------------------------------------------------


# MAIN
if __name__ == '__main__':
    Statistic.testJieba()
    pass
