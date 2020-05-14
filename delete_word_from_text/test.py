"""
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""

def main():
    
    # 用户输入语句
    user_words = input('')

    with open('word_banned.txt', 'r') as f:
        if user_words in f.read():
            print('freedom')
        else:
            print('humain rights')

        

    # 输出用户输入语句
    # print(user_words)




if __name__ == '__main__':
    main()
