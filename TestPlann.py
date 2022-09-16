import math
import sys
x=0

while x != 1:
    try:
        A = float(input("Введите число A: "))
        if A==0:
            print("")
            print("A не может быть 0!")
            print("")
            continue
        else:
            print("")
            break
            
    except ValueError:
        print("")
        print("Введите цифру!")
        print("")
        continue
    
print("")
print("----------------------")
        

while x != 1:
    try:
        B = float(input("Введите число B: "))
        print("")
        break
    except ValueError:
        print("")
        print("Введите цифру!")
        print("")
        continue

print("")
print("----------------------")

while x != 1:
    try:
        C = float(input("Введите число C: "))
        print("")
        break
    except ValueError:
        print("")
        print("Введите цифру!")
        print("")
        continue

print("")
print("----------------------")

D = B*B-4*A*C


print("D =", D)

if D == 0:
    X = (-B)/(2*A)
    print("X = ", X)
    
elif D < 0:
    print("Корней нет!")
    sys.exit(1)

else:
    X1 = (-B+math.sqrt(D))/(2*A)
    X2 = (-B-math.sqrt(D))/(2*A)
    print("X1 =", X1)
    print("X2 =", X2)
