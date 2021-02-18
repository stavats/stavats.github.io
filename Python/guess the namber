import random     # генерация случайного чмсла

x = 0             # введенное пользователем число
digit = 0         # загаданное (случайное) компьютером число
lowDigit = 10     # нижняя граница диапазона загаданного числа
highDigit = 40    # верхняя граница диапазона загаданного числа
countInput = 0    # количество попыток пользователя угадать число
playGame = True   # если false, игра прекращается
win = False       # угадал ли пользователь число
score = 0         # текущее количество очков
startScore = 100  # начальное количество очков
maxScore = 0      # максимальное количество очков в текущей игре

# - - - - - - - - - Main loop
while (playGame):
    digit = random.randint(lowDigit, highDigit)
    countInput = 0
    score = startScore
    print("-" * 40)
    print(f"""
            Компьютер загадал число, попробуйте угадать.
            Вам дано {startScore} очков.""")
    print("-" * 40)
    print(f"Случайное число: {digit}")

    # - - - - - - - ВНУТРЕННИЙ ЦИКЛ
    while (not win and score > 0):
        print("-" * 40)
        print(f"Заработано {score} очков.")
        print(f"Рекорд: {maxScore}")
        print("-" * 40)

        x = ""                                                           # для проверки x на число
        while (not x.isdigit()):                                         # цикл будет запрашивать ввод, пока не введешь число
            x = input(f"Введите число от {lowDigit} до {highDigit}: ")
            # startScore -= 10
            # score = startScore 
            # print(f"Осталось {score} очков")                                             
            if (not x.isdigit()):
                print("." * 20 + "Введите, пожалуйста, число.")
            elif (score > maxScore):
                maxScore = score

        x = int(x)
        if (x == digit):                                                 # сравнение введенного пользователем числа с загаданным
            win = True                                                   # число угадали, прекратить внутренний цикл    
        else:
            length = abs(x - digit)
            if (length < 3):
                print("Очень горячо!")
            elif (length < 5):
                print("Горячо!")
            elif (length < 10):
                print("Тепло")
            elif (length < 15):
                print("Прохладно")
            elif (length < 20):
                print("Холодно")
            else:
                print("Совсем холодно")

            if (countInput == 7):
                score -= 10
                if (digit % 2 == 0):
                    print("Число четное")
                else:
                    print("Число нечетное")
            elif (countInput == 6):
                score -= 4
                if (digit % 4 == 0):
                    print("Число делится на 4")
                else:
                    print("Число не делится на 4")   
            elif (countInput > 2 and countInput < 5):
                score -= 2
                if (x > digit):
                    print("Загаданное число МЕНЬШЕ вашего")
                else:
                    print("Загаданное число БОЛЬШЕ вашего")
            score -= 5
        countInput += 1

    print("*" * 30)
    if (x == digit):
        print("Победа! Поздравляем!")
    else:
        print("У вас закончились очки. Вы проиграли.")

    if (input("Enter - сыграть ещё, 0 - выход ") == "0" ):               #  при вводе значения отличного от 0, будет продолжена игра
        playGame = False
    else:
        win = False   
        
    # elif (score == 0):                                               # кончились очки 
    #     print("Вы потратили все очки")
    #     win = True                                                   # при утрате всех очков, прекратить внутренний цикл

print("*" * 30)
print("Спасибо за игру")    
