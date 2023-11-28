
def entry():

    print ("\nPlease enter your password")
    password = input (">")

    if len(password) > 16 or len(password) < 6:
          print ("Your password must contain:")
          print ("- Minimum of 6 characters")
          print ("- Maximum of 16 characters")
          entry()

    if not any (char.isdigit() for char in password):
        print ("Your password must contain:")
        print ("- At least 1 number")
        entry()

    if not any (char.isupper() for char in password):
        print ("Your password must contain:")
        print ("- At least 1 uppercase letter")
        entry()

    if not any (char.islower() for char in password):
        print ("Your password must contain:")
        print ("- At least 1 lowercase letter") 
        entry()

    if not any (not char.isalnum() for char in password): #for loops to check for non-alphanumeric (special) characters in the string
        print ("Your password must contain:")
        print ("- At least 1 special character")
        entry()
          
    else:
        print ("\nYour password is valid!")
        entry()
    



print ("Welcome to the password creator.")
print ("\nYour password must contain:")
print ("- Minimum of 6 characters, maximum of 16 characters,")
print ("- At least 1 lowercase and uppercase letter,")
print ("- At least 1 integer number,")
print ("- At least 1 special character.")
entry()