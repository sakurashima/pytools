# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution(object):

    def __init__(self, num=[], target=0):
        self._num = num
        self._target = target 
        self.ret_f = list()
        self.new_number_list = list()
    
    @property
    def num(self):
        return self._num

    @property
    def target(self):
        return self._target
    
    @num.setter
    def num(self, num):
        self._num = num

    @target.setter
    def target(self, target):
        self._target = target

    def number_sum(self, new_list, target):
        ret = list()
        for i in range(len(new_list)):
            num_target = self.target - new_list[i]
            for j in new_list:
                if j == num_target:
                    ret.append((new_list[i], j)) 
                else:
                    pass
        # [(7, 37), (8, 36), (23, 21), (21, 23), (36, 8), (37, 7)]
        for h in range(int(len(ret)/2)):
            self.ret_f.append(ret[h])
        return self.ret_f
    
    def filter(self):
    
        # 筛选出符合条件的数
        for i in range(len(self._num)):
            if self.num[i] >= self.target:
                pass
            else:
                self.new_number_list.append(self.num[i])
       
        # 调用函数
        number_turple = self.number_sum(self.new_number_list, self.target)
        if not number_turple:
            print('该数组不存在')
        else:
            print(number_turple)
    """
    def filter_senior(num, target):
        
        new_number_list_02 = num.copy()
        new_number_list_02.sort(reverse=False)
        print(new_number_list_02)

    """
obj = Solution()
obj.num = [3,4,8,0,9,8,12,34,14,56,76,98,89,90,67]
obj.target = 100
obj.filter()



