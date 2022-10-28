from random import randint; print("----------------\nNUMBER WANG\n----------------"); wang_found = False
while wang_found == False and input("guess: "): print("THATS NUMBER WANG"); wang_found = True if randint(1, 2) == 1 else print("that is not number wang")
