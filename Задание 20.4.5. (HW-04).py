import json
from collections import defaultdict

# Читаем данные из файла
with open("orders_july_2023.json", "r", encoding="utf-8") as file:
    orders = json.load(file)

# Инициализация переменных для анализа
max_price = 0
max_order_price = ''

max_quantity = 0
max_order_quantity = ''

orders_per_day = defaultdict(int)
orders_per_user = defaultdict(int)
total_spent_per_user = defaultdict(float)

sum_price = 0
sum_quantity = 0
order_count = 0

# Обработка данных
for order_num, order_data in orders.items():
    # Данные заказа
    date = order_data['date']
    user_id = order_data['user_id']
    quantity = order_data['quantity']
    price = order_data['price']

    # Поиск самого дорогого заказа
    if price > max_price:
        max_price = price
        max_order_price = order_num

    # Поиск заказа с наибольшим количеством товаров
    if quantity > max_quantity:
        max_quantity = quantity
        max_order_quantity = order_num

    # Подсчет заказов по дням
    orders_per_day[date] += 1

    # Подсчет заказов и затрат на пользователя
    orders_per_user[user_id] += 1
    total_spent_per_user[user_id] += price

    # Подсчет общей стоимости и количества товаров
    sum_price += price
    sum_quantity += quantity
    order_count += 1

# День с наибольшим количеством заказов
most_orders_day = max(orders_per_day, key=orders_per_day.get)

# Пользователь с наибольшим количеством заказов
most_active_user = max(orders_per_user, key=orders_per_user.get)

# Пользователь с наибольшей суммарной стоимостью заказов
highest_spender = max(total_spent_per_user, key=total_spent_per_user.get)

# Средняя стоимость заказа и товаров
average_order_price = sum_price / order_count
average_item_price = sum_price / sum_quantity

# Вывод результатов
print(f"Номер самого дорогого заказа: {max_order_price}")
print(f"Номер заказа с самым большим количеством товаров: {max_order_quantity}")
print(f"День с наибольшим количеством заказов: {most_orders_day}")
print(f"Пользователь с наибольшим количеством заказов: {most_active_user}")
print(f"Пользователь с наибольшей суммарной стоимостью заказов: {highest_spender}")
print(f"Средняя стоимость заказа: {average_order_price:.2f}")
print(f"Средняя стоимость товаров: {average_item_price:.2f}")
