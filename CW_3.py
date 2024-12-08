from typing import List


def syracuse_sequence(n: int) -> List[int]:

    "Возвращает сиракузскую последовательность для заданного числа n."

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():

    while True:

        print("Введите натуральное число или 'exit' для завершения программы.")

        user_input = input("Ваш ввод: ").strip()
        if user_input.lower() == 'exit':
            print("Работа программы завершена.")
            break

        if not user_input.isdigit() or int(user_input) <= 0:
            print("Ошибка: введите положительное целое число.")
            continue

        n = int(user_input)
        sequence = syracuse_sequence(n)

        print(f"\nСиракузская последовательность для {n}: {sequence}")


if __name__ == "__main__":
    main()