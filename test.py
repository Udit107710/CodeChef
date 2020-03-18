def series(n):
    if n == 0 or n == 1:
        return n
    else:
        return 2*series(n-1) - 2*series(n-2)

def is_part_of_series():
    for i in range(0, 30):
        print(i, series(i))

is_part_of_series()