import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Sachin")
    x = input("Enteer What you want me to speak: ")
    command = f"say{x}"
    os.system(command)
