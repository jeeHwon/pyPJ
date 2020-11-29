import re

print(re.search('ca{2}t', 'ct'))
print(re.search('ca{2}t', 'caat'))
print(re.search('ca{2,}t', 'caat'))
print(re.search('ca{2,5}t', 'caaaaat'))
print(re.search('ca?t', 'ct'))
print(re.search('ca?t', 'cat'))
print(re.search('ca?t', 'caat'))
print('\n'*30)

# sub(바꿀문자열, 대상문자열) : 치환
color = re.compile('(blue|green|red)')
print(color.sub('pink', 'orange book and green dress and red socks'))