# @Software: PyCharm
# @Time    : 2020-12-14 10:52
# @Author  : Super-Zhang
# @Description :
import synonyms
print(synonyms.seg("中文近义词工具包"))

# 分词结果，由两个 list 组成的元组，分别是单词和对应的词性。
# (['中文', '近义词', '工具包'], ['nz', 'n', 'n'])


print("交换: ", synonyms.nearby("交换"))

print("交换: ", synonyms.nearby("交换"))
print("两数: ", synonyms.nearby("两个数"))

# sen1 = "两数交换"
# sen2 = "a与b交换"
# r = synonyms.compare(sen1, sen2, seg=True)
# print(r)
print("=======语义相似度计算==========")

# 名词和动词可以比较好的进行计算。

# print(synonyms.compare("打开主函数", "开启main函数", seg=True))



print("两数交换","交换两个变量", synonyms.compare("两数交换","交换两个变量", seg=True))
print("我爱看中国有嘻哈", "中国有嘻哈是我爱看的节目",synonyms.compare("我爱看中国有嘻哈", "中国有嘻哈是我爱看的节目", seg=True))
print("打开主函数", "开启main函数", synonyms.compare("打开主函数", "开启main函数", seg=True))

