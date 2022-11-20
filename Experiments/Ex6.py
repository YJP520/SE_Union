#
# Crawler Edited by Pycharm.
# Time : 2022/10/21
# Author : YU.J.P
#

"""
    版本: V1.0
    基本功能:
        - TF_IDF

    实验要求:
        根据给定的文档集合，统计单词在文档和文档集中出现的次数，根据TF和IDF来计算词项在文档集中的权重TFIDF；
        利用scikit-learn库来计算TFIDF；
        另外选定一篇文档，利用余弦相似度计算它和已有的20篇文档的相似度，对这20篇文档排序。
        扩展实验1：利用tfidf计算权重，利用simhash算法筛选重复文档。
        扩展实验2：你还可以用其他的相似度计算方法吗？如果有，将结果和余弦相似度的结果进行比较。


"""
import codecs
import os

import chardet
import math
import jieba
import jieba.analyse
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Plug_in.Colors import Color


# -------------------------------------------------------------------------------------------------------------

# 根据给定的文档集合，统计单词在文档和文档集中出现的次数，根据TF和IDF来计算词项在文档集中的权重TFIDF；

class MY_TF_IDF:
    def __init__(self):
        pass

    @classmethod
    def cutWords(cls, content):
        """
        jieba 分词
        :param content:
        :return:
        """
        seg_list = jieba.cut(content)
        words = []
        for seg in seg_list:
            seg = ''.join(seg.split())
            if seg != '，' and seg != '？' and seg != '。' and seg != "\n" and seg != "\n\n":
                words.append(seg)
        return words

    @classmethod
    def proceed(cls, texts):
        """
        对文本预处理，以列表类型存放
        :param texts:
        :return:
        """
        docs = []
        for text in texts:
            doc = cls.cutWords(text)
            docs.append(doc)
        return docs

    @classmethod
    def wordsFrequency(cls, docs):
        """
        此处的docv存放各个文档中单词出现的频率
        :param texts: 文本
        :param docs: 文本分词预处理
        :return:
        """
        docv = []
        for i, doc in enumerate(docs):
            vec = {}
            for word in doc:
                if word not in vec:
                    vec[word] = 1
                else:
                    vec[word] += 1
            docv.append(vec)
        return docv

    @classmethod
    def tf(cls, docs, docv):
        """
        计算 tf
        :param docs:
        :return:
        """
        tf_word = []
        for i, doc in enumerate(docs):
            doc_count = len(doc)
            tf = {}
            for word in doc:
                word_count = docv[i][word]
                word_tf = 1.0 * word_count / doc_count
                tf[word] = word_tf
                tf_word.append(tf)
        return tf_word

    @classmethod
    def wordsIdf(cls, docs):
        """
        单词集合
        :param docs:
        :return:
        """
        words_idf = {}
        for i, doc in enumerate(docs):
            for word in doc:
                if word not in words_idf:
                    words_idf[word] = []
                    words_idf[word].append(i)
                else:
                    words_idf[word].append(i)
        for key in words_idf:
            words_idf[key] = len(set(words_idf[key]))
        return words_idf

    @classmethod
    def idf(cls, words_idf, docs):
        """
        计算 idf 值
        :param words_idf:
        :return:
        """
        idf_word = {}
        docs_count = len(docs)
        for word in words_idf:
            idf_word[word] = math.log(docs_count / (words_idf[word] + 1))
        return idf_word

    @classmethod
    def tf_idf(cls, tf_word, idf_word):
        word_tfidf = {}
        for word_vec in tf_word:
            for word in word_vec:
                word_tfidf[word] = 1.0 * word_vec[word] * idf_word[word]
        return word_tfidf

    @classmethod
    def getTFIDF(cls, texts):
        """
        返回 TF-IDF
        :return: TF-IDF values
        """
        docs = cls.proceed(texts)
        # print(Color.blue, docs)

        docv = cls.wordsFrequency(docs)
        # print(Color.green, docv)

        tf_word = cls.tf(docs, docv)
        # print(Color.red, tf_word)

        words_idf = cls.wordsIdf(docs)
        # print(Color.carmine, words_idf)

        idf_word = cls.idf(words_idf, docs)
        # print(Color.blue, idf_word)

        word_tfidf = cls.tf_idf(tf_word, idf_word)
        # print(Color.red, word_tfidf)

        return word_tfidf


# -------------------------------------------------------------------------------------------------------------

class SL_TFIDF:
    # 利用scikit-learn库来计算TFIDF；
    @classmethod
    def convert(cls, filename, out_enc="UTF-8"):
        """
        可将任意编码形式的文档转换为UTF-8编码
        :param filename: 文件路径
        :param out_enc: 文件编码
        :return: 编码后的结果
        """
        content = codecs.open(filename, 'rb').read()
        source_encoding = chardet.detect(content)['encoding']
        content = content.decode(source_encoding).encode(out_enc)
        codecs.open(filename, 'wb').write(content)

    @classmethod
    def fenci(cls):
        # 保存分词结果的目录
        sFilePath = 'Data/Ex6/Data_T2_Out'
        # 读取文档file 读取文件下的文档名 然后依次打开调用
        basePath = "Data/Ex6/Data_T2"
        folder = os.listdir(basePath)
        # 利用列表corpus存储所有文档的文本
        corpus = []

        for index in folder:
            # print(Color.blue, "----------------------------------------------------------------")
            filePath = basePath + '/' + index
            with open(filePath, 'r', encoding='utf-8') as f1:
                content = f1.read()
                # print(content)
                corpus.append(content)

                # 对文档进行分词处理，采用默认模式
                seg_list = jieba.cut(content, cut_all=True)
                # 对空格，换行符进行处理
                result = []
                for seg in seg_list:
                    seg = ''.join(seg.split())
                    if seg != '' and seg != "\n" and seg != "\n\n":
                        result.append(seg)
                # 将分词后的结果用空格隔开，保存至本地。比如"我来到北京清华大学"，分词结果写入为："我 来到 北京 清华大学"
                f2 = open(sFilePath + "/" + index + "-seg.txt", "w+")
                f2.write(' '.join(result))
                f2.close()
            f1.close()
        # print(corpus)
        return corpus

    @classmethod
    def Tfidf(cls):
        corpus = cls.fenci()
        # 首先利用列表corpus存储所有文档的文本
        vectorizer = CountVectorizer()
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

        word = vectorizer.get_feature_names()
        # print(Color.red, word)

        weight = tfidf.toarray()
        # print(Color.yellow, weight)

        tfidfDict = {}
        for i in range(len(weight)):
            for j in range(len(word)):
                getWord = word[j]
                getValue = weight[i][j]
                if getValue != 0:
                    if tfidfDict.__contains__(getWord):
                        tfidfDict[getWord] += float(getValue)
                    else:
                        tfidfDict.update({getWord: getValue})
        # print(Color.green, tfidfDict)

        sorted_tfidf = sorted(tfidfDict.items(), key=lambda d: d[1], reverse=True)
        return sorted_tfidf
        # fw = open('Data/result1.txt', 'w')
        # for i in sorted_tfidf:
        #     fw.write(i[0] + '\t' + str(i[1]) + '\n')


# -------------------------------------------------------------------------------------------------------------
# 外选定一篇文档，利用余弦相似度计算它和已有的20篇文档的相似度，对这20篇文档排序。

class Cos:
    def __init__(self, content1, content2):
        """
        :param fileName: 文件名
        :param content1: 文本 1
        :param content2: 文本 2
        """
        self.words1 = self.cutWords(content1)  # 单词序列 1
        # print(Color.green, self.words1)

        self.words2 = self.cutWords(content2)  # 单词序列 2
        # print(Color.green, self.words2)

        self.wordsSet = self.getSet()  # 单词并集
        # print(Color.green, self.wordsSet)

        self.V1 = self.getVector(self.words1)  # 向量 1
        # print(Color.blue, self.V1)

        self.V2 = self.getVector(self.words2)  # 向量 2
        # print(Color.blue, self.V2)

        a = []
        a.append(self.V1)
        a.append(self.V2)
        similarity = cosine_similarity(a)
        # print(similarity)

        self.similarity = self.culculate()  # 相似度
        # print(Color.red, 'similarity = ', self.similarity)

    def cutWords(self, content):
        """
        jieba 分词
        :return: 单词序列
        """
        seg_list = jieba.cut(content)
        words = []
        for seg in seg_list:
            seg = ''.join(seg.split())
            if seg != '' \
                    and seg != ' ' \
                    and seg != '，' \
                    and seg != '？' \
                    and seg != '。' \
                    and seg != "\n" \
                    and seg != "\n\n":
                words.append(seg)
        return words

    def getSet(self):
        """
        :return: 单词集合
        """
        return set(self.words1 + self.words2)

    def getVector(self, words):
        """
        计算向量
        :return: 向量
        """
        dic = {}
        # 初始化向量
        for index in self.wordsSet:
            dic[index] = 0
        for index in words:
            if index in dic:
                dic[index] += 1
        print(Color.carmine, dic)
        return list(dic.values())

    def culculate(self):
        # 分子
        molecule = 0.0
        # 左右平方和
        left = 0.0
        right = 0.0
        # 计算
        for i in range(len(self.wordsSet)):
            v1 = self.V1[i]
            v2 = self.V2[i]
            molecule += v1 * v2
            left += v1 * v1
            right += v2 * v2
        # 分母
        denominator = math.sqrt(left) * math.sqrt(right)
        similarity = molecule / denominator
        # 返回相似度
        return similarity

# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
