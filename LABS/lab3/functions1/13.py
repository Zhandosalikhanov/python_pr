from random import randint

def Guessing_game():
    Name = input("Hello! What is your name?" + "\n")
    print("\n" + "Well,", Name, ", I am thinking of a number between 1 and 20.")

    guess = 0
    trials = 0
    rand = randint(1, 20)

    while guess != rand:
        guess = int(input("Take a guess." + "\n"))

        if guess > rand:
            print("\n" + "Your guess is to high.")
        elif guess < rand:
            print("\n" + "Your guess is to low.")
        
        trials += 1
    else:
        if(trials < 3):
            print("Very good job,", Name, "You guessed my number in only", trials, "guesses!")
        elif(trials < 6):
            print("Bad job,", Name, "You guessed my number in", trials, "guesses!")
        else:
            print("Very, very bad job, " + Name + "! It takes you", trials, "trials to guess a single number")