# @Software: PyCharm
# @Time    : 2020年12月14日09:42:41
# @Author  : Super-Zhang
# @Description :


#1、创建与访问列表
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7]
#
# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[1:5])

#2.用for 来遍历列表
ListNLP=[
    '我爱吃馒头',"我爱吃油条",
    "我喜欢萝莉","我喜欢御姐",
    "我爱数学课","我爱跳舞",
    "这个程序的功能是 吃豆豆游戏","这是一个吃豆豆游戏程序"
]
# for s in  ListNLP :
#     print("s: " ,s )

#2.控制步长遍历列表(两个两个的取）
for i in range(0, len(ListNLP),2):
    print("s1:" ,ListNLP[i])
print("------分割--------")
for i in range(1, len(ListNLP),2):
    print("s2:" ,ListNLP[i])

#3.成对的将句子保存起来,存成两个列表即可，对应位置是一对句子。
list1=[]
list2=[]

for i in range(0, len(ListNLP),2):
    print("s1:" ,ListNLP[i])
    list1.append(ListNLP[i])
print("-----list存储---------")
for i in range(1, len(ListNLP),2):
    print("s2:" ,ListNLP[i])
    list2.append(ListNLP[i])

print(list1)
print(list2)