"""
File: PotholeFilling.py
Name: 馮郁宸
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *
def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole, facing East
    post-condition:Karel is in the pothole, facing South
    """
    move()
    turn_right()
    move()
def go_out():
    """
    pre-condition:Karel is in the pothole, facing South
    post-condition:Karel is at the upper right of the pothole, facing East
    """
    turn_right()
    turn_right()
    move()
    turn_right()
    move()
def main():
    """
    TODO:
    """
    pass
    for i in range(3):
        go_in()
        put_beeper99()
        go_out()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
