from random import randint; print("----------------\nNUMBER WANG\n----------------"); wang_found = False
while wang_found == False and input("guess: "): 
    if randint(1, 2) == 1: print("THATS NUMBER WANG"); wang_found = True 
    else: print("that is not number wang")
