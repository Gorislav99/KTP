count = int(input("\n Укажите количество элементов в списке: "))

mas = []
sum = 0

for i in range(count):
	mas.append(int(input()))
	if(mas[i] <= 10 and mas[i] >= 1):
		sum += mas[i]

print("\n Сумма всех чисел, от 1 до 10: ")
print(sum)
