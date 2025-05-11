"""
File: Steeplechase.py
Name: 馮令彝
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def up():
    """
    per-condition: Karel is on the left side of the wall, facing East
    post-condition: Karel is on the upper left of the wall, facing North
    """
    turn_left()
    while not right_is_clear():
        move()
    #alternative
    #while not front_is_clear():
    #   turn_left()
    #   move()
    #   turn_right()


def cross():
    """
        per-condition: Karel is on the upper left of the wall, facing North
        post-condition: Karel is on the upper right of the wall, facing Sorth
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    per-condition:Karel is on the upper right of the wall, facing Sorth
    post-condition: Karel is on the upper right of the wall, facing East
    """
    while front_is_clear():
        move()
    turn_left()


def jump():
    """
    per-condition: Karel is on the left side of the wall, facing East
    post-condition: Karel is on the right side of the wall
    """
    up()
    cross()
    down()

def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """



    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
