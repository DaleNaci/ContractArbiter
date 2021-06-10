from getpass import getpass


d = {
    "spy": "spy",
    "p": "private",
    "serg": "sergeant",
    "2l": "2nd lieutenant",
    "1l": "1st lieutenant",
    "capt": "captain",
    "m": "major",
    "lc": "lieutenant colonel",
    "col": "colonel",
    "1g": "1 star general",
    "2g": "2 star general",
    "3g": "3 star general",
    "4g": "4 star general",
    "5g": "5 star general"
}


while True:
    while True:
        p1 = getpass("Attacking: ")
        if p1 == "q":
            break

        if p1 not in d.keys():
            print("Invalid game piece")
        else:
            break

    if p1 == "q":
        break

    while True:
        p2 = getpass("Defending: ")
        if p2 == "q":
            break

        if p2 not in d.keys():
            print("Invalid game piece")
        else:
             break

    if p2 == "q":
        break

    print(f"Attacking: {d[p1]}")
    print(f"Defending: {d[p2]}")
