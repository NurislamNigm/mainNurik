#Homework 2.10
# Задание: «Меню кафе»
# Программа должна помочь владельцу кафе управлять меню и заказами.
# Все действия оформляются как отдельные функции, где обязательно хотя бы в половине случаев используются lambda и встроенные функции.
# Требования
# Сохранить меню в виде словаря:

# # 	menu = {
# #     "coffee": 120,
# #     "tea": 80,
# #     "sandwich": 200,
# #     "cake": 150,
# #     "juice": 100
# # }
# # Вывести всё меню, отсортированное:
# # по названию блюда (алфавит)
# # по цене (от дешёвого к дорогому)
# # Использовать sorted + lambda.
# # Посчитать среднюю цену блюда в меню.
# # Использовать sum, len и lambda (например, внутри map).


# Добавить новые блюда в меню через ввод от пользователя. Если блюдо уже есть, заменить цену.
# Использовать dict.update и lambda.


# Удалить блюдо из меню (с проверкой, что оно существует).
# Использовать if … else в одну строку.


# Показать все блюда дешевле определённой цены N.
# Использовать filter + lambda.


# Найти самое дешёвое и самое дорогое блюдо.
# Использовать min и max с lambda.


# Сделать список только напитков (coffee, tea, juice) и отсортировать их по цене.
# Использовать filter + sorted + lambda.


# Сформировать заказ: пользователь вводит список блюд через запятую.
# Убрать пробелы
# Проверить, есть ли блюда в меню
# Составить словарь заказа {блюдо: цена}

# Использовать map, filter, lambda.


# Посчитать общую стоимость заказа.
# Использовать reduce + lambda.


# Показать заказ в красивом виде:
# Ваш заказ:
# 1. Coffee — 120 руб.
# 2. Cake — 150 руб.
# Итого: 270 руб.
# Использовать enumerate + lambda.


# Проверить заказ:
# Если сумма больше 500, вывести: «Поздравляем, у вас скидка 10%!».
# Если заказ пустой — вывести: «Вы ничего не выбрали».

#  Использовать any / a

# Меню кафе
menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}

# Вывести всё меню, отсортированное:
# по названию блюда (алфавит)
# по цене (от дешёвого к дорогому)
def show_menu_sorted():
    print("\nМеню, отсортированное по названию:")
    for item in sorted(menu.items(), key=lambda x: x[0]):
        print(f"{item[0]} — {item[1]} руб.")
    
    print("\nМеню, отсортированное по цене:")
    for item in sorted(menu.items(), key=lambda x: x[1]):
        print(f"{item[0]} — {item[1]} руб.")

# Посчитать среднюю цену блюда в меню.
# Использовать sum, len и lambda (например, внутри map).
def average_price():
    avg = sum(map(lambda x: x[1], menu.items())) / len(menu)
    print(f"\nСредняя цена блюда в меню: {avg:.2f} руб.")

# Добавить новые блюда в меню через ввод от пользователя. Если блюдо уже есть, заменить цену.
# Использовать dict.update и lambda.
def add_dish():
    name = input("Введите название блюда: ").strip().lower()
    try:
        price = int(input("Введите цену блюда: ").strip())
    except ValueError:
        print("Цена должна быть числом.")
        return
    menu.update({name: price})
    print(f"Блюдо '{name}' добавлено/обновлено с ценой {price} руб.")

# Удалить блюдо из меню (с проверкой, что оно существует).
# Использовать if … else в одну строку.
def delete_dish():
    name = input("Введите название блюда для удаления: ").strip().lower()
    print(f"Блюдо '{name}' удалено." if menu.pop(name, None) is not None else "Блюдо не найдено.")

# Показать все блюда дешевле определённой цены N.
# Использовать filter + lambda.
def dishes_cheaper_N():
    try:
        N = int(input("Введите цену N: ").strip())
    except ValueError:
        print("Цена должна быть числом.")
        return
    cheap_dishes = list(filter(lambda x: x[1] < N, menu.items()))
    if cheap_dishes:
        print(f"\nБлюда дешевле {N} руб.:")
        for item in cheap_dishes:
            print(f"{item[0]} — {item[1]} руб.")
    else:
        print(f"Нет блюд дешевле {N} руб.")

# Найти самое дешёвое и самое дорогое блюдо.
# Использовать min и max с lambda.
def cheapest_and_costliest():
    cheapest = min(menu.items(), key=lambda x: x[1])
    costliest = max(menu.items(), key=lambda x: x[1])
    print(f"\nСамое дешевое блюдо: {cheapest[0]} — {cheapest[1]} руб.")
    print(f"Самое дорогое блюдо: {costliest[0]} — {costliest[1]} руб.")

# Сделать список только напитков (coffee, tea, juice) и отсортировать их по цене.
# Использовать filter + sorted + lambda.
def drinks_sorted():
    drinks = list(filter(lambda x: x[0] in ["coffee", "tea", "juice"], menu.items()))
    sorted_drinks = sorted(drinks, key=lambda x: x[1])
    print("\nНапитки, отсортированные по цене:")
    for item in sorted_drinks:
        print(f"{item[0]} — {item[1]} руб.")

# Сформировать заказ: пользователь вводит список блюд через запятую.
# Убрать пробелы
# Проверить, есть ли блюда в меню
# Составить словарь заказа {блюдо: цена}

# Использовать map, filter, lambda.
def create_order():
    order_input = input("Введите список блюд через запятую: ").strip().lower()
    order_list = list(map(lambda x: x.strip(), order_input.split(',')))
    order = dict(filter(lambda x: x[0] in menu, map(lambda x: (x, menu[x]), order_list)))
    if not order:
        print("Вы ничего не выбрали.")
        return None
    return order

# Посчитать общую стоимость заказа.
# Использовать reduce + lambda.
def total_order_cost(order):
    from functools import reduce
    total = reduce(lambda acc, x: acc + x[1], order.items(), 0)
    return total

# Показать заказ в красивом виде:
# Ваш заказ:
# 1. Coffee — 120 руб.
# 2. Cake — 150 руб.
# Итого: 270 руб.
# Использовать enumerate + lambda.
def show_order(order):
    print("\nВаш заказ:")
    for idx, item in enumerate(order.items(), start=1):
        print(f"{idx}. {item[0].capitalize()} — {item[1]} руб.")
    total = total_order_cost(order)
    if total > 500:
        total = total * 0.9
        print("Поздравляем, у вас скидка 10%!")
    print(f"Итого: {total} руб.")

# Главное меню
def main_menu():
    while True:
        print("\nМеню кафе:")
        print("1. Показать меню, отсортированное по названию и цене")
        print("2. Посчитать среднюю цену блюда в меню")
        print("3. Добавить новое блюдо в меню")
        print("4. Удалить блюдо из меню")
        print("5. Показать все блюда дешевле определённой цены N")
        print("6. Найти самое дешёвое и самое дорогое блюдо")
        print("7. Показать список напитков, отсортированных по цене")
        print("8. Сформировать заказ")
        print("0. Выход")

        choice = input("Введите номер действия: ").strip()

        if choice == '1':
            show_menu_sorted()
        elif choice == '2':
            average_price()
        elif choice == '3':
            add_dish()
        elif choice == '4':
            delete_dish()
        elif choice == '5':
            dishes_cheaper_N()
        elif choice == '6':
            cheapest_and_costliest()
        elif choice == '7':
            drinks_sorted()
        elif choice == '8':
            order = create_order()
            if order:
                show_order(order)
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()