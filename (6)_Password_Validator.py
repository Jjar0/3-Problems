
def entry():

    print ("\nPlease enter your password")
    password = input (">")

    valid = True

    #series of if statements which check validation, if any fail, function is looped.
    if len(password) > 16:  
        print("Password must be no more than 16 characters") #User is informed of which requirement(s) failed.
        valid = False

    if len(password) < 6:
        print ("Password must be a minimum of 6 characters")
        valid = False

    #'any' function check for requirements,for loop checks characters in string.
    if not any (char.isdigit() for char in password): 
        print ("Password must contain at least 1 number") 
        valid = False
        

    if not any (char.isupper() for char in password):
        print ("Password must contain at least 1 uppercase letter")
        valid = False
        

    if not any (not char.islower() for char in password): #[REVISION] Fixed special character validation loop.
        print ("Password must contain at least 1 lowercase letter") 
        valid = False
        

    if not any (not char.isalnum() for char in password): 
        print ("Password must contain at least 1 special character")
        valid = False

    if valid == True:
        print ("\nYour password is valid!")
        
    entry()

print ("Welcome to the password creator.")
print ("\nYour password must contain:")
print ("- Minimum of 6 characters, maximum of 16 characters,")
print ("- At least 1 lowercase and uppercase letter,")
print ("- At least 1 integer number,")
print ("- At least 1 special character.")
entry()
