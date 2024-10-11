import math
from array import array

# VARIANT 16.1
# a = float(input())
# b = float(input())
# h = float(input())
#
# def f(x):
#     return (math.pow(x, 3) + math.exp(x)) / (abs(math.sin(x)) + 0.12)
# x = a
# while x<=b:
#     y=f(x)
#     print("x=%.1f f(x)=%.3f"%(x,y))
#     x=x+h


# VARIANT 16.2
# a = float(input("Початкове значення:"))
# b = float(input("Кінцеве значення:"))
# h = float(input("Крок:"))
#
# if h == 0:
#     raise ValueError("Крок h не може бути нульовим")
# if a == b:
#     raise ValueError("Початкове і кінцеве значення не можуть бути однаковими")
#
# def f(x):
#     return (math.pow(x, 3) + math.exp(x)) / (abs(math.sin(x)) + 0.12)
# x = a
# while x<=b:
#     y=f(x)
#     print("x=%.1f f(x)=%.3f"%(x,y))
#     x=x+h

# VARIANT 16.3
a = float(input("Початкове значення:"))
b = float(input("Кінцеве значення:"))
h = float(input("Крок:"))

list = []
list1 = []
list1 = list
if h == 0:
    raise ValueError("Крок h не може бути нульовим")
if a == b:
    raise ValueError("Початкове і кінцеве значення не можуть бути однаковими")

def f(x):
    return (math.pow(x, 3) + math.exp(x)) / (abs(math.sin(x)) + 0.12)
x = a
while x<=b:
    y=f(x)
    list.append(y)
    print("x=%.1f f(x)=%.3f"%(x,y))
    x=x+h

print(list)
list1.sort()
list1.reverse()
print(list1)