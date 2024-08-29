num = input("how many times")
num = int(num)
fibo = 0
myList = [0, 1]
for i in range(2, num):
    fibo = myList[i-2] + myList[i-1]
    myList.append(fibo)

print(myList)