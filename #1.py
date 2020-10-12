#1.	The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas are the same.

length1 = float(input("what is the length of the first rectangle:"))
width1 = float(input("what is the width of the first rectangle:"))
length2 = float(input("what is the length of the second rectangle:"))
width2 = float(input("what is the width of the second rectangle:"))

area1 = length1 * width1 
area2 = length2 * width2

if area1 > area2:
    print("The area of the first triangle is greater.")
elif area2 > area1:  
    print("The area of the second rectangle is greater.")
else:
    print("The areas are equal.")

      