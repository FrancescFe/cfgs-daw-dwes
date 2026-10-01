INSERT_LEFT_OPERAND:str = "Escribe el primer número:"
INSERT_RIGHT_OPERAND:str = "Escribe el segundo número:"
INSERT_OPERATOR:str = "Indica la operación (+, -, *, /):"
OPERAND_ERROR_MESSAGE:str = "El nº debe ser entero."
OPERATOR_ERROR_MESSAGE:str = "Operación no válida."
ZERO_DIVISION_ERROR_MESSAGE:str = "No se puede dividir entre cero."

while True:
    try:
        leftOperand:int = int(input(INSERT_LEFT_OPERAND))
        break
    except ValueError:
        print(OPERAND_ERROR_MESSAGE)

while True:
    try:
        rightOperand:int = int(input(INSERT_RIGHT_OPERAND))
        break
    except ValueError:
        print(OPERAND_ERROR_MESSAGE)

while True:
    operator:str = input(INSERT_OPERATOR)
    if operator in ("+", "-", "*", "/"):
        break
    print(OPERATOR_ERROR_MESSAGE)

if operator == "+":
    print(leftOperand + rightOperand)
elif operator == "-":
    print(leftOperand - rightOperand)
elif operator == "*":
    print(leftOperand * rightOperand)
else:
    try:
        print(leftOperand / rightOperand)
    except ZeroDivisionError:
        print(ZERO_DIVISION_ERROR_MESSAGE)