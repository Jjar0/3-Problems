import time

def menu():
    
    print ("Which units would to like to convert?")
    print ("[1] Miles to Kilometers")
    print ("[2] Feet to Meters")
    print ("[3] Yards to Meters")
    print ("[4] Inches to Centimeters")

    menuSelection = input (">")

    if menuSelection == "1":
        miles()
    if menuSelection == "2":
        feet()
    if menuSelection == "3":
        yards()
    if menuSelection == "4":
        inches()
    else:
        print ("Please enter one of the numbers listed above")
    
def miles():
    
    print ("enter 0 to exit to the menu")
    print ("Please enter a value (in miles)")
    milesValue = input (">")

    if milesValue == "0":
        menu()

    try:
        milesValue = float(milesValue)
    except:
        print ("Please enter a numeric value")
        miles()

    milesValue = float(milesValue)
    kiloValue = (milesValue * 1.6)
    print (milesValue + " miles is " + kiloValue + " in Kilometers!")
    miles()   

def feet():
    

def yards():
    

def inches():



print ("Welcome to the imperial to metric unit converter!")
menu()