#630510582
#tulakorn sawnagmuang
#section-001
#Lab02-04
#Convert time units From fractions of a second
x = int(input("Input number of milliseconds: ")) #The value of x (milliseconds)
day = x//86400000 #Equation day
y = x%86400000 #Equation y
hour = y//3600000 #Equation hour
z = y%3600000 #Equation z
minute = z//60000 #Equation minute
a = z%60000 #Equation a
second = a//1000 #Equation second
b = a%1000 #Equation b
millisec = b #Equation millisec
print("Results = %d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s)"%(day,hour,minute,second,millisec)) #Answer