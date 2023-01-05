with open("input/13.txt", "r") as f:
    lines = f.read().split("\n")
    earliest_dp = int(lines[0])
    buses = [int(entry) for entry in lines[1].split(",") if entry != "x"]


def find_fastest_bus(departure, schedules):
    wait_times = [schedule - (departure % schedule) for schedule in schedules]
    shortest_wait = min(wait_times)
    fastest_bus_id = schedules[wait_times.index(shortest_wait)]
    return shortest_wait * fastest_bus_id


print(find_fastest_bus(earliest_dp, buses))
