
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
        menu()
    
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
    
    milesValue = str(milesValue)
    kiloValue = str(kiloValue)

    print (milesValue + " miles is " + kiloValue + " in Kilometers.")
    miles()   

def feet():
    
    print ("enter 0 to exit to the menu")
    print ("Please enter a value (in feet)")
    feetValue = input (">")

    if feetValue == "0":
        menu()

    try:
        feetValue = float(feetValue)
    except:
        print ("Please enter a numeric value")
        feet()

    feetValue = float(feetValue)
    cmValue = (feetValue * 30.48)
    
    feetValue = str(feetValue)
    cmValue = str(cmValue)

    print (feetValue + " feet is " + cmValue + " in centimeters.")
    feet()   

def yards():
    
    print ("enter 0 to exit to the menu")
    print ("Please enter a value (in yards)")
    yardsValue = input (">")

    if yardsValue == "0":
        menu()

    try:
        yardsValue = float(yardsValue)
    except:
        print ("Please enter a numeric value")
        yards()

    yardsValue = float(yardsValue)
    mValue = (yardsValue * 0.9144)
    
    yardsValue = str(yardsValue)
    mValue = str(mValue)

    print (yardsValue + " yards is " + mValue + " in meters.")
    yards()   

def inches():
    
    print ("enter 0 to exit to the menu")
    print ("Please enter a value (in inches)")
    inchValue = input (">")

    if inchValue == "0":
        menu()

    try:
        inchValue = float(inchValue)
    except:
        print ("Please enter a numeric value")
        inches()

    inchValue = float(inchValue)
    cmValue = (inchValue * 2.54)
    
    inchValue = str(inchValue)
    cmValue = str(cmValue)

    print (inchValue + " inches is " + cmValue + " in centimeters.")
    inches()


print ("Welcome to the imperial to metric unit converter!")
menu()