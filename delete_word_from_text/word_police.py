"""
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

def main():
        
    with open('word_banned.txt', 'r') as f:
        content = f.read()
    

    # filter off the None segement
    word_list = list(filter(None, content.split('\n')))
    
    # print(word_list)
    
    user_input = input()
    
    for word in word_list:
        if word in user_input:
            user_input = user_input.replace(word, len(word)*'*')
    print(user_input)

    # user_input.replace(content, '**')
    # message = 'aaaaaaaab'
    # print(message.replace('a', '*'))

    

if __name__ == '__main__':
    main()
