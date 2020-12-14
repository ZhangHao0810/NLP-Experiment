# @Software: PyCharm
# @Time    : 2020-12-14 11:34
# @Author  : Super-Zhang
# @Description :
# @Software: PyCharm
# @Time    : 2020-12-14 10:02
# @Author  : Super-Zhang
# @Description :

# 实验正式开始
import synonyms

# 待匹配句子。
ListNLP = [
    '两数交换',"a与b交换",
'两数交换',"变量a与变量b变换",
    "两个变量交换位置","x与y变换",
    "变换两个游戏角色的位置","互相改变角色1与角色2的地理坐标"
]

# 两个列表接住每一列
list1 = []
list2 = []

print("-----存入list1---------")
for i in range(0, len(ListNLP), 2):
    print("s1:", ListNLP[i])
    list1.append(ListNLP[i])
print("-----存入list2---------")
for i in range(1, len(ListNLP), 2):
    print("s2:", ListNLP[i])
    list2.append(ListNLP[i])

print("list1", list1)
print("list2", list2)

for s1, s2 in zip(list1, list2):
    # print(s1,s2, synonyms.compare(s1,s2, seg=False)) 如果False 表示不分词，模型里面就没有词 全部警告。
    print(s1, s2, synonyms.compare(s1, s2, seg=True))
