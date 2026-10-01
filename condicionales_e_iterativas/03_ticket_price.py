INSERT_AGE:str = "Indica tu edad:"
ERROR_MESSAGE:str = "Debes indicar un número entero mayor o igual a 0."
PRICE_MESSAGE:str = "El precio de la entrada es:"
EUR:str = "€"

while True:
    try:
        age: int = int(input(INSERT_AGE))
        break
    except ValueError:
        print(ERROR_MESSAGE)

price:int = 0

if age < 0:
    print("Edad no válida")
elif age < 5:
    print(PRICE_MESSAGE + "GRATUITA")
elif age <= 12:
    price = 5
    print(PRICE_MESSAGE, price, EUR)
elif age <= 64:
    price = 9
    print(PRICE_MESSAGE, price, EUR)
else:
    price = 6
    print(PRICE_MESSAGE, price, EUR)
