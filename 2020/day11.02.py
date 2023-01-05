with open("input/11.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    seats, floor = set(), set()
    for y, line in enumerate(lines):
        for x, state in enumerate(line):
            if state == "L":
                seats.add((x, y))
            else:
                floor.add((x, y))
    return seats, floor


def move(seat, direction):
    return tuple(map(sum, zip(seat, direction)))


def has_visible_occupied_neighbor(seat, direction, vacancies, occupancies, floor):
    grid = vacancies | occupancies | floor
    visible_neighbor = move(seat, direction)
    while True:
        if visible_neighbor in grid:
            if visible_neighbor in occupancies:
                return True
            elif visible_neighbor in vacancies:
                return False
            else:
                visible_neighbor = move(visible_neighbor, direction)
        else:
            return False


def becomes_occupied(seat, vacancies, occupancies, floor):
    occupied_visible_neighbors = 0
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            if not a == b == 0:
                direction = (a, b)
                if has_visible_occupied_neighbor(seat, direction, vacancies, occupancies, floor):
                    occupied_visible_neighbors += 1

    if seat in vacancies:
        if occupied_visible_neighbors == 0:
            return True
        else:
            return False
    else:
        if occupied_visible_neighbors >= 5:
            return False
        else:
            return True


def next_board(vacancies, occupancies, floor):
    future_vacancies, future_occupancies = set(), set()
    for seat in vacancies | occupancies:
        if becomes_occupied(seat, vacancies, occupancies, floor):
            future_occupancies.add(seat)
        else:
            future_vacancies.add(seat)
    return future_vacancies, future_occupancies


def final_occupancy(seats, floor):
    future_vacancies, future_occupancies, occupancies = set(), seats, set()
    while not occupancies or future_occupancies != occupancies:
        vacancies, occupancies = future_vacancies, future_occupancies
        print_board(vacancies, occupancies, floor)
        future_vacancies, future_occupancies = next_board(vacancies, occupancies, floor)
    return occupancies


def print_board(vacancies, occupancies, floor):
    max_x, max_y = max(vacancies | occupancies | floor)
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if (x, y) in vacancies:
                line += "L"
            elif (x, y) in occupancies:
                line += "#"
            elif (x, y) in floor:
                line += "."
        print(line)
    print("")


seats, floor = parse(lines)
print(len(final_occupancy(seats, floor)))
