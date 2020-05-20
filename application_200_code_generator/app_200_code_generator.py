from random import randint


def app_code_generator():
    """
    生成的code应该包括a-z,0-9,A-Z，一共有十三位.前三位是小写字母，后九位是数字，最后一位是大写字母,
str.upper()方法可以是小写字母变成大写。
    """

    # 利用asii码，输出随机a-z
    # code1 = chr(randint(97, 122))
    # code2 = chr(randint(97, 122))
    # code3 = chr(randint(97, 122))，不可能真正意义上使用这种方法，效率太低
    i = 0
    app_code = str()
    while i<13:
        # 48～57为0到9十个阿拉伯数字。65～90为26个大写英文字母，97～122号为26个小写英文字母
        choice = randint(1, 3)
        if choice == 1:
            app_code += chr(randint(48, 57)) 
        elif choice == 2:
            app_code += chr(randint(65, 90))
        elif choice == 3:
            app_code += chr(randint(97, 122))
        
        i += 1
    return app_code


def main():
    
    app_code_set = set()
    # app_code_list = list()
    # i=1的时候就需要写i<=200
    i = 0

    # 此时，完成200次的操作
    while i < 200:
        app_code_set.add(app_code_generator())
        # app_code_list.append(app_code_generator())
        i += 1

    # 有很微小的几率会出现重复的元素，又因为是集合，不能出现相同的元素，所以需要判断集合内元素的个数是否是200个
    while len(app_code_set) < 200:
        app_code_set.add(app_code_generator())

    
    # 最后输出200位优惠吗
    for code in app_code_set:
        print(code)


if __name__ == '__main__':
    main()
