INSERT_LEFT_OPERAND:str = "Escribe el primer número:"
INSERT_RIGHT_OPERAND:str = "Escribe el segundo número:"
ERROR_MESSAGE:str = "El nº debe ser entero."

while True:
    try:
        leftOperand:int = int(input(INSERT_LEFT_OPERAND))
        break
    except ValueError:
        print(ERROR_MESSAGE)

while True:
    try:
        rightOperand:int = int(input(INSERT_RIGHT_OPERAND))
        break
    except ValueError:
        print(ERROR_MESSAGE)


if leftOperand > rightOperand:
    print(leftOperand," es mayor que ", rightOperand)
elif leftOperand < rightOperand:
    print(rightOperand, " es mayor que", leftOperand)
else:
    print(leftOperand, " y ", rightOperand, " son iguales")