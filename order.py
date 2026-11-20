
def calculate_discount(price, discount):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")

    return price * discount / 100


def calculate_gst(amount, gst_rate=18):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if gst_rate < 0 or gst_rate > 100:
        raise ValueError("GST rate must be between 0 and 100")

    return amount * gst_rate / 100


def calculate_order_total(price, discount, gst_rate=18):
    discount_amount = calculate_discount(price, discount)
    discounted_price = price - discount_amount
    gst_amount = calculate_gst(discounted_price, gst_rate)

    return discounted_price + gst_amount


if __name__ == "__main__":
    price = 1000
    discount = 10

    discount_amount = calculate_discount(price, discount)
    gst_amount = calculate_gst(price - discount_amount)
    total = calculate_order_total(price, discount)

    print("Original Price:", price)
    print("Discount Amount:", discount_amount)
    print("GST Amount:", gst_amount)
    print("Final Order Total:", total)
