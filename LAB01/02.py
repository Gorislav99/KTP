count = int(input("Укажите количество элементов в массиве: "))

mas = []

for i in range(count):
	mas.append(input())

print("\n Элементы, стоящие на нечетных местах: ")

for i in range(count):
	if (i % 2 == 1):
		print(mas[i])
