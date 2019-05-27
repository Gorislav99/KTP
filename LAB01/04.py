count = int(input("\n Укажите количество элементов в списке: "))

mas = []

for i in range(count):
	mas.append(int(input()))

min = mas[0]

for i in range(count):
	if mas[i] < min:
		min = mas[i]

print("\n Минимальный элемент массива: ")
print(min)
