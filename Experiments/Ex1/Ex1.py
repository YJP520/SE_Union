"""
    @Time : 2022/09/12
    @Author : YU.J.P
    @Project : 实验 1 顺序检索技术
    @Description:
        Set up on 2022/09/12 - Finish Some Algorithms(BE and KMF).
        Upgrade on 2022/09/13 - Establish OrderMatch class and Finish BM.

"""


# 信息处理类
class OrderMatch:
    def __init__(self):
        pass

    # Brute Force - BF串匹配算法 查找一次
    @classmethod
    def BruteForceStringMatch(cls, S, P):
        for i in range(0, len(S) - 1):
            j = 0
            while S[i + j] == P[j] and j < len(P):
                j += 1
                if j == len(P):
                    return i
        return -1

    # Brute Force - BF串匹配算法 查找多次
    @classmethod
    def BruteForceStringMatchAll(cls, S, P, pos=0):
        position = []  # 索引列表
        S_len, P_len = len(S), len(P)
        for i in range(pos, S_len - 1):
            j = 0
            while S[i + j] == P[j] and j < P_len:
                j += 1
                if j == P_len:
                    position.append(i)  # 找到一个就加到列表中
                    break  # 退出此层循环
        return position  # 返回列表

    # 首先计算模式串的Next数组  这里是用回溯进行计算的
    @classmethod
    def calNext(cls, string):
        i = 0
        Next = [-1]
        j = -1
        while i < len(string) - 1:
            if j == -1 or string[i] == string[j]:  # 首次分析可忽略
                i += 1
                j += 1
                Next.append(j)
            else:
                j = Next[j]  # 会重新进入上面那个循环
        return Next

    # KMP算法 查找一次
    @classmethod
    def KMP_StringMatch(cls, S, P, pos=0):  # 从那个位置开始比较
        Next = OrderMatch.calNext(P)  # 计算 Next数组
        i = pos  # 开始位置，默认为 0
        j = 0
        while i < len(S) and j < len(P):
            if j == -1 or S[i] == P[j]:
                i += 1
                j += 1
            else:
                j = Next[j]
        if (j >= len(P)):
            return i - len(P)  # 说明匹配到最后了
        else:
            return 0

    # KMP算法 查找多次
    @classmethod
    def KMP_StringMatchAll(cls, S, P, pos=0):  # 从那个位置开始比较
        position = []  # 索引列表
        Next = OrderMatch.calNext(P)  # 计算 Next数组
        S_len, P_len = len(S), len(P)
        i = pos  # 开始位置，默认为 0
        j = 0
        while i < S_len and j < P_len:
            if j == -1 or S[i] == P[j]:
                i += 1
                j += 1
            else:
                j = Next[j]
            if j >= P_len:  # 说明匹配到最后了
                position.append(i - P_len)
                i += 1  # 更新位置
                j = 0  # 更新索引
        return position  # 返回列表

    # 模式匹配 Boyer-Moore
    @classmethod
    def BoyerMooreStringMatch(cls, S, P):
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
