
from gtts import gTTS
import random
import math


x=0
def listen_command():
    return input("Команда: ")

def do_this_command(message):
    message = message.lower()

    if "привет" in message:
        say_message ("Привет друг")
    elif "пока" in message:
        say_message("Пока")
        exit()

    elif "будильник" in message:
        import alarm

    elif "вычислить" in message:
        say_going= input("Введите действие: ")
        say_going = say_going.lower()
        if "возведи в квадрат" in say_going:
            print("введите число")
            x =int(input())
            x = x*x
            print(x)
        elif "построить график функции" in say_going:
            import Function
        elif "преобразование функции" in say_going:
            import Function_convert_convert
    elif "курс" in message:
        import Kurs
    elif "погода" in message:
        import Weather

    else:
        say_message("Unknown command")

def say_message(message):

    print(message)
if __name__ == "__main__":
    while True:
        command = listen_command()
        do_this_command(command)