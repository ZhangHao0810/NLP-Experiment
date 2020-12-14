# @Software: PyCharm
# @Time    : 2020-12-14 10:52
# @Author  : Super-Zhang
# @Description :
import synonyms
print(synonyms.seg("中文近义词工具包"))

# 分词结果，由两个 list 组成的元组，分别是单词和对应的词性。
# (['中文', '近义词', '工具包'], ['nz', 'n', 'n'])


print("交换: ", synonyms.nearby("交换"))