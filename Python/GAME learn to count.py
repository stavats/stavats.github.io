# программа-генератор простых арифметических примеров, которые предлагается решить
# x + y = ?
import random

x = 0                   # первая переменная арифметического выражение
y = 0                   # вторая переменная арифметического выражения
sign = 0                # хранит знак действия (сложение, вычитание и т.д.)
z = 0                   # число, которое вводит пользователь (ответ)
playGame = True         # продолжение или остановка игры
lowDigit = 90
highDigit = 100

while (playGame):
    sign = random.randint(0, 3)

    if (sign == 0):
        z = random.randint(lowDigit, highDigit)
        x = random.randint(lowDigit, z)
        y = z - x
        if (random.randint(0, 1) == 0):
            print(f"{x} + {y} = ?")
        else:
            print(f"{y} + {x} = ?")

    elif (sign == 1):
        x = random.randint(lowDigit, highDigit)
        y = random.randint(0, x - lowDigit)
        z = x - y
        print(f"{x} - {y} = ?")

    elif (sign == 2):
        x = random.randint(1, (highDigit - lowDigit) //
                            random.randint(1, highDigit // 10) +1)
        y = random.randint(lowDigit, highDigit) // x
        z = x * y
        print(f"{x} * {y} = ?")

    elif (sign == 3):
        x = random.randint(1, (highDigit - lowDigit) //
                        random.randint(1, highDigit // 10))
        y = random.randint(lowDigit, highDigit) // x
        if (y == 0):
            y = 1
        x = x * y
        z = x // y
        print(f"{x} / {y} = ?")
    
    userInput = input("Ваш ответ ")
    if (int(userInput) == z):
        print("Правильно")
    else:
        print("Неправильно. Получен взлом жопы")
        print("*" * 50)
        print("Чтобы продолжить игру, нажмите Enter")
        if (input()):
            playGame = True