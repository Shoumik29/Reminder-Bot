from pygame import *
from time import *

Initialsec = time()
print("Welcome to the Reminder Program")
print("You will be notified for: ")
print("1. Drinking Water\n2. Eye Exercise\n3. Physical Exercise")


while True:
    currentsec = time()
    mixer.init()

    if int(currentsec-Initialsec) == 900:
        mixer.music.load("eye.mp3")
        mixer.music.set_volume(4)
        mixer.music.play(-1)
        while True:
            ans = input("If your done then type done: ")
            if ans == "done":
                print("Thanks Mr.Shoumik for your response. Eye exercise Done!!!")
                mixer.music.stop()
                Initialsec = time()
                f = open("Shoumik.txt", "a")
                f.write(f"Eye Exercise-{ctime(Initialsec)}\n\n")
                f.close()
                while True:
                    currentsec = time()
                    if int(currentsec - Initialsec) == 600:
                        mixer.music.load("pani.mp3")
                        mixer.music.set_volume(4)
                        mixer.music.play(-1)
                        while True:
                            ans = input("If your done then type done: ")
                            if ans == "done":
                                print("Thanks Mr.Shoumik for your response. Drinking Water Done!!!")
                                mixer.music.stop()
                                Initialsec = time()
                                f = open("Shoumik.txt", "a")
                                f.write(f"Water Drinking-{ctime(Initialsec)}\n\n")
                                f.close()
                                while True:
                                    currentsec = time()
                                    if int(currentsec - Initialsec) == 600:
                                        mixer.music.load("physical.mp3")
                                        mixer.music.set_volume(4)
                                        mixer.music.play(-1)
                                        while True :
                                            ans = input("If your done then type done: ")
                                            if ans == "done":
                                                print("Thanks Mr.Shoumik for your response. Physical exercise done!!!")
                                                mixer.music.stop()
                                                Initialsec = time()
                                                f = open("Shoumik.txt", "a")
                                                f.write(f"Physical Exercise-{ctime(Initialsec)}\n\n")
                                                f.close()
                                                break
                                        break
                                break
                        break
                break