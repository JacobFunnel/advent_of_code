with open("input/11.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    seats = set()
    for y, line in enumerate(lines):
        for x, state in enumerate(line):
            if state == "L":
                seats.add((x, y))
    return seats


def becomes_occupied(seat, vacancies, occupancies):
    x, y = seat
    occupied_neighbors = 0
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            neighbor = (x + a, y + b)
            if neighbor != seat and neighbor in occupancies:
                occupied_neighbors += 1

    if seat in vacancies:
        if occupied_neighbors == 0:
            return True
        else:
            return False
    else:
        if occupied_neighbors >= 4:
            return False
        else:
            return True


def next_board(vacancies, occupancies):
    future_vacancies, future_occupancies = set(), set()
    for seat in vacancies | occupancies:
        if becomes_occupied(seat, vacancies, occupancies):
            future_occupancies.add(seat)
        else:
            future_vacancies.add(seat)
    return future_vacancies, future_occupancies


def final_occupancy(seats):
    future_vacancies, future_occupancies, occupancies = seats, set(), set()
    while not occupancies or future_occupancies != occupancies:
        vacancies, occupancies = future_vacancies, future_occupancies
        future_vacancies, future_occupancies = next_board(vacancies, occupancies)
    return occupancies


seats = parse(lines)
print(len(final_occupancy(seats)))
