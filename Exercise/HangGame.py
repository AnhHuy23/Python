import random  # Để chọn từ ngẫu nhiên
from collections import Counter  # Để đếm số lượng ký tự trong chuỗi

# Danh sách các loại trái cây
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

# Chuyển chuỗi thành danh sách
someWords = someWords.split(' ')

# Chọn một từ ngẫu nhiên trong danh sách
word = random.choice(someWords)

# Kiểm tra nếu chạy chương trình trực tiếp
if __name__ == '__main__':
    print('Đoán từ! GỢI Ý: Đây là tên một loại trái cây')

    # In ra dấu gạch dưới tương ứng với số ký tự trong từ
    for i in word:
        print('_', end=' ')
    print()

    playing = True  # Biến kiểm tra trạng thái chơi
    letterGuessed = ''  # Chuỗi lưu các chữ cái đã đoán
    chances = len(word) + 2  # Số lượt đoán cho phép = số ký tự + 2
    correct = 0  # Đếm số ký tự đúng
    flag = 0  # Cờ báo hiệu đã đoán xong từ chưa

    try:
        # Vòng lặp đoán chữ cái
        while (chances != 0) and flag == 0:
            print()
            chances -= 1  # Giảm số lượt sau mỗi lần đoán

            try:
                guess = str(input('Nhập một chữ cái để đoán: '))
            except:
                print('Vui lòng chỉ nhập một chữ cái!')
                continue

            # Kiểm tra tính hợp lệ của dữ liệu nhập vào
            if not guess.isalpha():
                print('Chỉ được nhập chữ cái!')
                continue
            elif len(guess) > 1:
                print('Chỉ được nhập MỘT chữ cái!')
                continue
            elif guess in letterGuessed:
                print('Bạn đã đoán chữ này rồi!')
                continue

            # Nếu đoán đúng chữ có trong từ
            if guess in word:
                # Đếm số lần chữ đó xuất hiện trong từ
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # Thêm chữ vào danh sách đã đoán

            # In ra trạng thái hiện tại của từ
            for char in word:
                # Nếu chữ này đã được đoán đúng và chưa đoán hết từ
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # Nếu đã đoán đủ các chữ của từ
                elif (Counter(letterGuessed) == Counter(word)):
                    print("Từ cần đoán là: ", end=' ')
                    print(word)
                    flag = 1  # Báo hiệu đã đoán xong
                    print('Chúc mừng, bạn đã chiến thắng!')
                    break  # Thoát khỏi vòng lặp for
                else:
                    print('_', end=' ')  # In dấu gạch dưới cho chữ chưa đoán

        # Nếu hết lượt mà chưa đoán được
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('Bạn đã thua! Thử lại lần sau nhé..')
            print('Từ cần đoán là: {}'.format(word))

    # Nếu người dùng nhấn Ctrl + C
    except KeyboardInterrupt:
        print()
        print('Tạm biệt! Hẹn gặp lại.')
        exit()
