# password-strength is licensed under the GNU Public License v3.0
# Copyright (c) 2021 tlegx
# This program comes with NO warranty or credibility whatsoever. Use this at your own risk.

# Imports
import readchar
import sys
import utils
import check
from getpass import getpass


# Welcome screen
def main():
    utils.clear_screen()
    print("===== password-strength =====")
    print(
        "Simply enter your password and we will check it against multiple standards to see if your password is safe in this internet era.")
    print("This process is completely OFFLINE and PRIVATE. You can check the source code of this program if you want.")
    print("[S]tart/[C]redits/[E]xit")
    mainchoice = readchar.readkey()
    if mainchoice == "s" or mainchoice == "S":
        reqpassword()
    elif mainchoice == "c" or mainchoice == "C":
        credits()
    elif mainchoice == "e" or mainchoice == "E":
        sys.exit()
    else:
        main()


# Credits screen
def credits():
    utils.clear_screen()
    print("===== password-strength =====")
    print("Licensed under the GNU Public License v3.0")
    print("Copyright (c) 2021 tlegx. All rights reserved.")
    print("For more information, please visit https://github.com/tlegx/password-strength")
    print("Press any key to return to the main screen.")
    readchar.readkey()
    main()


def reqpassword():
    utils.clear_screen()
    password = getpass('Please enter the password you want to check: ')
    check.main(password)


if __name__ == '__main__':
    main()
