#630510582
#tulakorn sawangmuang
#Section-001
#Lab06_4

def find_max_2nd_average():
    student = int(input("Total students: ")) # input Number of students 
    print("Enter score:") 
    max = 0 # max score value
    round_up = 0 # 2nd score
    point = 0 # the point of all students

    for i in range(abs(student)): # do loop
        score = float(input()) # input scroe students
        if score > max: # condition 
            round_up = max # equation
            max = score # max value
        elif max > score > round_up: # another condition
            round_up = score # 2nd score
        point += score # plus point from students
    average1 = abs(point/student) # average value
    print("---")
    print("Max score is: %.2f"%(max)) # display max score
    if average1 == max: # condition of 2nd score
        print("Runner up is: None") # display 
    else: # other condition
        print("Runner up is: %.2f"%(round_up)) # display 2nd score
    print("Average is: %.2f"%(average1)) # display average the score

if __name__ == "__main__":
    find_max_2nd_average()

