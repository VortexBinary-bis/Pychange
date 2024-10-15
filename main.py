from pythonchangeversion import PyVersionManager as pvm # type: ignore
from colors import Color as c # type: ignore

# Introduction
print(c.set(62)+ """__________ _____.___._________    ___ ___     _____    _______     ________ ___________
\\______   \\\\__  |   |\\_   ___ \\  /   |   \\   /  _  \\   \\      \\   /  _____/ \\_   _____/
 |     ___/ /   |   |/    \\  \\/ /    ~    \\ /  /_\\  \\  /   |   \\ /   \\  ___  |    __)_ 
 |    |     \\____   |\\     \\____\\    Y    //    |    \\/    |    \\\\    \\_\\  \\ |        \\
 |____|     / ______| \\______  / \\___|_  / \\____|__  /\\____|__  / \\______  //_______  /
            \\/               \\/        \\/          \\/         \\/         \\/         \\/ """,c.set(238),"Coded by kipruun")
print(c.set(255),"\nThis project permite us to change in path python version, to install version, to remove version.")
print("    1.",c.set(62),"Install",c.set(255),"version\n    2.",c.set(62),"Remove",c.set(255),"version\n    3. Set",c.set(62),"default",c.set(255),"version\n    4. Get",c.set(62),"default",c.set(255),"version\n    5.",c.set(62),"List",c.set(255),"versions")
while True:
    userChoice = input(" > ")
    if userChoice == "q":
        break
    
    try:
        userChoice = int(userChoice)
        if userChoice == 1:
            pass
        elif userChoice == 2:
            pass
        elif userChoice == 3:
            pvm.set_default_version()
        elif userChoice == 4:
            print(pvm.get_default_v())
        elif userChoice == 5:
            for i in pvm.get_versions()[0] : print("Python",i)
        else:
            print(c.set(196)+"Error : Numeral valor not allowed",c.set(255))
    except:
        print(c.set(196)+"Error : Not a numeral valor",c.set(255))
