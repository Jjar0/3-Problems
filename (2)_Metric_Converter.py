
def menu():
    
    print ("Which units would to like to convert?") #output of main menu for user.
    print ("[1] Miles to Kilometers")
    print ("[2] Feet to Meters")
    print ("[3] Yards to Meters")
    print ("[4] Inches to Centimeters")

    menuSelection = input (">") #menu function to choose conversion rate.

    conversionRate = 0 #variable defenitions.
    imperial = ""
    metric = ""

    if menuSelection == "1":
        conversionRate = 1.6 #conversion rate and measurements are stored in variables for later use. 
        imperial = "miles"  #when condition is true, values are assigned to variables and cvarried through to convert function
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
        print ("Please enter one of the numbers listed above") #basic validation to check for invalid code.
        menu()
    
def convert(conversionRate,imperial,metric): #function is used to loop converter.

    conversionRate = float(conversionRate) #data stype casting so that conversion rates can be operated in maths.
    
    print ("enter 0 to exit to the menu")
    print ("Please enter a value in " + imperial) #tells user to input the data in thier chosen imperial unit via variable.
    inp = input (">")

    if inp == "0": #exit condition to return to menu at any time.
        menu()

    try:
        inp = float(inp) #validation for user input as a float value.
    except:
        print ("Please enter a numeric value")
        convert(conversionRate,imperial,metric) #uses function to loop upon non float entry.

    inp = float(inp)
    out = (inp * conversionRate) #calculation conversion to find metric value.
    
    #imperial/metric strings are used so output message defines which numbers are which measurements
    print (str(inp) + " " + imperial + " is " + "%.2f" % out + " in " + metric + ".") #[REVISION] string formatting keeps outputted values to 2 decimal places for easier readability.
    convert(conversionRate,imperial,metric)  

print ("Welcome to the imperial to metric unit converter!")
menu() #restart game
