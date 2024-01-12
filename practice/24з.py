import re
txt = open('24_10724.txt').readline().strip()
result = re.findall(r'[1-9A-F]+', txt)
print(max([len(i) for  i in result]))
#print(max([len(i) for  i in re.findall(r'[1-9A-F]+', open('24_10724.txt').readline().strip())]))
