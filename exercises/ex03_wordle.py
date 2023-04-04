"""EX03 - Structured Wordle."""
__author__ = "730551547"


def contains_char(searchword: str, charsearch: str) -> bool:
    """Looks through a word and sees if a letter is in a word."""
    assert len(charsearch) == 1
    letter = 0
    check = True
    differentplace = True
    while check:
        if (searchword[letter] == charsearch):
            check = False
            return True
        else:
            while differentplace:
                if (searchword[letter] != charsearch):
                    if (letter == (len(searchword) - 1)):
                        differentplace = False
                        check = False
                        return False
                    letter = letter + 1
                else:
                    differentplace = False
                    check = False
                    return True    

     
def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis with codified colors."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    guessletter = 0
    emoji = ""
    while (guessletter < len(guess)):
        checkletter = contains_char(secret, guess[guessletter])
        if (checkletter is False):
            emoji = emoji + WHITE_BOX
        if (checkletter is True):
            if (secret[guessletter] == guess[guessletter]):
                emoji = emoji + GREEN_BOX
            else:
                emoji = emoji + YELLOW_BOX
        guessletter = guessletter + 1
    return emoji


def input_guess(expectedlength: int) -> str:
    """Takes input and checks length."""
    length = True
    wordguess = ""
    wordguess = input(f"Enter a {expectedlength} character word: ")
    while length:
        if (len(wordguess) != expectedlength):
            wordguess = input(f"That wasn't {expectedlength} chars! Try again: ")
        else:
            length = False
            return wordguess

        
def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secretword = "codes"
    secretlength = len(secretword)
    turn = 1
    greenemoji = ""
    greenindex = 0
    GREEN_BOX: str = "\U0001F7E9"
    while (greenindex < secretlength):
        greenemoji = greenemoji + GREEN_BOX
        greenindex = greenindex + 1
    turncount = True
    while ((turncount is True and turn < 7)):
        print(f"=== Turn {turn}/6 ===")
        guessword = input_guess(secretlength)
        emojilist = emojified(guessword, secretword)
        print(emojilist)
        if (emojilist == greenemoji):
            print(f"You won in {turn}/6 turn!")
            turncount = False
        else:
            turn = turn + 1
            if (turn == 7):
                print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()