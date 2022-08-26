import random

def pythonsay(txt, big = False):
    
    print(f"\n\n< {txt} >")
    print(f" {'_' * len(txt) if len(txt) < 54 else '_' * 54}")
    print("          \\")
    print("           \\      /^\\/^\\")
    print("            \   _|_O|  O|")
    print("        \\/     /~     \\_/ \\")
    print("         \\____|__________/  \\")
    print("               \\_______      \\")
    print("                       `\\     \\                 \\")
    print("                        /     /                  \\")
    print("                      /     /                    \\")
    print("                    /     /                       \\\\")
    if not big:
        print("                   /     /                         \\ \\\n\n")
    if big:
        print("                   /     /                         \\ \\")
        print("                  /     /                            \\  \\")
        print("                 /     /             _----_            \\   \\")
        print("                /     /           _-~      ~-_         |   |")
        print("               (      (        _-~    _--_    ~-_     _/   |")
        print("                \\      ~-____-~    _-~    ~-_    ~-_-~    /")
        print("                 ~-_           _-~          ~-_       _-~")
        print("                    ~--______-~                ~-___-~\n\n")

    
    
def cowsay(txt):
    """Prints a cow saying the given text"""
    
    print(f"\n\n< {txt} >")
    print(f" {'_' * len(txt) if len(txt) < 54 else '_' * 54}")
    print("      \   ^__^     ")
    print("       \  (oo)\_______")
    print("          (__)\        )\\/\\")
    print("           U   ||----w |")
    print("               ||     ||\n\n")


def random_cow_prases():
    """Returns a random phrase from the list of phrases"""

    phrases = [
        "Go Vegan!",
        "I'm not your mother!",
        "Not your mom, not your milk!" "Vegan Revolution!",
        "Cow’s milk is for baby cows!",
        "Stop stealing my milk!",
        "I'm not a milk machine!",
    ]
    return random.choice(phrases)

def random_python_prases():
    """Returns a random phrase from the list of phrases"""

    phrases = [
        "Beautiful code is better than ugly code",
        "C: Combines the power of assembly language with the \nreadability and maintainability of assembly language.",
        "If you don't know how to program, do it in Python!",
        "There are always a library for that!",
        "Python is the best language! (if you have time to wait)",
        "Automate everything!",
        "Python is the best language! (if you have enough memory to leak)",
        "Constants??? What is it?",
        "1 + 1 = 11",
        "is True? is not False!",
        "You can't do that in Python! joking, you can :)",
        "Best about Python, you just need to import it!"
    ]
    return random.choice(phrases)