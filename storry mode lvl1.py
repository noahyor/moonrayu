from time import sleep # imports the function "sleep()" (from time) witch takes a floting point intiger inside the paretheses as input and suspends the program for that amount of time in seconds.
from time import localtime # imports the function "localtime()" witch prints (not on the screen) the current time in your time zone. see lines 25-27 for exampels.
# empty line. I don't know why this is here
typeronof = str(input('''typer on/off option 
boolian valeues only
True = on
False = off
off recomended for eager people
''')) # that was a triple qwoted string
if typeronof == "True": # TODO: add strings like, "O.K" or "shure!" to if statement block.
    string = "Welcome to this program... or... well... I'm more of an AI than a program. but, wait, aren't AI's made of\n"
    caracternum = 0
    for letter in string: # FIXME: printing ticker could work better and faster in C++.
        caracternum += 1
        print(letter, end="", flush=True)
        if caracternum == 26 or caracternum == 33 or caracternum == 42 or caracternum == 82 or caracternum == 88:
            sleep(1.8)
        else:
            sleep(0.4)
    string = "programs? anyways, let's start lerning!\n"
    caracternum = 0
    for letter in string:
        caracternum += 1
        print(letter, end="", flush=True)
        if caracternum == 9 or caracternum == 18:
            sleep(1.8)
        else:
            sleep(0.4)
    string = "first of all, what is your name? "
    caracternum = 0
    for letter in string:
        caracternum += 1
        print(letter, end="", flush=True)
        if caracternum == 13:
            sleep(1.8)
        else:
            sleep(0.4)
    name = input()
else:
    print("Welcome to this program... or... well... I'm more of an AI than a program. but, wait, aren't AI's made of")
    print("programs? anyways, let's start lerning!")
    name = input("first of all, what is your name? ")
    print(f"hmm... {name}... good name!")
    print("OK enough of that, let's start!") # TODO: tweak time limitation.
t = localtime()
if not t[3] >= 7 and t[3] <= 19:
    sleep(5)
    if typeronof == "True" or "true":
        string = "wait a... you are not alloud in this program!\n"
        caracternum = 0
        for letter in string:
            caracternum += 1
            print(letter, end="", flush=True)
            if caracternum == 9:
                sleep(1.0)
            else:
                sleep(0.3)
    else:
        print('''wait a... you are not alloud in this program!
        our hours are as follows:
        mon-son: 8am-8pm''')
else:
    print("test")
