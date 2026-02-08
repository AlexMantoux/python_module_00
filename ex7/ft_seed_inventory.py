def ft_seed_inventory(seed_type, quantity, unit):
    if (unit == "packets"):
        unit_word: str = quantity + " " + unit + " available"
    elif (unit == "grams"):
        unit_word: str = quantity + " " + unit + " total"
    elif (unit == "area"):
        unit_word: str = "covers " + quantity + " square meters"
    print(seed_type.title() + " seeds:", unit_word)
