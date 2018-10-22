import random
import numpy as np



PLATFORMS = [(np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)]

GOAL = (np.random.randint(-301,301,1)

def paintPlatforms():
    penWidth(8)
    setPenColor(makeColor("sky blue"))
    for x_left, x_right, height in PLATFORMS:
        y = GROUNDLEVEL + height - 5
        setPos(x_left, y)
        moveTo(x_right, y)
