from random import randint
from time import time
from sys import argv


def random_num_list_generator(aug):
    
    num_list = list()

    for i in range(int(aug)):
        num = randint(1, 100)
        num_list.append(num)

    return num_list


def main():
    
    start_time = time()

    # 随机生成一个包含十个随机数的列表
    try:
        aug = argv[1]

    except Exception:
        print('错误：缺少必要的参数')
        return
    
    else:
        num_list = random_num_list_generator(aug)
        print('生成的列表是:{}'.format(num_list))
        
        index_nums = input("输入数字：")
        index_nums = index_nums.split(",")
        
        index_list = list()
        
        for i in index_nums:
            index_list.append(int(i))
        # print(index_list)

        for i in range(int(aug)):
            if num_list[i] in index_list:
                print('{}存在于生成的列表中，序号是{}'.format(num_list[i], i+1))
            else:
                continue
    over_time = time()

    # print('时长：%d' % int(over_time))
    print(over_time-start_time)


if __name__ == '__main__':
    main()











