def get_recipe_price(prices, optionals=None, **ingredients):
    # if there's no parameter optionals
    if optionals is None:
        optionals = []

    total_price = 0

    for ingredient, quantity in ingredients.items():
        if ingredient not in optionals:
            price_per_100g = prices.get(ingredient)
            if price_per_100g is not None:
                ingredient_price = (price_per_100g / 100) * quantity  # calculate the price according to the formula
                total_price += ingredient_price

    return total_price
