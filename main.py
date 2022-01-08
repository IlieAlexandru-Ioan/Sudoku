import random
dimension = 9
table = []

def create_table():
    table = [0 for i in range(1, dimension + 1)]
    for i in range(dimension):
        table[i] = [0 for j in range(1, dimension + 1)]
    return table

def auto_population(number):
    i= 0
    while i < number:
        val1 = random.randint(0, dimension - 1)
        val2 = random.randint(0, dimension - 1)
        if table[val1][val2] == 0:
            table[val1][val2] = random.randint(1, dimension)
            i += 1

def frequency(index, table, dimens, mode):
    dict = {}
    for i in range(1, dimens + 1):
        dict[i] = 0
    if mode == "line":
        for i in range(dimens):
            if table[index][i] != 0:
                dict[table[index][i]] += 1

    if mode == "column":
        for i in range(dimens):
            if table[i][index] != 0:
                dict[table[i][index]] += 1
    return dict

def square_frequency(line, column, table, dimens):
    dict = {}
    index_col = column // 3
    index_lin = line // 3
    for i in range(1, dimens + 1):
        dict[i] = 0
    for i in range(3):
        for j in range(3):
            if table[index_lin * 3 + i][index_col * 3 + j] != 0:
                dict[table[index_lin * 3 + i][index_col * 3 + j]] += 1
    return dict


def verif_unique(line, column, dimens,table):
    dict_col = frequency(column, table, dimens, "column")
    dict_line = frequency(line, table, dimens, "line")
    dict_square = square_frequency(line, column, table, dimens)
    if table[line][column] != 0:
        if dict_line[table[line][column]] >= 2 or dict_col[table[line][column]] >= 2 or dict_square[table[line][column]] >= 2:
            value = 1
            while True:
                if dict_col[value] == 0 and dict_line[value] == 0 and dict_square[value] == 0:
                    table[line][column] = value
                    break
                value += 1
                if value > 9:
                    print("Nu exista solutie")
                    break

def is_choise(number, line, column, table, dimens):
    dict_line = frequency(line, table, dimens, "line")
    dict_col = frequency(column, table, dimens, "column")
    dict_square = square_frequency(line, column, table, dimens)
    if dict_col[number] == 0 and dict_line[number] == 0 and dict_square[number] == 0:
        return True
    else:
        return False

def solve():
    for line in range(dimension):
        for column in range(dimension):
            if table[line][column] == 0:
                for possible_val in range(1, dimension+1):
                    if is_choise(possible_val, line, column,table, dimension):
                        table[line][column] = possible_val
                        solve()
                        table[line][column] = 0 # do rollback
                return
    afis_fancy(table, dimension)
    input("more?")


def afis_fancy(table, dim):
    for i in range(dim):
        print(table[i])

if __name__=="__main__":
    table = create_table()
    auto_population(30)
    afis_fancy(table, dimension)
    for i in range(dimension):
        for j in range(dimension):
            verif_unique(i,j, dimension, table)
    print("\n")
    solve()
    afis_fancy(table, dimension)

