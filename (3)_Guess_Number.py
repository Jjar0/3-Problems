import random

def main():
    goal = random.randint(1,100) #creating random number between 1-100.

    start = input ("enter 'start' to begin a new game.\n>")

    while start != "start":
        start = input ("enter 'start' to begin a new game.\n>")
    if start == "start":
        game(goal)

def game(goal):

    counter = 0
    guess = ""

    while guess != goal: #game is contained in loop to iterate the guess counter.

        counter = counter + 1 #iterate guess counter every faliure.

        print ("Guess the number!")

        while True:
            try:
                guess = int(input(">")) #input validation for digits.
                if guess > 100 or guess < 1:
                    raise
                break
            except:
                print ("please enter a number!")
                counter-1
                continue
        
        guess = int(guess)

        if guess > goal:
            print ("lower!") #tells user if they need to guess higher/lower.
            continue

        if guess < goal:
            print ("higher!")
            continue

    answer = str(goal)
    attempts = str(counter)

    print ("\nCorrect!")
    print ("The number was " + answer) #tell player how many guesses it took to win.
    print ("it took you "+attempts+" guesses to win.\n")
    main()


print ("Welcome to the number guessing game,")
print ("A random number has been generated and you must guess the number,")
print ("The number is between 1-100,")
main()
