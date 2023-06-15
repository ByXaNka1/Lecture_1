def calculate_lace_length(a, b, l, N):
    horizontal_length = (N - 1) * b
    vertical_length = (N - 1) * a
    lace_length = horizontal_length + vertical_length + l
    return lace_length
a = int(input("Введіть відстань між рядами (a): "))
b = int(input("Введіть відстань між дірочками в ряді (b): "))
l = int(input("Введіть довжину вільного кінця шнурка (l): "))
N = int(input("Введіть кількість дірочок у кожному ряду (N): "))
result = calculate_lace_length(a, b, l, N)
print("Довжина шнурка: ", result)