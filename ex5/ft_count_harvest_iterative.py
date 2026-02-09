def ft_count_harvest_iterative() -> None:
    day_n: int = int(input("Days until harvest: "))
    for d in range(1, day_n + 1):
        print("Day", d)
    print("Harvest time !")
