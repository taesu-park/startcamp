# window - cp949(encoding)
# mac/web... - utf-8

# readlines는 라인을 각각 리스트의 원소로 하여 반환한다.
with open('ssafy_with.txt','r') as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())

with open('ssafy.txt','r') as f:
    # read : 전체 내용을 하나의 string으로 반환한다.
    txt = f.read()

print(txt)


