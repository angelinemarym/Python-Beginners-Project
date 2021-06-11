num1 = float(input("Masukkan angka pertama: "))
op = input("Masukkan operator: ")
num2 = float(input("Masukkan angka kedua: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Operator tidak valid")