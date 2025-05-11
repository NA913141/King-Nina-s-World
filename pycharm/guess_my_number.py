"""
File: guess_my_number.py
Name:馮令彝
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
SECRET = 32


def main():
    print("猜 0-99")
    while True:
        guess = int(input('請猜:'))
        if guess == SECRET:
            break
        elif guess < SECRET:
            print('太低')
        else:
            print('太高')
    print('Congrats! The answer: ' + str(SECRET))














    # guess = int(input('請猜:'))
    # while guess != SECRET:
    #     if guess > SECRET:
    #         print("太高")
    #     else:
    #         print('太低')
    #     guess = int(input('請猜:'))
    # print('恭喜!答案:' + str(SECRET))

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
