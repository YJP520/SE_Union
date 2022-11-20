#
# Crawler Edited by Pycharm.
# Time : 2022/10/07
# Author : YU.J.P
#

"""
    版本: V1.0
    基本功能:
        - 网页的重要性计算

    实验要求:
         给定网页链接关系，根据PageRank的计算公式计算网页的PR值，直到每个网页的PR值稳定为止，列出最终的PR值；
          假设每个网页的初始PR值相等。（计算结果保留小数点后5位数）
         根据PR值对网页重要性进行排序；如果有1,000,000个网页，你将使用什么排序技术，写出排序算法，查资料分析它与其它算法的优劣。
         扩展实验1：使用TextRank提取给定句子中的关键词。
         扩展实验2：利用NetworkX包(或其它)用图示的方式表示网络图。
         扩展实验3：利用NetworkX画出希拉里邮件中的人物关系图。

"""

from pygraph.classes.digraph import digraph
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import jieba.analyse
from Plug_in.Colors import Color


# -------------------------------------------------------------------------------------------------------------

# 给定网页链接关系，根据PageRank的计算公式计算网页的PR值，直到每个网页的PR值稳定为止，列出最终的PR值；
class PRIterator:
    __doc__ = '''计算一张图中的PR值'''

    def __init__(self, dg, max=10, d=0.5):
        """
        PageRank 构造函数
        :param dg: 创建好的图
        """
        self.damping_factor = d  # 阻尼系数,即d
        self.max_iterations = max  # 最大迭代次数
        self.min_delta = 0.00001  # 确定迭代是否结束的参数,即ϵ
        self.graph = dg  # 要计算的图

    def page_rank(self):
        """
        PageRank 计算函数
        :return: 各顶点PR值的列表
        """
        # 将
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, node2))

        nodes = self.graph.nodes()  # 顶点信息
        graph_size = len(nodes)  # 顶点个数
        if graph_size == 0:  # 图为空 返回空列表
            return {}

        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)
        damping_value = (1.0 - self.damping_factor) / graph_size  # 阻尼
        flag = False  # 计算标志

        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                    rank += damping_value
                    change += abs(page_rank[node] - rank)  # 绝对值
                    page_rank[node] = rank
            # print(Color.yellow, "# This is NO.%s iteration" % (i + 1), end=' ')
            # print(Color.blue, page_rank)
            if change < self.min_delta:
                flag = True
                break
        if flag:
            print(Color.carmine, "# finished in %s iterations!" % node)
        else:
            print(Color.green, "# finished out of 100 iterations!")
        return page_rank

    @classmethod
    def read_data(cls, path):
        """
        读取文件中的图信息
        :param path: 文件路径
        :return: 顶点集，边集
        """
        node_list = []  # 顶点集
        edge_list = []  # 边集
        with open(path) as f:
            lines = f.readlines()
            nodes = lines[1].split(' ')
            nodes[-1] = nodes[-1].split('\n')[0]
        for node in nodes:
            node_list.append(node)
            edges = lines[3:]
        for edge in edges:
            edge = edge.split(' ')
            edge[1] = edge[1].split('\n')[0]
            edge_list.append(edge)
        return node_list, edge_list

    @classmethod
    def test(cls):
        """
        PageRank 测试函数
        :return: None
        """
        # path = 'Data/Ex5_T1_Data/pagerank_four_nodes.txt'
        # path = 'Data/Ex5_T1_Data/pagerank_seven_nodes.txt'
        path = 'Data/Ex5_T1_Data/pagerank_tri_nodes.txt'
        node_list, edge_list = cls.read_data(path)
        print(Color.carmine, '# 顶点信息：', node_list)
        print(Color.carmine, '# 边信息：', edge_list)

        dg = digraph()
        dg.add_nodes(node_list)
        for edg in edge_list:
            dg.add_edge(edg)

        pr = PRIterator(dg)
        page_ranks = pr.page_rank()
        print(Color.green, "# The final page rank is", page_ranks)


# -------------------------------------------------------------------------------------------------------------

class TextRank:
    # 关键词抽取
    @classmethod
    def keywords_extraction(cls, text):
        tr4w = TextRank4Keyword(allow_speech_tags=['n', 'nr', 'nrfg', 'ns', 'nt', 'nz'])
        # allow_speech_tags   --词性列表，用于过滤某些词性的词

        tr4w.analyze(text=text, window=4, lower=True, vertex_source='all_filters', edge_source='no_stop_words',
                     pagerank_config={'alpha': 0.85, })
        # text    --  文本内容，字符串
        # window  --  窗口大小，int，用来构造单词之间的边。默认值为2
        # lower   --  是否将英文文本转换为小写，默认值为False
        # vertex_source  -- 选择使用words_no_filter, words_no_stop_words, words_all_filters中的哪一个来构造pagerank对应的图中的节点
        #                -- 默认值为`'all_filters'`，可选值为`'no_filter', 'no_stop_words', 'all_filters'
        # edge_source  -- 选择使用words_no_filter, words_no_stop_words, words_all_filters中的哪一个来构造pagerank对应的图中的节点之间的边
        #              -- 默认值为`'no_stop_words'`，可选值为`'no_filter', 'no_stop_words', 'all_filters'`。边的构造要结合`window`参数

        # pagerank_config  -- pagerank算法参数配置，阻尼系数为0.85

        keywords = tr4w.get_keywords(num=6, word_min_len=2)
        # num           --  返回关键词数量
        # word_min_len  --  词的最小长度，默认值为1
        return keywords

    # 关键短语抽取
    @classmethod
    def keyphrases_extraction(cls, text):
        tr4w = TextRank4Keyword()
        tr4w.analyze(text=text, window=2, lower=True, vertex_source='all_filters', edge_source='no_stop_words',
                     pagerank_config={'alpha': 0.85, })
        keyphrases = tr4w.get_keyphrases(keywords_num=6, min_occur_num=1)
        # keywords_num    --  抽取的关键词数量
        # min_occur_num   --  关键短语在文中的最少出现次数
        return keyphrases

    # 关键句抽取
    @classmethod
    def keysentences_extraction(cls, text):
        tr4s = TextRank4Sentence()
        tr4s.analyze(text, lower=True, source='all_filters')
        # text    -- 文本内容，字符串
        # lower   -- 是否将英文文本转换为小写，默认值为False
        # source  -- 选择使用words_no_filter, words_no_stop_words, words_all_filters中的哪一个来生成句子之间的相似度。
        # 		  -- 默认值为`'all_filters'`，可选值为`'no_filter', 'no_stop_words', 'all_filters'
        # sim_func -- 指定计算句子相似度的函数

        # 获取最重要的num个长度大于等于sentence_min_len的句子用来生成摘要
        keysentences = tr4s.get_key_sentences(num=3, sentence_min_len=6)
        return keysentences

    @classmethod
    def keywords_textrank(cls, text):
        keywords = jieba.analyse.textrank(text, topK=6)
        return keywords

# -------------------------------------------------------------------------------------------------------------
