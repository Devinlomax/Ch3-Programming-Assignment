#6.	A software company sells a package that retails for $99.  Quantity discounts are given according to the following: 10 – 19 (10%), 20 - 49 (20%), 50 – 99 (30%), and 100 or more (40%). Write a program that asks the user to enter the number of packages purchased. The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount
retailprice = 99
quantity = int(input("Quantity purchased:"))

if quantity <10:
    discount = 0
elif 10 <= quantity and quantity < 20:
    discount = 0.1
elif 20 <= quantity and quantity < 50:
    discount = 0.2
elif 50 <= quantity and quantity < 100:
    discount = 0.3
else:discount = 0.4
subtotal = retailprice * quantity 
totaldiscount = subtotal * discount 
total = subtotal - totaldiscount

print(format("\nSubtotal:", "<10s") , "$", format(subtotal, ",.2f"))
print(format("Discount:", "<10s") , "$", format(totaldiscount, ",.2f"))
print(format("total:", "<10s")  , "$", format(total, ",.2f"))     
             