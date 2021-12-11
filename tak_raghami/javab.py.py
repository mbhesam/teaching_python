from sys import argv
number = argv[1]
each_number=[]
for i in range(len(number)):
    each_number.append(int(number[i]))
#print(type(each_number[1]))
#print(each_number)
while True:
    sum =0
    for i in range(len(each_number)):
        sum = sum + int(each_number[i])
    if len(str(sum)) == 1:
        print(sum)
        break
    else:
        number = str(sum)
        each_number=[]
        for j in range(len(number)):
            each_number.append(number[j])
        continue

