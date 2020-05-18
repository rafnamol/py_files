file = open(r"/Users/rafnaali/Desktop/interview code/text.txt", 'r')
content = file.readlines()
for line in content[0:3]:
   print(line)
#print(content)
file.close()
