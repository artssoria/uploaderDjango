def suma (a,b):
    return a + b
def resta (a,b):
    return a - b
def multi (a,b):
    return a * b
def div (a,b):
    return a / b

while True:
    try:
        operacion = int(input("Seleccione la operacion que desea realizar: " "\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n"))
        if(operacion <=4 and operacion >0):
            break
        
    except:
        print("ingrese un entero válido")



num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el primer numero: "))

if operacion == 1:
    resultado = suma(num1, num2)
elif operacion == 2:
    resultado = resta(num1, num2)
elif operacion == 3:
    resultado = multi(num1, num2)
elif operacion == 4:
    resultado = div(num1, num2)

else:
    print("operacion no válida")

print(f"Resultado: {resultado}")