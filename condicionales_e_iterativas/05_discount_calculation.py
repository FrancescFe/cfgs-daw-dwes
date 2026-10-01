INSERT_ORIGINAL_PRICE:str = "Indica el importe total de la compra:"
ERROR_MESSAGE:str = "Debes indicar un número mayor o igual a 0."
ORIGINAL_PRICE_MESSAGE:str = "Importe de la compra:"
DISCOUNT_MESSAGE:str = "Descuento:"
FINAL_PRICE_MESSAGE:str = "Precio final:"
EUR:str = "€"

while True:
    try:
        ticket:float = float(input(INSERT_ORIGINAL_PRICE))
        if ticket > 0:
            break
        print(ERROR_MESSAGE)
    except ValueError:
        print(ERROR_MESSAGE)

discount_amount:float = 0
final_price:float = ticket

if ticket < 50:
    print(f"{ORIGINAL_PRICE_MESSAGE} {ticket:.2f} {EUR}")
    print(DISCOUNT_MESSAGE + " sin descuento")
    print(FINAL_PRICE_MESSAGE, final_price, EUR)
elif ticket <= 99.99:
    discount_amount = ticket * 0.05
    final_price = ticket - discount_amount
    print(f"{ORIGINAL_PRICE_MESSAGE} {ticket:.2f} {EUR}")
    print(f"{DISCOUNT_MESSAGE} {discount_amount:.2f} {EUR}")
    print(f"{FINAL_PRICE_MESSAGE} {final_price:.2f} {EUR}")
elif ticket <= 199.99:
    discount_amount = ticket * 0.1
    final_price = ticket - discount_amount
    print(f"{ORIGINAL_PRICE_MESSAGE} {ticket:.2f} {EUR}")
    print(f"{DISCOUNT_MESSAGE} {discount_amount:.2f} {EUR}")
    print(f"{FINAL_PRICE_MESSAGE} {final_price:.2f} {EUR}")
else:
    discount_amount = ticket * 0.15
    final_price = ticket - discount_amount
    print(f"{ORIGINAL_PRICE_MESSAGE} {ticket:.2f} {EUR}")
    print(f"{DISCOUNT_MESSAGE} {discount_amount:.2f} {EUR}")
    print(f"{FINAL_PRICE_MESSAGE} {final_price:.2f} {EUR}")
