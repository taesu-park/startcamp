# number.txt를 읽어서
#리스트(readlines)

with open('number.txt','r') as file:
    numbers = file.readlines()
print(numbers)




# 리스트를 뒤집는다.
numbers.reverse()



   
# number_reverse.txt로 저장!
# 4
# 3
# 2
# 1
# 0


with open('number_revers.txt','w') as file:
    for number in numbers:
        file.write(number)
