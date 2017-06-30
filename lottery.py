import numpy as np


# 产生随机不重复的数字list, length:list长度, divisor: 数字范围 1~divisor
def random_non_repetitive_list(length, divisor):
    while 1:
        flag = 0
        # 不知为何选取系数为 100 时随机值分布更均匀,可能涉及数值分析等专业领域知识
        number = list((np.random.rand(length) * 100).astype(np.int16) % divisor + 1)
        # 判断 list 中是否有重复的数字
        for i in range(length):
            for j in range(length - 1 - i):
                if number[length - 1 - i] == number[j]:
                    flag = 1
                    break

            if flag != 0:
                break

        if flag != 1:
            break

    number.sort()
    return number

count = int(input("请输入您的双色球彩票选取注数，按 ‘Enter’ 键结束："))
while count > 0:
    red_number = random_non_repetitive_list(6, 33)  # 6 个红色球
    blue_number = random_non_repetitive_list(1, 16) # 1 个蓝色球
    print(red_number[0], ",", red_number[1], ",", red_number[2], ",",
          red_number[3], ",", red_number[4], ",", red_number[5], ",",
          blue_number[0])
    count = count - 1

count = int(input("请输入您的大乐透彩票选取注数，按 ‘Enter’ 键结束："))
while count > 0:
    red_number = random_non_repetitive_list(5, 35) # 5 个蓝色球
    blue_number = random_non_repetitive_list(2, 12) # 2 个红色球
    print(red_number[0], ",", red_number[1], ",", red_number[2], ",",
          red_number[3], ",", red_number[4], ",", blue_number[0], ",",
          blue_number[1])
    count = count - 1





