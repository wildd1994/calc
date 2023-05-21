import itertools


def calc(seq: list, n: int) -> list:
    """
    :param seq: последовательность цифр
    :param n: число которое необходимо получить
    :return:
    """
    signs = ['+', '-', '']
    results = []
    # Проверка что последовательность состоит из чисел
    if not all([char.isdigit() for char in seq]):
        print(f'В последовательности "{seq}" встречаются не только цифры')
        return results
    # Получаем количество знаков, которые будем вставлять
    number_sign = len(seq) - 1
    # Получаем все возможные вариации расстановки знаков для нашей последовательности
    for poss in itertools.product(signs, repeat=number_sign):
        # Склеиваем нашу последовательность со знаками
        seq_lst = [seq[i] + poss[i] for i in range(len(poss))]
        seq_lst.append(seq[number_sign])
        seq_with_sings = ''.join(seq_lst)
        # Считаем (можно использовать eval, но это не безопасно)
        res = evaluation(seq_with_sings)
        # Проверяем сумму с условием
        if res == n:
            results.append(seq_with_sings)
    return results


def evaluation(expression: str) -> int:
    res = []
    number_str = ''
    for idx, char in enumerate(expression):
        if char.isdigit():
            number_str += char
            if idx == len(expression) - 1:
                res.append(number_str)
        else:
            res.append(number_str)
            res.append(char)
            number_str = ''
    res_int = int(res[0])
    sign_idx = 1
    number_idx = 2
    while number_idx < len(res):
        sign_el = res[sign_idx]
        number_el = res[number_idx]
        if sign_el == '+':
            res_int += int(number_el)
        elif sign_el == '-':
            res_int -= int(number_el)
        sign_idx += 2
        number_idx += 2
    return res_int


if __name__ == '__main__':
    a = '9876543210'
    print('Введите число')
    number = input()
    if number.isdigit():
        number = int(number)
        solutions = '\n'.join(calc([char for char in a], number))
        if solutions:
            print(f'Решения для числа {number} последовательности {a}: \n{solutions}')
        else:
            print(f'Нет решений для числа {number} последовательности {a}')
    else:
        print(f'Введеное число некорректно')
