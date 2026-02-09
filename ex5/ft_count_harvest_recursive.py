def ft_count_harvest_recursive(n: int = 1, n_max: int = 0) -> None:
    if (n_max == 0):
        n_max = int(input("Days until harvest: "))
    if (n <= n_max):
        print("Day ", n)
        ft_count_harvest_recursive(n + 1, n_max)
    else:
        print("Harvest time !")
