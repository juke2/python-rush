from copy import deepcopy

conways_grid = []
conways_variables = {}


def conways_init(X_LIM: int, Y_LIM: int):
    if conways_grid:
        conways_grid.clear()
    for i in range(0, X_LIM):
        conways_grid.append([0 for i in range(X_LIM)])
    conways_variables["X_LIM"] = X_LIM
    conways_variables["Y_LIM"] = Y_LIM


def mutate_grid_value_at_xy(x: int, y: int, new_val: int) -> list:
    X_LIM = conways_variables["X_LIM"]
    Y_LIM = conways_variables["Y_LIM"]
    if x > X_LIM:
        return mutate_grid_value_at_xy(x - X_LIM, y, new_val)
    elif y > Y_LIM:
        return mutate_grid_value_at_xy(x, y - X_LIM, new_val)
    elif x < 0:
        return mutate_grid_value_at_xy(x + X_LIM, y, new_val)
    elif y < 0:
        return mutate_grid_value_at_xy(x, y + Y_LIM, new_val)
    conways_grid[x][y] = new_val
    return conways_grid


def access_val_at_xy(x: int, y: int, grid: list) -> int:
    X_LIM = conways_variables["X_LIM"]
    Y_LIM = conways_variables["Y_LIM"]
    if x >= X_LIM:
        return access_val_at_xy(x - X_LIM, y, grid)
    elif y >= Y_LIM:
        return access_val_at_xy(x, y - X_LIM, grid)
    elif x < 0:
        return access_val_at_xy(x + X_LIM, y, grid)
    elif y < 0:
        return access_val_at_xy(x, y + Y_LIM, grid)
    return grid[x][y]


def count_neighbors(x: int, y: int, grid: list) -> int:
    neighbor_count = 0
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            neighbor_count += access_val_at_xy(x + x_offset, y + y_offset, grid)
    return neighbor_count - access_val_at_xy(x, y, grid)


def step():
    conways_grid_copy = deepcopy(conways_grid)
    X_LIM = conways_variables["X_LIM"]
    Y_LIM = conways_variables["Y_LIM"]
    for x in range(X_LIM):
        for y in range(Y_LIM):
            mutate_grid_value_at_xy(
                x, y, check_conways_condition(x, y, conways_grid_copy)
            )


def check_conways_condition(x: int, y: int, grid: list) -> int:
    cell_val = access_val_at_xy(x, y, grid)
    neighbors = count_neighbors(x, y, grid)
    if cell_val == 0:
        return 1 if neighbors == 3 else 0
    if cell_val == 1:
        return 1 if neighbors == 2 or neighbors == 3 else 0
    return 0


def pretty_print_grid() -> str:
    for row in conways_grid:
        print("".join([str(x) for x in row]))


def test_conways():
    conways_init(10, 10)
    mutate_grid_value_at_xy(5, 5, 1)
    mutate_grid_value_at_xy(5, 6, 1)
    mutate_grid_value_at_xy(5, 7, 1)
    mutate_grid_value_at_xy(4, 7, 1)
    mutate_grid_value_at_xy(3, 6, 1)

    X_LIM = conways_variables["X_LIM"]
    Y_LIM = conways_variables["Y_LIM"]
    for i in range(0, 30):
        step()
        pretty_print_grid()
        print()
