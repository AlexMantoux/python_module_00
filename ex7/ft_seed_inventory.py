def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        unit_word: str = f"{quantity} {unit} available"
    elif unit == "grams":
        unit_word: str = f"{quantity} {unit} total"
    elif unit == "area":
        unit_word: str = f"covers {quantity} square meters"
    else:
        unit_word: str = f"{quantity} {unit}"
    print(seed_type.title() + " seeds: " + unit_word)
