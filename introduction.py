import time
import os
import printing_effects

def startup():
    #playsound('Audio/01.mp3',False)

    print("██░ ██ ▓█████  ██▓     ██▓     ▒█████      █     █░ ▒█████   ██▓     ██▀███  ▓█████▄  ")
    time.sleep(0.7)
    print("▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ▒██▒  ██▒   ▓█░ █ ░█░▒██▒  ██▒▓██▒    ▓██ ▒ ██▒▒██▀ ██▌")
    time.sleep(0.15)
    print("▒██▀▀██░▒███   ▒██░    ▒██░    ▒██░  ██▒   ▒█░ █ ░█ ▒██░  ██▒▒██░    ▓██ ░▄█ ▒░██   █▌")
    time.sleep(0.1)
    print("░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    ▒██   ██░   ░█░ █ ░█ ▒██   ██░▒██░    ▒██▀▀█▄  ░▓█▄   ▌")
    time.sleep(1)
    print("░▓█▒░██▓░▒████▒░██████▒░██████▒░ ████▓▒░   ░░██▒██▓ ░ ████▓▒░░██████▒░██▓ ▒██▒░▒████▓ ")
    time.sleep(0.55)
    print(" ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░░ ▒░▒░▒░    ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ")
    time.sleep(0.33)
    print(" ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░  ░ ▒ ▒░      ▒ ░ ░    ░ ▒ ▒░ ░ ░ ▒  ░  ░▒ ░ ▒░ ░ ▒  ▒ ")
    time.sleep(0.25)
    print(" ░  ░░ ░   ░     ░ ░     ░ ░   ░ ░ ░ ▒       ░   ░  ░ ░ ░ ▒    ░ ░     ░░   ░  ░ ░  ░ ")
    time.sleep(0.17)
    print(" ░  ░  ░   ░  ░    ░  ░    ░  ░    ░ ░         ░        ░ ░      ░  ░   ░        ░    ")
    time.sleep(0.1)
    print("                                                                               ░      ")
    time.sleep(2)
    
    printing_effects.delay_print("Get ready to embark on a new experience!\n", 0.02)
    time.sleep(2)
    printing_effects.delay_print("The game is going to start soon... you might be next to play.\n", 0.015)
    time.sleep(5)
    
    os.system('cls') # It clears the screen from anything printed. It won't work for the ipython console.
    
def introduction():
    print("NOT DONE")


startup()