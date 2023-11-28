import random

def main():
    goal = random.randint(1,100)

    start = input ("enter 'start' to begin a new game.\n>")

    while start != "start":
        start = input ("enter 'start' to begin a new game.\n>")
    if start == "start":
        game(goal)

def game(goal):

    counter = 0
    guess = ""

    while guess != goal:

        counter = counter + 1

        print ("Guess the number!")

        while True:
            try:
                guess = int(input(">"))
                break
            except:
                print ("please enter a number!")
                continue
        
        guess = int(guess)

        if guess > goal:
            print ("lower!")
            continue

        if guess < goal:
            print ("higher!")
            continue

    answer = str(goal)
    attempts = str(counter)

    print ("\nCorrect!")
    print ("The number was " + answer)
    print ("it took you "+attempts+" guesses to win.\n")
    main()


print ("Welcome to the number guessing game,")
print ("A random number has been generated and you must guess the number,")
print ("The number is between 1-100,")
main()