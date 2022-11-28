#630510582
#tulakorn sawangmuang
#section-001
#Lab03-01
#find volume

import math #import function math

def find_r_from_surface_area(surface_area): #create function surface area
    radius = (surface_area/(4*math.pi))**(1/2) #Equation find radius
    return radius #return radius value to this function

def sphere_volume(radius): #create function 
    volume = (4/3)*(math.pi)*(radius**3) #Equation find volume
    return volume #return volume value to this function

def main(): 
    # get surface area from user input
    surface_area = float(input("input surface area: ")) 
    # calculate radius from surface area
    radius = find_r_from_surface_area(surface_area) 
    # use radius to caculate volume
    volume = sphere_volume(radius) 
    # display volume
    print("volume = {0:.2f}".format(volume)) #Answer

if __name__=='__main__': #Check name 
    main()
