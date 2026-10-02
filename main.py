def greet(name):
    return f"Привет, {name}!"


def main():
    name = input("Как тебя зовут? ")

    message = greet(name)
    print(message)

    print("\nДавай посчитаем сумму двух чисел:")
    try:
        a = float(input("Введи первое число: "))
        b = float(input("Введи второе число: "))
        print(f"Сумма: {a + b}")
    except ValueError:
        print("Ошибка: нужно вводить числа!")


if __name__ == "__main__":
    main()
