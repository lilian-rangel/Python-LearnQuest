myList = []
x = int(input())
while x != -1:          #recebe entradas até -1
    myList.append(x)
    x = int(input())
sum = 0
for x in myList:
    sum += x
print(int(sum/len(myList)))     #imprime o número medio
for x in myList:
    print(x)        #imprime a lista na ordem de entrada