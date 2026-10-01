INSERT_LEAP_YEAR:str = "Introduce un año:"
ERROR_MESSAGE:str = "El año debe ser un número entero mayor que 0."

while True:
    try:
        year: int = int(input(INSERT_LEAP_YEAR))
        if year > 0:
            break
        print(ERROR_MESSAGE)
    except ValueError:
        print(ERROR_MESSAGE)

isDivisibleByFour:bool = year % 4 == 0
isDivisibleByOneHundred:bool = year % 100 == 0
isDivisibleByFourHundred:bool = year % 400 == 0

isLeapYear:bool = isDivisibleByFour and (not isDivisibleByOneHundred or isDivisibleByFourHundred)

if isLeapYear:
    print("The year is leap")
else:
    print("The year is not leap")