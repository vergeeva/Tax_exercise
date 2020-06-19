from header import *


def main():
    tax_list = {}  # Полный список налогоплательщиков и их налогов
    key = 0
    value = 1
    things_list = ["Квартира", "Загородный дом", "Земельный участок", "Автомобиль"]
    name_list = {}  # Словарь для названия имущества и суммы налога
    name = "отсутствует"
    while value != 0:
        key_1 = 1
        while key_1 != 0:
            print(f'Имя налогоплательщика сейчас : {name}')
            key_1 = int(input('Хотите изменить его?(0 - если нет)\nВаш выбор: '))
            if key_1 == 0:
                break
            name = input("Введите имя налогоплательщика: ")

        print("Выберите тип имущества:")
        try:
            key = int(input("1. Квартира\n2. Загородный дом\n3. Земельный участок\n4. Автомобиль\nВаш выбор: "))
        except ValueError:
            print("Введено неверное значение, попробуйте еще раз")
        if key == 1:
            price = float(input("Введите кадастровую стоимость квартиры: "))
            tax = house(abs(price))  # используем функцию abs(х), чтобы избежать отрицательных
            # счета отрицательных значений
            name_list[things_list[key - 1]] = tax
        elif key == 2:
            price = float(input("Введите кадастровую стоимость загородного дома: "))
            tax = country_house(abs(price))
            name_list[things_list[key - 1]] = tax
        elif key == 3:
            price = float(input("Введите кадастровую стоимость земельного участка: "))
            count_people = int(input("Введите количество собственников земельного участка: "))
            month = int(
                input("Введите количество полных месяцев, в которые вы являетесь собственником за данный год: "))
            tax = land(price, count_people, month)
            name_list[things_list[key - 1]] = tax
        elif key == 4:
            n = int(input("Введите мощность автомобиля(л/с): "))
            tax = car(n)
            name_list[things_list[key - 1]] = tax
        else:
            print("Вы выбрали неверный объект")
        (tax_list[name]) = name_list
        # name_list.clear()
        try:
            value = int(input("Нажмите 0, если хотите выйти "))
        except ValueError:
            value = 1

    for key, value in tax_list.items():
        print(f'Имя налогоплательщика: {key};\nНалоги: {value}\n')


main()
