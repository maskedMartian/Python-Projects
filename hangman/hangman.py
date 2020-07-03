# hangman game
# author: maskedMartian
# date: 2-28-2020

# ==================================== imports ====================================
import random

# =================================== constants ===================================
MAX = 40
SPACE = "              "

# =============================== global variables ================================
wordList = (
    "Indiana", "Michigan", "Iowa", "Illinois", "Maine", "computer", "lawnchair", "lightbulb", 
    "blanket", "sodapop", "Tennesee", "Missippi", "Texas", "Alaska", "Florida", "airplane",
    "television", "forrest", "girlfriend", "tractor", "watch", "vacuum", "Internet", "fireplace",
    "counter", "cupboard", "table", "workbook", "microwave", "arcade", "snowman", "Wisconsin",
    "birthday","toothpaste", "toilet", "freezer", "portrait", "carpet", "hangman", "forty"
)

# ==================================== classes ====================================
class HangingMan:
    BODY = ("O", "|_|", "/", "\\", "_/", "\\_")

    def __init__(self):
        self.qtyParts = 0
        self.display = [" ", "   ", " ", " ", "  ", "  "]

    def draw(self):
        print(SPACE + "       ______")
        print(SPACE + "       |    |")
        print(SPACE + "       " + self.display[0] + "    |")
        print(SPACE + "     " + self.display[2] + self.display[1] + self.display[3] + "  |")
        print(SPACE + "     " + self.display[4] + " " + self.display[5] + "  |")
        print(SPACE + "            |")
        print(SPACE + "   _________|")  
        print()

    def addBodyPart(self):
        if self.qtyParts < 6:
            self.display[self.qtyParts] = self.BODY[self.qtyParts]
            self.qtyParts += 1

    def checkLoss(self):
        if self.qtyParts > 5:
            print(SPACE + "  YOU LOST :(")
            print()
            return True
        return False

# ---------------------------------------------------------------------------------
class SecretWord:
    displayWord = ""

    def __init__(self):
        self.word = wordList[random.randrange(MAX)]
        for _i in range(len(self.word)):
            self.displayWord = self.displayWord + "*"

    def checkGuess(self, guess):
        return guess.upper() in self.word or guess.lower() in self.word

    def printWord(self):
        print(SPACE + "WORD: " + self.displayWord)

    def revealLetter(self, letter):
        for i in range(len(self.word)):
            if self.word[i].upper() == letter.upper():
                self.displayWord = self.displayWord[:i] + self.word[i] + self.displayWord[i + 1:]

    def checkWin(self):
        if not "*" in self.displayWord:
            print(SPACE + "    YOU WON!")
            print()
            return True
        return False

    def revealWord(self):
        print(" The word is: " + self.word)
        print()

# ---------------------------------------------------------------------------------
class GuessedLetters:
    guessedLetters = ""

    def printGuessedLetters(self):
        print(SPACE + "GUESSED LETTERS:")
        print(SPACE, end = "")
        for i in range(len(self.guessedLetters)):
            print(self.guessedLetters[i] + " ", end = "")
        print()
        if (len(self.guessedLetters)):
            print()

    def checkLetter(self, letter):
        return letter in self.guessedLetters

    def addLetter(self, letter):
        self.guessedLetters += letter.lower()

# ---------------------------------------------------------------------------------
class IoManager:
    guess = ""
    choice = ""

    def getGuess(self):
        self.guess = ""
        while not self.guess.isalpha():
            self.guess = input(" Enter your guess (a-z): ")
            if len(self.guess) > 1:
                self.guess = ""
                print(" Please enter only a single character.")
            elif not self.guess.isalpha():
                self.guess = ""
                print(" Please enter a letter of the alphabet.")
        return self.guess

    def playAgain(self):
        self.choice = ""
        while self.choice.upper() != "Y" and self.choice.upper() != "N":
            self.choice = input(" Want to play again? (y/n) ")
            if self.choice.upper() != "Y" and self.choice.upper() != "N":
                print(" Please enter only y or n.")
        print()
        return True if self.choice.upper() == "Y" else False

    def clearScreen(self):
        for _i in range(50):
            print()

    def gameTitle(self):
        print()
        print(" -------------------------------------------")
        print(" |                                         |")
        print(" |             -- HANGMAN --               |")
        print(" |                                         |")
        print(" -------------------------------------------")
        print()

    def gameIntro(self):
        print(" Let's play...")
        print()

    def thanks(self):
        print("          -- THANKS FOR PLAYING! --")

# ---------------------------------------------------------------------------------
# HangingMan:
    # draw()
    # addBodyPart()
    # checkLoss()
# SecretWord:
    # checkGuess(guess)
    # printWord()
    # revealLetter(letter)
    # checkWin()
    # revealWord()
# GuessedLetters:
    # printGuessedLetters()
    # checkLetter(letter)
    # addLetter(letter)
# IoManager:
    # getGuess()
    # playAgain()
    # clearScreen()
    # gameTitle()
    # gameIntro()

# =================================== functions ===================================
def main():
    io = IoManager()
    io.clearScreen()
    io.gameTitle()
    io.gameIntro()
    while 1:
        sw = SecretWord()
        random.seed()
        gl = GuessedLetters()
        hm = HangingMan()
        while 1:
            sw.printWord()
            hm.draw()
            gl.printGuessedLetters()
            if sw.checkWin():
                break
            elif hm.checkLoss():
                sw.revealWord()
                break
            io.getGuess()
            if not gl.checkLetter(io.guess):
                gl.addLetter(io.guess)
                if not sw.checkGuess(io.guess):
                    hm.addBodyPart()
            if sw.checkGuess(io.guess):
                sw.revealLetter(io.guess)
            io.clearScreen()
            io.gameTitle()
        if not io.playAgain():
            io.thanks()
            break
        else:
            io.clearScreen()
            io.gameTitle()
            io.gameIntro()
    print()
    print()

# ---------------------------------------------------------------------------------
main()