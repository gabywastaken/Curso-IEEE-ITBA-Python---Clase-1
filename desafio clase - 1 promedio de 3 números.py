# Programa para calcular promedio

print("Cálculo de promedio de 3 números")

num_1 = int(input("Primer número: "))

num_2 = int(input("Segundo número: "))

num_3 = int(input("Tercer número: "))

promedio = (num_1 + num_2 + num_3) / 3
prom_f = format(promedio, '.2f')

print("El promedio de los tres números proporcionados es {}".format(prom_f))
