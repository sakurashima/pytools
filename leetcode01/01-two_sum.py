# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def number_sum(new_list, target):
    ret = list()
    ret_f = list()
    for i in range(len(new_list)):
        num_target = target - new_list[i]
        for j in new_list:
            if j == num_target:
                ret.append((new_list[i], j)) 
            else:
                pass
    # [(7, 37), (8, 36), (23, 21), (21, 23), (36, 8), (37, 7)]
    for h in range(int(len(ret)/2)):
        ret_f.append(ret[h])
    return ret_f
    
def filter(num, target):
    
    # 浅拷贝，只对列表第一层进行拷贝
    new_number_list = list()

    # 筛选出符合条件的数
    for i in range(len(num)):
        if num[i] >= target:
            pass
        else:
            new_number_list.append(num[i])
   
    # 调用函数
    number_turple = number_sum(new_number_list, target)
    print(number_turple)
"""
def filter_senior(num, target):
    
    new_number_list_02 = num.copy()
    new_number_list_02.sort(reverse=False)
    print(new_number_list_02)
"""
def main():

    list_test = [2, 4, 5, 6, 3, 7, 3, 10, 11, 23, 21, 24, 36, 37, 18]
    filter(list_test, 44)


if __name__ == '__main__':
    main()
