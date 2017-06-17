# Kevin Loi
# kloi
# pa4
# Prints the first n prime numbers 


# isPrime: checks if the number is prime or composite -------------------------
def isPrime(m, L):
	for p in L:
		if m < p**2:
			return True
			break
		if m%p==0:
			return False 
			break



# main program ----------------------------------------------------------------

'''ask for user input'''
n = int(input('Enter a positive integer: '))

'''initialize primeList'''
primeList = [2]

'''go through each number until len(primeList)==n'''
nextNum = 2
while len(primeList)<n:
	nextNum += 1
	if( isPrime(nextNum, primeList)==True ):
		primeList.append(nextNum)


'''print primeList'''
for i in range(0, len(primeList), 10):
	print( *primeList[i:i+10] )
