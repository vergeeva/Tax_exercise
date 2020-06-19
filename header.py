import math


# 1. Квартира 2. Загородный дом 3. Земельный участок 4. Автомобиль

def car(n):  # для автомобиля
    if 0 < n < 100:  # Мощность и ставка в зависимости от количества лошадиных силы
        return n * 12
    elif 100 <= n < 125:
        return n * 25
    elif 125 <= n < 150:
        return n * 35
    elif 150 <= n < 175:
        return n * 45
    elif 175 <= n < 200:
        return n * 50
    elif 200 <= n < 225:
        return n * 65
    elif 225 <= n < 250:
        return n * 75
    elif n >= 250:
        return n * 150
    else:
        return 0  # Учитываем, что пользователь может случайно ввести отрицательное значени


def house(price):  # Для квартиры
    return price * 1.518 * 0.005  # Кадастровая стоимость, коэф. дефлятор и процент


def land(price, count_people, month):  # Земельный налог
    return price * (1 / count_people) * (month / 12) * 0.002


# Кадастровая стоимость, размер доли в праве на земельный участок,
# коэффициент владения земельным участком, налоговая ставка


def country_house(price):
    return price * 0.003
