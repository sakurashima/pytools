from random import randint


def index_generatot(i):
    if i == 1:
        print('这是1的流程')
    elif i == 2:
        print('这是2的流程')


def main():
    """主程序"""
    for i in range(3):
        index_generatot(i)

    

if __name__ == '__main__':
    main()
