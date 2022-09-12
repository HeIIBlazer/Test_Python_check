import math
import sys

try:
    A = int(input("Введите число A: "))
    if A==0:
        print("A не может быть 0")
        sys.exit(1)
except ValueError:
    print("")

try:
    B = int(input("Введите число B: "))
except ValueError:
    print("")

try:
    C = int(input("Введите число C: "))
except ValueError:
    print("")

try:
    D = B*B-4*A*C
except NameError:
    print("БЫЛИ ВВЕДИНЫ НЕ ПРАВИЛЬНЫЕ СИМВОЛЫ!")
    sys.exit(1)

print("D =", D)

if D < 0:
    print("Корней нет!")
    sys.exit(1)
else:
    X1 = (-B+math.sqrt(D))/(2*A)
    X2 = (-B-math.sqrt(D))/(2*A)

print("X1 =", X1)
print("X2 =", X2)
