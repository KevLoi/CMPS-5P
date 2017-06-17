# Kevin Loi
# kloi
# pa6
# Program that simulates a dice game

import random

# creates random number generator
rng = random.Random(237)

# --- functions ---------------------------------------------------------------
def throwDice(m, k):
	t = ()
	for i in range(m):
		num = rng.randrange(1, k+1)
		t = t + (num,)
	return t


# --- main --------------------------------------------------------------------
print()

# gets number of dice
dice = int(input("Enter the number of dice: "))
while dice<1:
	print("The number of dice must be at least 1")
	dice = int(input("Please enter the number of dice: "))
print()

# gets number of sides
sides = int(input("Enter the number of sides on each die: "))
while sides<2:
	print("The number of sides on each die must be at least 2")
	sides = int(input("Please enter the number sides on each die: "))
print()

# gets number of trials
trials = int(input("Enter the number of trials to perform: "))
while trials<1:
	print("The number of trials must be at least 1")
	trials = int(input("Please enter the number of trials to perform: "))
print()

# perform simulation, record frequencies
frequency = ((dice*sides)+1)*[0]
for i in range(trials):
	sum = 0
	t = throwDice(dice, sides)
	for j in range(len(t)):
		sum += t[j]
	frequency[sum] += 1

# get relative frequency, and Experimental Probability
relativeFrequency = []
experimentalProb = []
for j in range(dice):
	relativeFrequency.append(0)
	experimentalProb.append(0)
for k in range(dice, len(frequency)):
	relativeFrequency.append(frequency[k]/trials)
	percentage = relativeFrequency[k]*100
	experimentalProb.append(percentage)

# print(relativeFrequency)
# print(experimentalProb)
# print(frequency)

# print results
f1 = "{0:>4}{1:>14}{2:>23}{3:>29}"
f2 = 70*"-"
f3 = "{0:>4}{1:>11.0f}{2:>18.5f}{3:>21.2f}{4:>2}"
print(f1.format("Sum","Frequency","Relative Frequency","Experimental Probability"))
print(f2)
for x in range(dice, len(frequency)):
   print(f3.format(x, frequency[x], relativeFrequency[x], experimentalProb[x], "%"))
#end for
print()









		