# @Software: PyCharm
# @Time    : 2020-12-14 10:02
# @Author  : Super-Zhang
# @Description :

# 实验正式开始
import synonyms

# 待匹配句子。
ListNLP=[
    '我爱吃馒头',"我爱吃油条",
    "我喜欢萝莉","我喜欢御姐",
    "我爱数学课","我爱跳舞",
    "这个程序的功能是 吃豆豆游戏","这是一个吃豆豆游戏程序",
    "英雄联盟","王者荣耀",
    "过程模式挖掘","功能性过程模式挖掘"
]

# 两个列表接住每一列
list1=[]
list2=[]

print("-----存入list1---------")
for i in range(0, len(ListNLP),2):
    print("s1:" ,ListNLP[i])
    list1.append(ListNLP[i])
print("-----存入list2---------")
for i in range(1, len(ListNLP),2):
    print("s2:" ,ListNLP[i])
    list2.append(ListNLP[i])

print("list1",list1)
print("list2",list2)

for s1,s2 in zip(list1,list2) :
   # print(s1,s2, synonyms.compare(s1,s2, seg=False)) 如果False 表示不分词，模型里面就没有词 全部警告。
   print(s1, s2, synonyms.compare(s1, s2, seg=True))