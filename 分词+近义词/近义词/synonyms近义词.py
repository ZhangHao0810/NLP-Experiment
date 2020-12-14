# @Software: PyCharm
# @Time    : 2020-12-14 10:52
# @Author  : Super-Zhang
# @Description :
import synonyms

print(synonyms.seg("中文近义词工具包"))

# 分词结果，由两个 list 组成的元组，分别是单词和对应的词性。
# (['中文', '近义词', '工具包'], ['nz', 'n', 'n'])


print("测试: ", synonyms.nearby("测试"))

list = [
    "交换","笑容","爱情","初恋",
    "模型",
    "功能",
    "设计模式",
    "算法",
    "软件工程",
    "近义词"
]

s = ""

for s in range(len(list)):
    print(list[s], synonyms.nearby(list[s]))
    print(" ")
