
def menu():
    
    print ("Which units would to like to convert?")
    print ("[1] Miles to Kilometers")
    print ("[2] Feet to Meters")
    print ("[3] Yards to Meters")
    print ("[4] Inches to Centimeters")

    menuSelection = input (">") #menu function to choose conversion rate.

    conversionRate = 0
    imperial = ""
    metric = ""

    if menuSelection == "1":
        conversionRate = 1.6
        imperial = "miles"
        metric = "kilometers"
        convert(conversionRate,imperial,metric)
        
    if menuSelection == "2":
        conversionRate = 30.48
        imperial = "feet"
        metric = "meters"
        convert(conversionRate,imperial,metric)
        
    if menuSelection == "3":
        conversionRate = 0.9144
        imperial = "yards"
        metric = "meters"
        convert(conversionRate,imperial,metric)
        
    if menuSelection == "4":
        conversionRate = 2.54
        imperial = "inches"
        metric = "centimeters"
        convert(conversionRate,imperial,metric)
        
    else:
        print ("Please enter one of the numbers listed above")
        menu()
    
def convert(conversionRate,imperial,metric):

    conversionRate = float(conversionRate)
    
    print ("enter 0 to exit to the menu")
    print ("Please enter a value in " + imperial)
    inp = input (">")

    if inp == "0":
        menu()

    try:
        inp = float(inp)
    except:
        print ("Please enter a numeric value")
        convert(conversionRate,imperial,metric)

    inp = float(inp)
    out = (inp * conversionRate)
    
    inp = str(inp)
    out = str(out)

    print (inp + " " + imperial + " is " + out + " in " + metric + ".")
    convert(conversionRate,imperial,metric)  

print ("Welcome to the imperial to metric unit converter!")
menu()