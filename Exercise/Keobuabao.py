import random

print('Trò chơi kéo búa bao bắt đầu')

while True:

    print('Hãy chọn \n 1 - Kéo \n 2 - Búa \n 3 - Bao')

    choice = int(input('Hãy chọn lựa chọn của bạn: '))

    while choice > 3 or choice < 1:
        choice = int(input('Sai lỗi cũ pháp \n Hãy chọn lại lựa chọn của bạn: '))

    if choice == 1:
        choice_name = 'Kéo'
    elif choice == 2:
        choice_name = 'Búa'
    else:
        choice_name = 'Bao'

    computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        comp_choice_name = 'Kéo'
    elif computer_choice == 2:
        comp_choice_name = 'Búa'
    else:
        comp_choice_name = 'Bao'

    print(f'Lựa chọn của máy tính là: {comp_choice_name}')

    if choice == computer_choice:
        print('Draw')
    elif (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 3) or (choice == 3 and computer_choice == 1):
        print(f'Bạn ra {choice_name} va máy tính ra {comp_choice_name} \n You Loss')
    elif (choice == 1 and computer_choice == 3) or (choice == 2 and computer_choice == 1) or (choice == 3 and computer_choice == 2):
        print(f'Bạn ra {choice_name} va máy tính ra {comp_choice_name} \n You Win')

    print('Bạn có muốn chơi lại không ? (y/n)')
    ans =  input().lower()
    if ans == 'n':        
        break