#
# Crawler Edited by Pycharm.
# Time : 2022/09/30
# Author : YU.J.P
#

"""
    版本: V1.0

    实验要求:
        给定两个文本串，设置不同的K值，计算它们的k-shingle集合，并进行相似度计算；分析不同的k值对相似度的影响；
        利用K-shingle算法，计算两个给定文档的相似度，查找重复字符串，并将重复字符串高亮显示出来；
        扩展实验：对给定的一个文档，计算它和某路径下的所有文档的相似度，将相似度高于某阈值的文档名称和重复内容显示出来。
        扩展实验：自己编写I-match和simhash方法的代码，并对选定的文档进行相似度计算，对结果进行对比

"""

from Plug_in.Colors import Color
import jieba
import jieba.analyse
import numpy as np


# -------------------------------------------------------------------------------------------------------------
# 给定两个文本串，设置不同的K值，计算它们的k-shingle集合，并进行相似度计算；分析不同的k值对相似度的影响
# 文本查重技术 K-shingle
class KShingle:
    def __init__(self):
        pass

    @classmethod
    def getShingle(cls, content, k):
        """
        K-Shingle 获取字典
        :param content: 文本内容
        :param k: 间隔长度
        :return: dic
        """
        dic = dict()  # 新建字典
        for i in range(0, len(content) - k + 1):
            part = content[i:i + k]  # 拆分词
            if part in dic:  # 重复单词数量 +1
                dic[part] += 1
            else:  # 新单词赋值为 1
                dic[part] = 1
        return dic  # 返回字典

    @classmethod
    def getSimilarity(cls, content1, content2, k):
        """
        获取两段文本content1和content2的相似度
        :param content1: 文本 1
        :param content2: 文本 2
        :param k: 间隔长度
        :return: 相似度百分比
        """
        if content1 == content2:
            return 1
        set1, set2 = set(), set()  # 集合1 & 集合2
        profile1 = cls.getShingle(content1, k)  # 字典 1
        profile2 = cls.getShingle(content2, k)  # 字典 2
        for i in profile1.keys():
            set1.add(i)  # 加入到set中
        for i in profile2.keys():
            set2.add(i)  # 加入到set中
        # print(Color.blue, set1)
        # print(Color.blue, set2)
        return 1.0 * len(set1 & set2) / len(set1 | set2)
        # inter = len(profile1.keys()) + len(profile2.keys()) - len(set1)
        # return 1.0 * inter / len(set1)

    @classmethod
    def test_2(cls):  # Kshingle 测试函数
        print(Color.green, 'Experiment_4', Color.yellow, '---', Color.carmine, 'Ex4_T1')
        print()
        # content1 = '重庆理工大学在重庆市，是一个美丽的大学。'
        # content2 = '重庆市有一个美丽的大学，叫重庆理工大学。'
        content1 = 'uvwxyzab'
        content2 = 'uvwxyzac'
        print(Color.blue, 'content1:', content1)
        print(Color.green, 'content2:', content2)
        for K in range(1, 6):
            similarity = cls.getSimilarity(content1, content2, K) * 100
            print(Color.green + '# K_value = %g' % K, end=Color.yellow + ' <===> ')
            print(Color.red + 'Similarity: %.4g%%' % similarity)


# -------------------------------------------------------------------------------------------------------------
# 给利用K-shingle算法，计算两个给定文档的相似度，查找重复字符串，并将重复字符串高亮显示出来
# 改进文本查重技术 K-shingle
class KS_PRO:
    def __init__(self):
        pass

    @classmethod
    def cutWords(cls, content):
        """
        jieba分词
        :param content: 文本内容
        :return: 分词列表
        """
        return list(jieba.cut(content))

    @classmethod
    def getShingle(cls, content, k):
        """
        K-Shingle 获取字典
        :param content: 文本内容
        :param k: 间隔长度
        :return: dic
        """
        dic = dict()  # 新建字典
        for i in range(0, len(content) - k + 1):
            part = content[i:i + k]  # 拆分词
            if part in dic:  # 重复单词数量 +1
                dic[part] += 1
            else:  # 新单词赋值为 1
                dic[part] = 1
        return dic  # 返回字典

    @classmethod
    def getSimilarity(cls, content1, content2, k):
        """
        获取两段文本content1和content2的相似度
        :param content1: 文本 1
        :param content2: 文本 2
        :param k: 间隔长度
        :return: 相似度百分比
        """
        if content1 == content2:
            return 1
        set1, set2 = set(), set()  # 集合1 & 集合2
        profile1 = cls.getShingle(content1, k)  # 字典 1
        profile2 = cls.getShingle(content2, k)  # 字典 2
        for i in profile1.keys():
            set1.add(i)  # 加入到set中
        for i in profile2.keys():
            set2.add(i)  # 加入到set中
        # print(Color.blue, set1)
        # print(Color.blue, set2)
        return 1.0 * len(set1 & set2) / len(set1 | set2)
        # inter = len(profile1.keys()) + len(profile2.keys()) - len(set1)
        # return 1.0 * inter / len(set1)

    @classmethod
    def getSimilarity_list(cls, list1, list2):
        """
        获取两段文本content1和content2的相似度
        :param list1: 文本 1
        :param list2: 文本 2
        :param k: 间隔长度
        :return: 相似度百分比
        """
        if list1 == list2:
            return 1
        set1, set2 = set(list1), set(list2)  # 集合1 & 集合2
        # print(Color.blue, set1)
        # print(Color.blue, set2)
        return 1.0 * len(set1 & set2) / len(set1 | set2)
        # inter = len(profile1.keys()) + len(profile2.keys()) - len(set1)
        # return 1.0 * inter / len(set1)

    @classmethod
    def test_1(cls):  # Kshingle 测试函数
        filePath1 = 'Data/Ex4_T2_Data/content1.txt'
        content1 = None  # 内容 1
        filePath2 = 'Data/Ex4_T2_Data/content2.txt'
        content2 = None  # 内容 2
        with open(filePath1, 'r', encoding='utf-8') as f1:
            content1 = f1.read()
        f1.close()
        with open(filePath2, 'r', encoding='utf-8') as f2:
            content2 = f2.read()
        f2.close()

        list1 = cls.cutWords(content1)
        wordsList1 = []
        for index in list1:
            if index not in "，。《》、？；：‘”【{】}、|=+-——）（*&……%￥#@！ ,<.>/?\'\";:[{]}=+-_)(*&^%$#@!":
                wordsList1.append(index)
        print(Color.green, wordsList1)

        list2 = cls.cutWords(content2)
        wordsList2 = []
        for index in list2:
            if index not in "，。《》、？；：‘”【{】}、|=+-——）（*&……%￥#@！ ,<.>/?\'\";:[{]}=+-_)(*&^%$#@!":
                wordsList2.append(index)
        print(Color.carmine, wordsList2)

        commonWords = set(wordsList1) & set(wordsList2)
        print(Color.blue, commonWords)

        for index in list1:
            if index in commonWords:
                print(Color.green + index, end='')
            else:
                print(Color.black + index, end='')

        print("\n")
        for index in list2:
            if index in commonWords:
                print(Color.red + index, end='')
            else:
                print(Color.black + index, end='')

        # K_value = 2
        # print(Color.red, cls.getSimilarity(content1, content2, K_value))
        print(Color.red, '\nsimilarity =', cls.getSimilarity_list(wordsList1, wordsList2))


# -------------------------------------------------------------------------------------------------------------
# Simhash算法:
#   simhash算法的核心思想是降维，将文章表示为特征值集合，再降维为一个b位的hash特征向量，
#   通过比较两个simhash之间的海明（ Hamming）距离来衡量相似性
class SimHash(object):
    def __init__(self):
        pass

    @classmethod
    def _simHash(cls, content):
        """
        :param content: 文本内容
        :return: 哈希
        """
        # 1. jieba分词 可以使用TF-IDF方法获取一篇文章权重最高的前topK个词（feature）和权重（weight）
        seg = jieba.cut(content)
        keyWords = jieba.analyse.extract_tags("|".join(seg), topK=10, withWeight=True)
        # print(Color.carmine, keyWords)

        # 3. 加权
        keyList = []  # 所有权值
        print(Color.black, "----------------------------------")
        for feature, weight in keyWords:
            # print(Color.green, 'feature:' + feature,end=' ')
            print(Color.blue, 'weight: %g' % weight)
            weight = int(weight)
            # 2. 计算hash值
            binStr = cls._string_hash(feature)
            # print(Color.green, 'string_hash: ' + binStr)
            weightList = []  # feature 加权
            for c in binStr:
                if c == '1':
                    weightList.append(weight)
                else:
                    weightList.append(-weight)
            keyList.append(weightList)
        # print(Color.carmine, keyList)
        # 4. 合并 权值相加
        listSum = np.sum(np.array(keyList), axis=0)
        # print(Color.blue, listSum)

        # 为空
        if not keyList:
            return '00'
        # 5. 降维
        simHash = ''
        for i in listSum:
            if i > 0:
                simHash = simHash + '1'
            else:
                simHash = simHash + '0'
        # print(Color.yellow, simHash)
        return simHash

    @classmethod
    def _string_hash(cls, source):
        """
        :param source: 关键字
        :return: hash值
        """
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]

            return str(x)

    @classmethod
    def _getDistance(cls, hashStr1, hashStr2):
        """
        计算汉明距离
        :param hashStr1: 哈希值 1
        :param hashStr2: 哈希值 2
        :return: 汉明距离
        """
        length = 0
        for index, char in enumerate(hashStr1):
            if char == hashStr2[index]:
                continue
            else:
                length += 1
        return length

    @classmethod
    def getSimHash(cls, content1, content2):
        """
        :param content1: 文本 1
        :param content2: 文本 2
        :return: 汉明距离
        """
        hashStr1 = cls._simHash(content1)
        hashStr2 = cls._simHash(content2)
        return cls._getDistance(hashStr1, hashStr2)


# -------------------------------------------------------------------------------------------------------------

# 运行
if __name__ == '__main__':
    KShingle.test_2()  # 测试函数
    pass

    # print(Color.green, 'Experiment_4', Color.yellow, '---', Color.carmine, 'Ex4_ex2')
    #
    # # filePath1 = 'Data/Ex4_T2_Data/content1.txt'
    # # content1 = None  # 内容 1
    # # filePath2 = 'Data/Ex4_T2_Data/content2.txt'
    # # content2 = None  # 内容 2
    # # with open(filePath1, 'r', encoding='utf-8') as f1:
    # #     content1 = f1.read()
    # # f1.close()
    # # with open(filePath2, 'r', encoding='utf-8') as f2:
    # #     content2 = f2.read()
    # # f2.close()
    # # distance = SimHash.getSimHash(content1, content2)
    #
    # s1 = '我在重庆的重庆理工大学'
    # s2 = '我在重庆的重庆大学上大学'
    # print(Color.green, s1)
    # print(Color.blue, s2)
    # distance = SimHash.getSimHash(s1, s2)
    #
    # print(Color.black, "----------------------------------")
    # print(Color.red, 'distance = {}'.format(distance))
    #
    # pass
