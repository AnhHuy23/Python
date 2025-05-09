def Sum_even(n):

    sum = 0

    for i in range(2, n+1, 2):

        sum += i

    return sum

# Thay đổi giá trị của n theo mong muốn

n = int(input ("Nhập giá trị của n: "))

result = Sum_even(n)

print(f"Tổng của các số chẵn từ 1 đến {n} là: {result}")