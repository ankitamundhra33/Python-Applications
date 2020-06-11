#this is hangman game
import random

def hangman():
    movies = random.choice(["3|idiots", "lagaan", "jab|we|met", "sholay", "dil|chahta|hai", "queen", "zindagi|na|milegi|dobara", "dangal", "the|lunchbox", "barfi", "andaz|apna|apna", "hum|aapke|hain|koun", "kahaani", "haider", "gangs|of|wasseypur", "anand",
              "rang|de|basanti", "swades", "a|wednesday", "special|26", "black|friday", "bhaag|milkha|bhaag", "paan|singh|tomar", "drishyam", "guru", "baby", "yeh|jawaani|hai|deewani" ,"pk", "my|name|is|khan", "angrezi|medium", "baaghi|3", "tanhaji",
                "good|newwz", "war", "article|15", "kabir|singh", "kesari", "badla", "gully|boy", "uri", "badhaai|ho", "andhadhun", "stree", "sanju", "padman", "pink", "udta|punjab"])
    validLetters = 'qwertyuiopasdfghjklzxcvbnm023456789|'
    guessmade = ''
    turns = 10
    length = len(movies.split("|"))
    print("The movie has total " + str(length) + " words.")
    print("Hint: Please enter | first for multiple words")

    while len(movies) > 0:
        main = ""

        for letter in movies:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == movies:
            print(main)
            print("Congratulations!")
            break

        print("Guess the movie: ", main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character!")
            guess = input()

        if guess not in movies:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("   -------   ")
            if turns == 8:
                print("8 turns left")
                print("   -------   ")
                print("      O      ")
            if turns == 7:
                print("7 turns left")
                print("   -------   ")
                print("      O      ")
                print("      |      ")
            if turns == 6:
                print("6 turns left")
                print("   -------   ")
                print("      O      ")
                print("      |      ")
                print("     /       ")
            if turns == 5:
                print("5 turns left")
                print("   -------   ")
                print("      O      ")
                print("      |      ")
                print("     / \     ")
            if turns == 4:
                print("4 turns left")
                print("   -------   ")
                print("    \ O      ")
                print("      |      ")
                print("     / \     ")
            if turns == 3:
                print("3 turns left")
                print("   -------   ")
                print("    \ O /    ")
                print("      |      ")
                print("     / \     ")
            if turns == 2:
                print("2 turns left")
                print("   -------   ")
                print("    \ O / |  ")
                print("      |      ")
                print("     / \     ")
            if turns == 1:
                print("Last few breathes counting!")
                print("   -------   ")
                print("    \ O /_|  ")
                print("      |      ")
                print("     / \     ")
            if turns == 0:
                print("Dead! You lose")
                print("   -------   ")
                print("      O_|    ")
                print("    / | \    ")
                print("     / \     ")
                break


name=input("Please enter your name: ")
print("Welcome ", name)
print("\nTry to guess the name of Bollywood Movie before the man dies!\n")
hangman()