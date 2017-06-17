name = str(input("Your file name: "))
f = open(name, 'r')
L = f.readlines()
f.close()

for i in range(len(L)-1, -1, -1):
   print(L[i])
