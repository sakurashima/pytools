import re



html_tag = "<a href=\"https://kunqian888.cn\">link is not the Linker</a>"


pattern = re.compile("<a href=\"(.*)\">(\w*)</a>")
content = re.findall(pattern, html_tag)

for i in content:
    print(i[0])
    print(i[1])
