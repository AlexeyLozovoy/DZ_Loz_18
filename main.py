class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, value):
        if len(self.stack) < self.size:
            self.stack.append(value)
            print("Строка {} добавлена в стек".format(value))
        else:
            print("Стек заполнен, строка {} не может быть добавлена".format(value))

    def pop(self):
        if len(self.stack) > 0:
            value = self.stack.pop()
            print("Строка {} удалена из стека".format(value))
        else:
            print("Стек пуст, невозможно выполнить операцию")

    def count(self):
        print("Количество строк в стеке:", len(self.stack))

    def is_empty(self):
        if len(self.stack) == 0:
            print("Стек пуст")
        else:
            print("Стек не пуст")

    def is_full(self):
        if len(self.stack) == self.size:
            print("Стек заполнен")
        else:
            print("Стек не заполнен")

    def clear(self):
        self.stack = []
        print("Стек очищен")

    def peek(self):
        if len(self.stack) > 0:
            value = self.stack[-1]
            print("Верхняя строка в стеке:", value)
        else:
            print("Стек пуст, невозможно выполнить операцию")


def main():
    stack = Stack(5)
    stack.push("строка 1") 
    stack.push("строка 2")
    stack.push("строка 3")

    while True:
        print("""
            1. Добавить строку в стек
            2. Удалить верхнюю строку из стека
            3. Количество строк в стеке
            4. Проверить, пуст ли стек
            5. Проверить, заполнен ли стек
            6. Очистить стек
            7. Получить значение верхней строки из стека
            0. Выход
        """)

        choice = input("Выберите действие: ")

        if choice == "1":
            value = input("Введите строку для добавления в стек: ")
            stack.push(value)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            stack.count()
        elif choice == "4":
            stack.is_empty()
        elif choice == "5":
            stack.is_full()
        elif choice == "6":
            stack.clear()
        elif choice == "7":
            stack.peek()
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
