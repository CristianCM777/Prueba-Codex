print("Calculadora básica")

a = int(input("Número 1: "))
b = int(input("Número 2: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)

if b != 0:
    print("División:", a / b)
else:
    print("No se puede dividir entre cero")
