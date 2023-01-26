"""
======================
Author: 柠檬班-小简
Time: 2022/7/20 20:14
Project: day8_PO_v3-写完版本-无basepage
Company: 湖南零檬信息技术有限公司
======================
"""

mylist = ["py49", "小冷漠", "活出自己", "安稳"]

sex = ["男","男","男","男"]

for index in range(len(mylist)):
    print(index, mylist[index])

print(list(enumerate(mylist)))

# mydict = {}
# for index, value in enumerate(mylist,start=1):
#     mydict[value] = sex[index]