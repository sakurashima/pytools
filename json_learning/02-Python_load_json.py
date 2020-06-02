import json


def main():

	try:
		with open('handle_json.json', 'r', encoding='utf-8') as f:
			json_dicts = json.load(f)
	except Exception:
		return Exception	
	else:
		for k in json_dicts.keys():
			print(k, json_dicts[k])
		for i, j in json_dicts.items():
			print(i,'=',j)
	

if __name__ == "__main__":
	main()
