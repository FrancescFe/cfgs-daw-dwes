bank_balance:float = 1000.0
transaction:int = 0

deposit:float = 0
withdraw:float = 0

countDeposits:int = 0
countWithdrawals:int = 0

totalDepositAmount:float = 0
totalWithdrawalAmount:float = 0

ATM_MENU:str = '''====== CAJERO AUTOMÁTICO ======
1. Consultar saldo
2. Ingresar dinero
3. Retirar dinero
4. Salir
'''

while transaction!=4:
    print()
    print(ATM_MENU)

    try:
        transaction = int(input("Seleccione operación a realizar (1, 2, 3, 4):"))
    except ValueError:
        print("Operación Inválida.")
        continue

    if transaction == 1:
        print(f"Su saldo actual es {bank_balance:.2f}€")

    elif transaction == 2:
        try:
            deposit = float(input("Indique cantidad a ingresar:"))
        except ValueError:
            print("Operación cancelada. No ha introducido un número.")
            continue

        if deposit > 0:
            bank_balance += deposit
            countDeposits += 1
            totalDepositAmount += deposit
            print(f"Operación realizada con éxito. Saldo resultante: {bank_balance:.2f}€")
        else:
            print("Operación cancelada. El número ha de ser positivo.")
        

    elif transaction == 3:
        try:
            withdraw = float(input("Indique cantidad a retirar:"))
        except ValueError:
            print("Operación cancelada. No ha introducido un número.")
            continue

        if withdraw <= 0:
            print("Operación cancelada. El número ha de ser positivo.")

        elif bank_balance > withdraw:
            bank_balance -= withdraw
            countWithdrawals += 1
            totalWithdrawalAmount += withdraw
            print(f"Operación realizada con éxito. Saldo resultante: {bank_balance:.2f}€")

        else:
            print("Operación cancelada. Saldo insuficiente.")

    elif transaction != 4:
        print("Operación inválida.")

print()
print("====== FIN TRANSACCIONES ======")
print(f"Saldo final: {bank_balance:.2f}€")
print(f"Ingresos realizados: {countDeposits}")
print(f"Retiradas realizadas: {countWithdrawals}")
print(f"Total dinero ingresado: {totalDepositAmount:.2f}€")
print(f"Total dinero retirado: {totalWithdrawalAmount:.2f}€")
print("====== HASTA LA PRÓXIMA ======")
