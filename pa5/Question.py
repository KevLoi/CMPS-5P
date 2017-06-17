# Kevin Loi
# kloi
# pa5
# Plays Guesser of Guessing Game

print()
print()
print("Enter two numbers, low then high.")

# get low then high
low = int(input("low = "))
high = int(input("high = "))
print()
while low>high:
	print("Please enter the smaller followed by the larger number.")
	low = int(input("low = "))
	high = int(input("high = "))
	print()

print("Think of a number in the range", low, "to " +str(high) + ".\n")

# Begin guessing
count = 0
while low<=high:
   m = (low + high)//2
   if low==high:
      if count==1:
         print("I found your number in 1 guess. \n")
         print()
      else:
         print("Your number is " +str(m) + ". I found it in", count, "guesses. \n")
         print()
      break
   print("Is your number Less than, Greater than, or Equal to " +str(m) + "?")
   ans = str(input("Type 'L', 'G' or 'E': "))
   print()
   count += 1
   while ans!='G' and ans!='g' and ans!='L' and ans!='l' and ans!='E' and ans!='e':
      ans = str(input("Please type 'L', 'G', or 'E': "))
      print()
   if ans=='E' or ans=='e':
      if count==1:
         print("I found your number in 1 guess. \n")
         print()
      else: 
         print("Your number is " +str(m) + ". I found it in", count, " guesses. \n")
         print()
      break
   if ans=='L' or ans=='l':
      high = m-1
   if ans=='G' or ans=='g': #ans=='G' or ans=='g'
      low = m+1

if low>high:
   print("Your answers have not been consistent. \n")
   print()

