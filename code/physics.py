from math import sqrt

from numpy import mean

info = input("请输入：")
info_list = info.split(",")
number_list = []
for i in info_list:
    number_list.append(eval(i))

number_of_sum = sum(number_list)

number_of_mean = number_of_sum/len(number_list)
def function(x):
    return (x - number_of_mean) ** 2

temp = 0
for i in info_list:
    temp += function(eval(i))

temp = temp / len(number_list)*(len(number_list)-1)
A = pow(temp, 0.5)
print("最佳估值：{} A类不确定度：{}".format(number_of_mean, A))