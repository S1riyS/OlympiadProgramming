def get_trains_from_minutes(minutes, interval_length):
    full_cycles = minutes // (interval_length + 1)
    if minutes - full_cycles * (interval_length + 1) == interval_length:
        full_cycles += 1
    return full_cycles


a = int(input())
b = int(input())
n = int(input())
m = int(input())

first_way = n * a + (n - 1)
second_way = m * b + (m - 1)
max_time = max(first_way, second_way)
min_time = min(first_way, second_way)

check_1 = n == get_trains_from_minutes(min_time, a) and m == get_trains_from_minutes(min_time, b)
check_2 = n == get_trains_from_minutes(min_time, a) and m == get_trains_from_minutes(min_time, b)
if check_1 and check_2:
    print(min_time, max_time)
else:
    print(-1)

