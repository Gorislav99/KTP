import math

print(" Введите значение a:")
a = float(input())
print(" Введите значение b:")
b = float(input())
print(" Введите значение c:")
c = float(input())
print(" Введите значение d:")
d = float(input())
print(" Введите значение k:")
k = float(input())

if(b == 0 or a == 0):
        print("\n При вычислении происходит деление на ноль!")
else:
        result = (a*a-b*b*b-c*c*c*a*a)*(b-c+c*(k-d/(b*b*b)))-math.pow((k/b-k/a)*c,2)-20000  
        if(result < 0):
                result *= -1
        print("\n Результат вычислений: ")
        print(result)
