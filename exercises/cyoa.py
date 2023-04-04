"""EX06 - Create your own adventure."""
import random
__author__ = "730551547"
player: str = ""
randomnumber: int = random.randint(0, 0)
global points
points: int
EMOJI: str = "\U0001F973"


def greet() -> None:
    """Prints a welcome message for context and asks for name."""
    print("For this game, the player will enter a number and the game will generate a random number between one and the number that the player picked. The game then records the number of times that it takes the player to guess this number.")
    player: str = input("What is your name? ")
    print(f"Hello, {player}")


def guess() -> None: 
    """Gives the bound for which the number is generated between."""
    bound = input(f"Hello, {player} The random number generator will generate a number between 1 and which number? ")
    global randomnumber
    randomnumber = random.randint(1, int(bound))
    guessnum = 6
    global usedguess
    global pointcount
    usedguess = 1
    while (usedguess < guessnum):
        match = input(f"Guess the random number between 1 and {bound} ")
        if (int(match) == int(randomnumber)):
            print(f"You guessed the number, number of tries: {usedguess} ")
            guessnum = 0
        else:
            usedguess = usedguess + 1
            print("That is wrong try again")
    evenorodd = input("Guess if the number is even or odd. Type 1 for even and 2 for odd ")
    if ((randomnumber % 2 == 0) and (int(evenorodd) == 1)):
        print("You are correct. The number is even")
        pointcount = 20
    elif ((randomnumber % 2 == 1) and (int(evenorodd) == 2)):
        print("You are correct. The number is odd")
        pointcount = 20
    else:
        pointcount = 0


def point(points: int) -> int:
    """Track points."""
    i = 0
    while i <= usedguess:
        if (usedguess == i):
            print(f"Player{player} has this many points: {points + pointcount} ")
            print(f"{EMOJI}")
            return points
        else:
            i = i + 1
            points += -10


def main() -> None:
    """The entrypoint of the program and where it begins."""
    greet()
    guess()
    pointcounter: int = 50
    point(pointcounter)


if __name__ == "__main__":
    main()