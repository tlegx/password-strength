# Check file for password-strength

# Imports
import utils
import re


def main(password):
    utils.clear_screen()
    print("Please wait, we are checking your password...")
    print("\nYour password...")
    score = 0
    chklen(password, score)


def chklen(password, score):
    if len(password) >= 8:
        print("- is made of 8 or more characters: passed")
        score += 1
    else:
        print("- is made of 8 or more characters: failed")
    chkuplowandnum(password, score)


def chkuplowandnum(password, score):
    containsupper = "failed"
    containsnumber = "failed"
    containslower = "failed"
    for element in password:
        if element.isupper():
            containsupper = "passed"
            score += 1
            break
    for element in password:
        if element.isdigit():
            containsnumber = "passed"
            score += 1
            break
    for element in password:
        if element.islower():
            containslower = "passed"
            score += 1
            break
    print(f"- contains at least 1 uppercase character: {containsupper}")
    print(f"- contains at least 1 lowercase character: {containslower}")
    print(f"- contains at least 1 number: {containsnumber}")
    chkspec(password, score)


def chkspec(password, score):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(password) is None:
        print(f"- contains at least 1 special character: failed")
    else:
        print(f"- contains at least 1 special character: passed")
        score += 1
    chkcommon(password, score)


def chkcommon(password, score):
    try:
        f = open("vuln.txt", "r")
        for lines in f:
            if lines == password:
                print("- is not in the database of common passwords: failed")
                break
        print("- is not in the database of common passwords: passed")
        f.close()
        score += 1
    except:
        print("- is not in the database of common password: [cannot find vuln.txt, this test was ignored]")
    results(score)


def results(score):
    print(f"Your password score: {score}/6")
    if score < 6:
        print("Your password did not pass our 6 tests, which means it's not secure. Mind looking at ways to improve it?")
    else:
        print("Congratulations! Your password passed our 6 tests, which means it is most likely secure. However, some other factors might lead to it not being secure anymore.")