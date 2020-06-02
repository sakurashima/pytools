# coding=utf-8
import re



def main():
	with open('word_banned.txt', 'r', encoding='utf-8') as f:
		content = f.read()
	
	banned_words_list = content.split('\n')
	
	# 列表元素的个数，需要去除最后一个空的元素
	banned_words_list.remove(banned_words_list[len(banned_words_list)-1])
	
	
	# 把单词拼接到一起，分枝结构
	word_pattern = str()
	for word in banned_words_list:
		word_pattern += word + '|'
	word_pattern = word_pattern[:len(word_pattern)-1]
	print(word_pattern)

	sentence = input("人人争当祖安人：")

	ret = re.match(word_pattern, sentence)
	if not ret:
		print(sentence)
	if ret:
		ret1 = ret.group()
		print(sentence.replace(ret1, len(ret1)*'*'))



if __name__ == '__main__':
	main()
