import random
print("Doan so trong khoang 1 den 100 \nBan co 6 lan doan")

number_guess = random.randrange(100)
chances = 6
guess_counter = 0

while guess_counter < number_guess:
    guess_counter +=1
    my_guess = int(input("Nhap so: "))
    
    if my_guess == number_guess:
        print(f"Ban da chon dung so {my_guess}")
        break

    elif guess_counter >= chances and my_guess != number_guess :
        print(f"da het luot doan va so can tim la: {number_guess}")
        break
    
    elif my_guess < number_guess:
        print("Be hon so can tim")
    
    elif my_guess > number_guess:
        print("Lon hon so can tim")
