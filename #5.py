#5.	Assume that hot dogs come in package of 10, and hot dog buns come in packages of 8. Write a program that calculates the number of packages of hot dogs and the number packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given. The program should display the following details:
#a.The minimum number of packages of hot dogs required
#b.The minimum number of packages of hot dog buns required
#c.The number of hot dogs that will be left over
#d.he number of hot dog buns that will be left over

dogsPerpack = 10
bunsPerpack = 8
num_people = int(input("How many poeple are attending:"))
dogsPerperson = int(input("How many hot dogs will each person want?:"))

numDogs = num_people * dogsPerperson
if numDogs / dogsPerpack == numDogs // dogsPerpack:
    dogsPerpack = numDogs // dogsPerpack
    leftover_dogs = 0
else:
    dogsPerpack = numDogs // dogsPerpack + 1
    leftover_dogs = dogsPerpack - numDogs % dogsPerpack
if numDogs / bunsPerpack == numDogs // bunsPerpack:
    bunsPerpack = numDogs // bunsPerpack
    leftover_buns = 0
else: 
    bunsPerpack = numDogs // bunsPerpack + 1
    leftover_buns = bunsPerpack - numDogs % bunsPerpack
print("/nMinimum number of packages of hotdogs:", dogsPerpack)
print("Minimum number of packages of hotdogs:", bunsPerpack)
print("Number of left over hotdogs:", leftover_dogs)
print("Number of left over hotdogbuns:", leftover_buns)
                  