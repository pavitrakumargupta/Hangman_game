import random
from time import sleep
from hangman_art import stages, logo
from replit import clear

word_list = ["killer", "mudrer", "arrseted", "police"]
chosen_word = random.choice(word_list)
list_of_chosen_word = []
lives = len(stages) - 1

Time = len(chosen_word)
while Time >= 0:
    print(
        "this is a hanman game and you have fill all the blanks with words and you have",
        lives, "lives to fill this")
    print("your game will starts in --->>", end="  ")
    print(Time)
    Time -= 1
    sleep(2)
    clear()

for i in range(0, len(chosen_word)):
    list_of_chosen_word.extend("_")

listing_word = []

for k in chosen_word:
    listing_word.extend(k)
print(logo)
print(stages[0])
i = 1
while i < len(chosen_word):
    print(list_of_chosen_word)
    if "_" not in list_of_chosen_word:
        break
    guess = input("guess a letter :-  ").lower()
    clear()
    if guess in list_of_chosen_word:
        print("you have repeated")
        continue
    elif guess in listing_word:
        for j in range(0, len(chosen_word)):
            if guess == listing_word[j]:
                list_of_chosen_word[j] = guess
            else:
                continue
        print(logo)
        print(stages[0])
        print(stages[lives])
        print("yes you guessed a right letter", guess)
        print("your total life", lives)
    else:
        print(logo)
        print(stages[0])
        print(stages[lives])
        lives -= 1
        print(
            "you chosen a wrong one you have losed a life now total life you have",
            lives)
clear()
print("ops there is somthing terrifying in your result")
print("please wait until your result declares.....")
sleep(5)
if "_" in list_of_chosen_word:
    print(stages[0])
    print("you lost bcz you didn't complete this chalenge in",
          len(chosen_word), "lives")
else:
    print(stages[-1])
    print("you win congratulation hangman wasn't hanged he was saved by you")