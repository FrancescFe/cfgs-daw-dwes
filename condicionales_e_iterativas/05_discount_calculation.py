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
    discount_amount = 0
elif ticket < 100:
    discount_amount = ticket * 0.05
elif ticket < 200:
    discount_amount = ticket * 0.10
else:
    discount_amount = ticket * 0.15

final_price: float = ticket - discount_amount

print(f"{ORIGINAL_PRICE_MESSAGE} {ticket:.2f} {EUR}")

if discount_amount == 0:
    print(f"{DISCOUNT_MESSAGE} sin descuento")
else:
    print(f"{DISCOUNT_MESSAGE} {discount_amount:.2f} {EUR}")

print(f"{FINAL_PRICE_MESSAGE} {final_price:.2f} {EUR}")
