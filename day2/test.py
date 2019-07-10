with open('test.txt','r') as f:
    txt = f.read()
print(txt)


with open('test.txt','r') as f:
    lines = f.readlines()
for line in lines:
    print(line)
