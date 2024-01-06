from math import pow

num1 = int(input("Put your first score:"))
num2 = int(input("Put your second score: "))

print("Your score is {}, While  your second score is {}. So therefore your overall is {} ".format(num1,num2,pow(num2,2)/2))