import time

def sum_for_loop(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def sum_while_loop(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum

n_values = [10, 100, 1000, 10000, 100000]

for n in n_values:
    time_start = time.time()
    sum_for_loop(n)
    time_end = time.time()
    time_total_for = time_end - time_start

    time_start = time.time()
    sum_while_loop(n)
    time_end = time.time()
    time_total_while = time_end - time_start

    print(f"n = {n}")
    print(f"For loop execution time: {time_total_for} seconds")
    print(f"While loop execution time: {time_total_while} seconds")
    print("\n")