import re
from os import system, name 
from time import sleep 
opers = name
def clear(): 
        # for windows 
    if opers == 'nt': 
        _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
clear()
while True:
    print("\n")
    print("██████╗ ██╗   ██╗███╗   ███╗ █████╗ ██╗██╗     ")
    print("██╔══██╗╚██╗ ██╔╝████╗ ████║██╔══██╗██║██║     ")
    print("██████╔╝ ╚████╔╝ ██╔████╔██║███████║██║██║     ")
    print("██╔═══╝   ╚██╔╝  ██║╚██╔╝██║██╔══██║██║██║     ")
    print("██║        ██║   ██║ ╚═╝ ██║██║  ██║██║███████╗")
    print("╚═╝        ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝")                                             
    print("\n")
    name = input("Enter a email inbox file:")
    ranking = input("Enter a ranking max (ex: 10 = top 10 emailers):")
    if len(name) < 1 : print("[Error] No file selected.")
    if len(ranking) < 1 : print("[Error] No number of top selected, at least 1.")
    try:
        ranking = int(ranking)
    except: 
        print("[Error] No integrer number entered:", name)
        break
    try:
        handle = open(name, encoding="utf8")
    except:
        print("[Error] No file fonund called:", name)
        break
    print('[OK] File oppened successfully')
    print('[OK] Number entered correct')
    print("[WAIT] Scanning... This can take a while...")
    top = dict()   
    counter = 0 
    for line in handle:
        if not line.startswith("From:") : continue        
        x = re.findall('[a-zA-Z0-9\-.]\S+@[a-zA-Z0-9].\S+[a-zA-Z]', line)
        for email in x:
            counter = counter +1
            top[email] = top.get(email, 0) + 1
    lst = list()
    for key, val in top.items():
        newtup = (val, key)
        lst.append(newtup)
    lst = sorted(lst, reverse=True)

    rankedlst = lst[:ranking]
    print("[FOUND] Found", counter, "emails received.")
    print("\n")
    print("* [RESULT] Theese are the most emailers to you :)")
    rank = 0
    
    for val, key in rankedlst:
        space = ""
        rank = rank + 1
        spacestodo = 45 - int(len(key))
        
        for numbers in range(spacestodo):
            space = space + " "
            
        print("TOP", rank, ": ", key, space, " sent you: ", val, " emails")

    print("[OK] Scan done :)")
    print()
    system('pause')
    clear()