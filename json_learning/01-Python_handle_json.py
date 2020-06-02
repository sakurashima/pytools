import json


def main():
	my_dict = {
	'name': 'martin-ghs',
	'age': 20,
	'gender': '男',
	'computer': [
	{'leveno': '小新'},
	{'huawei': 'dsad'},
	]
}


	try:
		with open('handle_json.json', 'w', encoding='utf-8') as f:
			json.dump(my_dict, f)
	except Exception:
		return Exception
	
	print('数据保存成功!')


if __name__ == '__main__':
	main()
