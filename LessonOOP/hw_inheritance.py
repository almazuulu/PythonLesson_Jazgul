""" 
Задание 1: Множественное наследование

Создай классы для системы авторизации пользователей.

    User – базовый класс

        Поля: username (логин), email (почта).

        Метод display_info() – выводит информацию о пользователе.

    AuthSystem – отвечает за авторизацию

        Поле: is_authenticated (по умолчанию False).

        Метод login() – делает пользователя авторизованным 
        (is_authenticated = True).

        Метод logout() – разлогинивает (is_authenticated = False).

    Admin – наследуется от User и AuthSystem (множественное наследование)

        Поле: admin_level (уровень доступа).

        Метод display_admin_info() – показывает уровень доступа.

Пример работы кода:

admin = Admin("superuser", "admin@example.com", 5)

admin.display_info()  # "Логин: superuser, Почта: admin@example.com"
admin.display_admin_info()  # "Уровень доступа: 5"

admin.login()
print(admin.is_authenticated)  # True

admin.logout()
print(admin.is_authenticated)  # False

"""
# Ваш код


""" 
Задание 2: Цепочное наследование

Представь, что ты разрабатываешь систему заказов в магазине. Создай три класса:

    Product – базовый класс

        Поля: name (название товара), price (цена).

        Метод display_product() – выводит название и цену.

    OrderItem – наследуется от Product

        Поле: quantity (количество товара).

        Метод calculate_total() – считает общую стоимость (price * quantity).

    Order – наследуется от OrderItem

        Поле: order_id (уникальный номер заказа).

        Метод display_order() – выводит номер заказа, название товара,
        количество и общую стоимость.
        
Пример работы кода:

order = Order("Ноутбук", 1000, 2, 12345)

order.display_product()  # "Товар: Ноутбук, Цена: 1000$"
print(order.calculate_total())  # 2000

order.display_order()  
# "Заказ #12345: Ноутбук, Количество: 2, Итоговая сумма: 2000$"
"""

# Ваш код

