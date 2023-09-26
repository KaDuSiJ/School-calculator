a = int(input())
b = int(input())

plus_1 = a + b
minus_2 = a - b
multiply_3 = a * b
divide_4 = a / b

print("Chose action:")
print("1 is plus")
print("2 is minus")
print("3 is multiply")
print("4 is divide")

c = int(input())
print(type(c))
if c == 1:
    print(plus_1)
if c == 2:
    print(minus_2)
if c == 3:
    print(multiply_3)
if c == 4:
    print(divide_4)
