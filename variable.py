#Ejemplo de variables

lenguaje = 'Python'
x = 3.14
y = 3 + 2

#Asignar multiples valores
numero1, numero2 = 1, 2

numero1, numero2 = 2, 1

#x = None
print(x)

x +=10
print(x)

valor = 50
valor = valor / 2

print(valor)

rem = 4
y = y - (x + valor + rem)

print(y)

total = 158000000
print(f'El monto total es {total:,} euros'.replace(',','.'))

total_decimales = 158000000.57462
print(f'El monto total es: {total_decimales:,.2f} €')
