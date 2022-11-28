#630510582
#tulakorn sawnagmuang
#section-001
#Lab02-03
#Find the intersection of two straight lines
print("First Equation") #1st Equation
m1 = float(input("Input m1: ")) #The value of m1
b1 = float(input("Input b1: ")) #The value of b1
print("Second Equation") #2nd Equation
m2 = float(input("Input m2: ")) #The value of m2
b2 = float(input("Input b2: ")) #The value of b2
x = (b2-b1)/(m1-m2) #Equation X
y = (m1*x)+b1 #Equation Y
print("The point of intersection is at x = %.2f and y = %.2f"%(x,y)) #Answer