def choose_field_size():
    """a function that crafts a field"""
    while True:
        print('Пожалуйста, задайте размер поля (число от 3 до 5):')
        try:
            field_size = int(input())
        except ValueError:
            continue
        if field_size == 3:
            print('\nПоле для игры:\n')
            rows = {'a': 1, 'b': 2, 'c': 3}
            columns = [1, 2, 3]
            field = [[['   '], ['   '], ['   ']], [['   '], ['   '], ['   ']], [['   '], ['   '], ['   ']]]
            rows_name = ['a', 'b', 'c']
            print('  1   2   3\n')
            for row_num in range(len(field)):
                print(rows_name[row_num], sep='', end='')
                for cell in field[row_num]:
                    print(cell[0], '|', sep='', end='')
                print('\n --------------', sep='', end='')
                print('\n')
            break
        elif field_size == 4:
            print("""  1   2   3   4
a   |   |   |   
 --------------
b   |   |   |
 --------------
c   |   |   |
 --------------
d   |   |   |""")
            break
        elif field_size == 5:
            print("""  1   2   3   4   5
a   |   |   |   | 
 ------------------
b   |   |   |   |
 ------------------
c   |   |   |   |
 ------------------
d   |   |   |   |
 ------------------
e   |   |   |   |""")
            break
        else:
            continue
    return field, rows, columns


def player_x(field: list, rows: dict, columns: tuple) -> list:
    """a function that determines player X"""
    print('Игрок 1, ваш ход')
    while True:
        print('Пожалуйста, введите номер строки и столбца (например, а3)')
        move = list(input())
        print(move)
        try:
            chosen_row_num = rows.get(move[0])
        except KeyError:
            print('Первым символом должна быть маленькая латинская буква')
            continue
        if int(move[1]) in columns:
            chosen_column_num = int(move[1])
            break
        else:
            print('Вторым символом должна быть цифра от 1 до 3')
    return print(chosen_row_num, chosen_column_num)


def player_o() -> int:
    """a function that determines player O"""
    return


if __name__ == '__main__':
    det_field, det_rows, det_columns = choose_field_size()
    player_x(det_field, det_rows, det_columns)
