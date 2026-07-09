def apply_discount(amount, discount_percent):
    if amount <= 0:
        raise ValueError("amount must be > 0")

    if discount_percent < 0 or discount_percent > 80:
        raise ValueError("discount must be between 0 and 80")

    discounted = amount * (1 - discount_percent / 100)
    return round(discounted, 2)
