from sys import argv


def main():
    

    # 永远不要忘记给程序一个合理的出口
    try:
        input_message = argv[1]
    except IndexError as ret:
        print("输入信息有误")
        return
    else:
       print('输入的信息是{}'.format(input_message))



if __name__ == '__main__':
    main()
