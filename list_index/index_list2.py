import random
from sys import argv
from time import time


def num_list_generator(aug):
    
    num_list = list()

    for i in range(int(aug)):
        num = random.randint(1, 100)
        num_list.append(num)

    return num_list


def run():
    
    # 随机生成一个包含十个随机数的列表
    aug = argv[1]
    num_list = num_list_generator(aug)
    print('生成的列表是:{}'.format(num_list))
    
    index_nums = input("输入数字：")
    index_nums = index_nums.split(",")
    
    index_list = list()
    
    for i in index_nums:
        index_list.append(int(i))
    # print(index_list)

    for i in range(int(aug)):
        if num_list[i] in index_list:
            print('{}在生成的列表中，排序是{}'.format(num_list[i], i+1))
        else:
            continue


def time_clock_decrator(func):
    def inner(func):
        start_time = time()
        func()
        over_time = time()
        print(over_time-start_time)
    return inner
        

@time_clock_decrator(run)
def main():
    print("dasda")

if __name__ == '__main__':
    main()











