def max_2(array):

    if len(array) < 2:

        return "Danh sách quá ngắn"

    Max = max(array[0], array[1])

    Max2 = min(array[0], array[1])

    for num in array[2:]:

        if num > Max:

            Max2 = Max

            Max = num

        elif num > Max2 and num < Max:

            Max2 = num

    return Max2
array = list(map(int ,input("nhap day so = ").split()))
result = max_2(array)
print(f"so lon thu 2 la: {result}")