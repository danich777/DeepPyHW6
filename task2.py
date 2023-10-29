# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from classes import ChessBoard


def check_position(list_of_position: tuple) -> bool:
    board = ChessBoard()
    for index, coord in enumerate(list_of_position, 1):
        if not board.set(int(coord[0]), int(coord[1])):
            print(f'Ошибка на {index} фигуре')
            print(board)
            return False
    print(board)
    return True


if __name__ == '__main__':
    list_of_position = []
    for i in range(1, 9):
        list_of_pos = input(f'Введите координаты {i} ферзя через пробел: ').split()
        list_of_position.append((int(list_of_pos[0]), int(list_of_pos[1])))
    print(check_position(tuple(list_of_position)))