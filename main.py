# main.py
# Daniel Wolff
# 10/21/2015

from logic import Logic

SCREEN_SIZE = (400, 400)
SCREEN_CAPTION = "SSS Testing"

def main() :
    env = Logic(SCREEN_SIZE, SCREEN_CAPTION)
    env.run()

main()

