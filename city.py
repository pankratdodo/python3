class City():

    def __init__(self, name, days, old, kid, money_per_day, price, flight):
        print("Выберите город:\n•Рим\n•Париж\n•Лондон\n•Токио\n•Пекин\nдля выхода напишите выход\n")
        self.name = input()
        if self.name == "выход":
            exit()
        self.days = int(input("Введите количество дней поездки: "))
        self.old = int(input("Введите количество взрослых: "))
        self.kid = int(input("Введите количество детей: "))
        self.money_per_day = int(input("Введите количество денег, которые вы готовы потратить в день(руб): "))
        self.price = 0
        self.flight = 0


def parse_param():
    while True:
        if city1.name != "Рим" and city1.name != "Париж" and city1.name != "Лондон" and city1.name != "Токио" and city1.name != "Пекин":
            city1.name = input("Такого города нет, выберете из предложенных:\n•Рим\n•Париж\n•Лондон\n•Токио\n•Пекин\nдля выхода напишите выход\n")
        if city1.days < 1 or city1.days > 20:
            print("Введите верное количестно дней поездки(от 1 до 20): ")
            city1.days = int(input())
        elif city1.old < 1 or city1.old > 3:
            print("Введите верное количестно взрослых (от 1 до 3): ")
            city1.old = int(input())
        elif city1.kid < 0 or city1.kid > 3:
            print("Введите верное количестно детей(от 0 до 3): ")
            city1.kid = int(input())
        elif city1.money_per_day < 1000 or city1.money_per_day > 100000:
            print("Введите верное количестно денег, которые вы готовы потратить в день на человека(от 1000руб до 100000руб): ")
            city1.money_per_day = int(input())
        else:
            break

def check_money():
    money = city1.days * city1.money_per_day
    print(city1.price)
    while money < city1.price:
        city1.money_per_day = int(input("К сожалению, вам не хватит средств, введите число больше: "))
        parse_param()
        money = city1.days * city1.money_per_day
    return money - city1.price


def move_rome():
    vivod = "Передвигаться в Риме очень удобно на метро, вы можете взять проездной "
    if city1.days > 3 and city1.days < 11:
        vivod += "на неделю "
        city1.price += (city1.old + city1.kid) * 1698
    if city1.days == 1 or city1.days == 8:
        if city1.days == 8:
            vivod += "и "
        vivod += "на один день "
        city1.price += (city1.old + city1.kid) * 485
    if city1.days == 2 or city1.days == 9:
        if city1.days == 9:
            vivod += "и "
        vivod += "на два дня "
        city1.price += (city1.old + city1.kid) * 867
    if city1.days == 3 or city1.days == 10:
        if city1.days == 10:
            vivod += "и "
        vivod += "на три дня "
        city1.price += (city1.old + city1.kid) * 1250
    if city1.days > 10:
        vivod += "на месяц"
        city1.price += (city1.old + city1.kid) * 2429
    return vivod

def attractions_rome(vivod, money):
    if money < (city1.old + city1.kid) * 600:
        print("Вы можете выбрать для посещения бесплатные музеи:\n•Санта-Мария-Маджоре\n•Церковь Сан-Луиджи-деи-Франчези\n• Музея Ватикана\n•Палаццо Монтечиторио\n•Пантеон\n•Форум Романум")
    elif money < 3600 * (city1.old + city1.kid):
        money = int(money / 600 / (city1.old + city1.kid))
        print("Вы можете выбрать " + str(money) + ", учитывая ваши средства:\n•галерея Боргезе\n•дворец фамилии Барберини\n•художественная галерея в римском палаццо Спада\n•Галерея Корсини\n•Музей музыкальных инструментов\n•Вход в Колизей")
        print(vivod)
        city1.price += int(money) * 600 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")
    else:
        print("Вы можете выбрать все предложенные достопримечательности, учитывая ваши средства:\n•галерея Боргезе\n•дворец фамилии Барберини\n•художественная галерея в римском палаццо Спада\n•Галерея Корсини\n•Музей музыкальных инструментов\n•Вход в Колизей")
        print(vivod)
        city1.price += 3600 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")

def rome():
    # Перелет
    city1.flight += (city1.old * 8500 + city1.kid * 7000)
    # Проживание
    city1.price += (city1.kid + city1.old) * city1.days * 700
    # Проезд
    vivod = move_rome()
    # Покушать
    city1.price += (city1.old + city1.kid) * 700 * 3 * city1.days
    #Проверяем, хватило ли денег
    money = check_money()
    #Достопримечательности
    attractions_rome(vivod, money)

def move_paris():
    vivod = "Передвигаться в Париже очень удобно на метро, вы можете взять проездной "
    ost = city1.days % 5
    cel = city1.days / 5
    if ost == 0:
        vivod += "на 5 дней " + str(int(cel)) + " раз"
        city1.price += (city1.old + city1.kid) * cel * 3500
    elif ost == 1:
        if cel > 0:
            vivod += "на 5 дней " + str(int(cel)) + " раз и на 1 день"
            city1.price += (city1.old + city1.kid) * (int(cel) * 3500 + 1400)
        else:
            vivod += "на 1 день"
            city1.price += (city1.old + city1.kid) * 1400
    elif ost == 2:
        if cel > 0:
            vivod += "на 5 дней " + str(int(cel)) + " раз и на 2 дня"
            city1.price += (city1.old + city1.kid) * (int(cel) * 3500 + 2100)
        else:
            vivod += "на 2 дня"
            city1.price += (city1.old + city1.kid) * 2100
    elif ost == 3:
        if cel > 0:
            vivod += "на 5 дней " + str(int(cel)) + " раз и на 3 дня"
            city1.price += (city1.old + city1.kid) * (int(cel) * 3500 + 2800)
        else:
            vivod += "на 3 дня"
            city1.price += (city1.old + city1.kid) * 2800
    else:
        if cel > 0:
            vivod += "на 5 дней " + str(int(cel + 1)) + " раз"
            city1.price += (city1.old + city1.kid) * (int(cel) * 3500 + 3500)
        else:
            vivod += "на 5 дней"
            city1.price += (city1.old + city1.kid) * 3500
    return vivod

def attractions_paris(vivod, money):
    if money < (city1.old + city1.kid) * 1400:
        print("Вы можете выбрать для посещения бесплатные музеи:\n•«Блошиный рынок» в Сент-Уан\n•Марсово поле\n•Кладбище Пер-Лашез\n•Музей современного искусства города Парижа\n•Базилика Сакре-Кёр\n•Парк Бют-Шомон")
    elif money < 8400 * (city1.old + city1.kid):
        money = int(money / 1400 / (city1.old + city1.kid))
        print("Вы можете выбрать " + str(money) + ", учитывая ваши средства:\n•Билет в Диснейленд\n•Вход на смотровую площадку Эйфелевой башни\n•Входной билет в Лувр\n•Экскурсия по катакомбам Парижа\n•Вход в Версальский дворец\n•Билет в Музей Средневековья")
        print(vivod)
        city1.price += int(money) * 1400 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")
    else:
        print("Вы можете выбрать все предложенные достопримечательности, учитывая ваши средства:\n•Билет в Диснейленд\n•Вход на смотровую площадку Эйфелевой башни\n•Входной билет в Лувр\n•Экскурсия по катакомбам Парижа\n•Вход в Версальский дворец\n•Билет в Музей Средневековья")
        print(vivod)
        city1.price += 8400 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")

def paris():
    # Перелет
    city1.flight += (city1.old * 25000 + city1.kid * 23500)
    # Проживание
    city1.price += (city1.kid + city1.old) * city1.days * 2600
    # Проезд
    #Проезд от аэропорта до города
    vivod = move_paris()
    #Покушать
    city1.price += (city1.old + city1.kid) * 800 * 3 * city1.days
    #Проверяем, хватило ли денег
    money = check_money()
    # Достопримечательности
    attractions_paris(vivod, money)

def move_london():
    vivod = "Передвигаться в Лондоне очень удобно на автобусах, вы можете взять проездной "
    if city1.days < 8:
        vivod += "на неделю"
        city1.price += (city1.old + city1.kid) * 1508
    elif city1.days < 15:
        vivod += "на две недели"
        city1.price += (city1.old + city1.kid) * 1508 * 2
    else:
        vivod += "на три недели"
        city1.price += (city1.old + city1.kid) * 1508 * 3
    return vivod

def attractions_london(vivod, money):
    if money < (city1.old + city1.kid) * 600:
        print("Вы можете выбрать для посещения бесплатные музеи:\n•Музей естествознания\n•Галерея Тейт\n•Музей Лондона\n•Национальная портретная галерея\n•Вестминстерский собор\n•Музей Виктории и Альберта")
    elif money < 3600 * (city1.old + city1.kid):
        money = int(money / 600 / (city1.old + city1.kid))
        print("Вы можете выбрать " + str(money) + ", учитывая ваши средства:\n•Виндзорский замок\n•Букингемский дворец\n•Лондонский Тауэр\n•Вестминстерское Аббатство\n•Собор Святого Павла\n•Музей мадам Тюссо")
        print(vivod)
        city1.price += int(money) * 600 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")
    else:
        print("Вы можете выбрать все предложенные достопримечательности, учитывая ваши средства:\n•Виндзорский замок\n•Букингемский дворец\n•Лондонский Тауэр\n•Вестминстерское Аббатство\n•Собор Святого Павла\n•Музей мадам Тюссо")
        print(vivod)
        city1.price += 3600 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")

def london():
    # Перелет
    city1.flight += (city1.old * 18000 + city1.kid * 16800)
    # Проживание
    city1.price += (city1.kid + city1.old) * city1.days * 1500
    # Проезд
    vivod = move_london()
    # Покушать
    city1.price += (city1.old + city1.kid) * 1100 * 3 * city1.days
    # Проверяем, хватило ли денег
    money = check_money()
    # Достопримечательности
    attractions_london(vivod, money)

def move_tokio():
    vivod = "Передвигаться в Токио очень удобно на метро, вы можете взять проездной "
    ost = city1.days % 3
    cel = city1.days / 3
    if ost == 0:
        vivod += "на 3 дня " + str(int(cel)) + " раз"
        city1.price += city1.old * cel * 900 + city1.kid * cel * 450
    elif ost == 1:
        if cel > 0:
            vivod += "на 3 дней " + str(int(cel)) + " раз и на 1 день"
            city1.price += city1.old * (int(cel) * 900 + 480) + city1.kid * (int(cel) * 450 + 240)
        else:
            vivod += "на 1 день"
            city1.price += city1.old * 480 + city1.kid * 240
    elif ost == 2:
        if cel > 0:
            vivod += "на 3 дней " + str(int(cel)) + " раз и на 2 дня"
            city1.price += city1.old * (int(cel) * 900 + 720) + city1.kid (int(cel) * 450 * 360)
        else:
            vivod += "на 2 дня"
            city1.price += city1.old * 720 + city1.kid * 360
    return vivod

def attractions_tokio(vivod, money):
    if money < (city1.old + city1.kid) * 700:
        print("Вы можете выбрать для посещения бесплатные музеи:\n•Императорский дворец\n•Парк Уэно\n•Храм Мэйдзи\n•Радужный мост\n•Памятник Хатико\n•Перекресток Сибуя")
    elif money < 4800 * (city1.old + city1.kid):
        money = int(money / 700 / (city1.old + city1.kid))
        print("Вы можете выбрать " + str(money) + ", учитывая ваши средства:\n•Токийская телебашня\n•Музей маленького принца\n•Зоопарк Уэно\n•Дворец Аксака\n•Ругоку Кокугикан\n•Сады Хамарикю")
        print(vivod)
        city1.price += int(money) * 700 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")
    else:
        print("Вы можете выбрать все предложенные достопримечательности, учитывая ваши средства:\n•Токийская телебашня\n•Музей маленького принца\n•Зоопарк Уэно\n•Дворец Аксака\n•Ругоку Кокугикан\n•Сады Хамарикю")
        print(vivod)
        city1.price += 4800 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")

def tokio():
    # Перелет
    city1.flight += (city1.old * 28000 + city1.kid * 25400)
    # Проживание
    city1.price += (city1.kid + city1.old) * city1.days * 2100
    # Проезд
    vivod = move_tokio()
    # Покушать
    city1.price += (city1.old + city1.kid) * 475 * 3 * city1.days
    # Проверяем, хватило ли денег
    money = check_money()
    # Достопримечательности
    attractions_tokio(vivod, money)

def move_pekin():
    vivod = "Передвигаться в Пекине очень удобно на метро, вы можете купить билет за 47 рублей"
    city1.price += (city1.kid + city1.old) * 47 * 5 * city1.days
    return vivod

def attractions_pekin(vivod, money):
    if money < (city1.old + city1.kid) * 330:
        print("Вы можете выбрать для посещения бесплатные музеи:\n•798 Art Zone\n•Площадь Тяньаньмэнь\n•Национальный музей Китая\n•Рынок Паньцзяюань\n•рынок Ябаолу\n•Люличан")
    elif money < 1980 * (city1.old + city1.kid):
        money = int(money / 330 / (city1.old + city1.kid))
        print("Вы можете выбрать " + str(money) + ", учитывая ваши средства:\n•парк Бэйхай стоит\n•Китайская стена\n•Храм парка Beihai\n•парк возле Храма неба\n•Храм Юнхэгун\n•Запретный город Гугун")
        print(vivod)
        city1.price += int(money) * 330 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")
    else:
        print("Вы можете выбрать все предложенные достопримечательности, учитывая ваши средства:\n•парк Бэйхай стоит\n•Китайская стена\n•Храм парка Beihai\n•парк возле Храма неба\n•Храм Юнхэгун\n•Запретный город Гугун")
        print(vivod)
        city1.price += 1980 * (city1.old + city1.kid)
        print("Не забудьте сделать визу!")

def pekin():
    # Перелет
    city1.flight += (city1.old * 20000 + city1.kid * 18000)
    # Проживание
    city1.price += (city1.kid + city1.old) * city1.days * 1500
    # Проезд
    vivod = move_pekin()
    # Покушать
    city1.price += (city1.old + city1.kid) * 330 * 3 * city1.days
    # Проверяем, хватило ли денег
    money = check_money()
    # Достопримечательности
    attractions_pekin(vivod, money)

def check_city():
    if city1.name == "Рим":
        rome()
    elif city1.name == "Париж":
        paris()
    elif city1.name == "Лондон":
        london()
    elif city1.name == "Токио":
        tokio()
    elif city1.name == "Пекин":
        pekin()

while True:
    city1 = City(0, 0, 0, 0, 0, 0, 0)
    parse_param()
    check_city()
    print("Итоговая сумма: " + str(int(city1.price + city1.flight)) + " руб\n")
