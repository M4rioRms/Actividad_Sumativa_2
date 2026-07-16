peso = int(input("Dime tu peso en kg: "))
altura = int(input("Dime tu altura en cm: "))

print("Tu IMC aproximado es:", (peso * 10000) // (altura ** 2))