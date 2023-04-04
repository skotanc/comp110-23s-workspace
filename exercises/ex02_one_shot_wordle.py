"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730551547"
secretword = "python"
playing: bool = True
yellow: bool = False
lenguess = len(secretword)
guess: str = input(f"What is your {lenguess}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
letter = 0
secretletter = 0
emoji = ""
while playing:
    if (len(guess) != len(secretword)):
        guess = input(f"That was not {lenguess} letters! Try again: ")
    if (len(guess) == len(secretword)):
        playing = False
        while (letter < len(secretword)):
            if (guess[letter] == secretword[letter]):
                emoji = emoji + GREEN_BOX
            else:
                    yellow = True
                    secretletter = 0
                    while (yellow and secretletter < len (secretword)):
                        if (guess[letter] != secretword [secretletter]):
                            secretletter = secretletter + 1
                        else:
                            emoji = emoji + YELLOW_BOX
                            secretletter = secretletter + 1
                            yellow = False                                
                    if (secretletter == len(secretword) and yellow):
                        emoji = emoji + WHITE_BOX
            if (letter == len(secretword)-1):
                print(emoji)
            letter = letter + 1
if (guess == secretword):
    print("Woo! You got it!")
    playing = False
if (guess != secretword):
    print("Not quite. Play again soon!")
    playing = False
