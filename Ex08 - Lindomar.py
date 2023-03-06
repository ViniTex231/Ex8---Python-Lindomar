num_list = []
pares_list = []
impares_list = []

i = 0

while i < 7:
    num = int(input("Digite um número: "))
    num_list.append(num)
    i +=1
for num in num_list:
    if num % 2 == 0:
        pares_list.append(num)
    else:
        impares_list.append(num)


pares_list.sort()
impares_list.sort()

print(f"Valores pares: ", pares_list)
print(f"Valores impares: ", impares_list)

