import random

card_category = {'heart', 'diamonds', 'spade', 'club'}
card_value = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
               11: 'J', 12: 'Q', 13: 'K'}
deck = [(card, category) for category in card_category for card in card_value]

def card_value(card):
    if card[0] in [11, 12, 13]:
        return 10
    elif card[0] == 1:
        return 11
    else:
        return int(card[0])
    
random.shuffle(deck)
player_cards = [deck.pop(), deck.pop()]  # Người chơi được chia 2 lá bài
dealer_cards = [deck.pop(), deck.pop()]  # Dealer chỉ lật một lá bài

while True:
    player_score = sum(card_value(card) for card in player_cards) # Tính tổng điểm của người chơi
    if player_score > 21 and any(card[0] == 1 for card in player_cards):
        player_score -= 10  # Nếu có A và tổng điểm > 21, giảm 10 điểm
    dealer_score = sum(card_value(card) for card in dealer_cards) # Tính tổng điểm của dealer
    if dealer_score > 21 and any(card[0] == 1 for card in dealer_cards):
        dealer_score -= 10  # Nếu có A và tổng điểm > 21, giảm 10 điểm
    print(f"Your cards: {player_cards}, score: {player_score}") # In ra bài của người chơi
    print(f"Dealer's cards: {dealer_cards[0]}, score: {card_value(dealer_cards[0])}") # In ra bài của dealer
    if player_score > 21: # Kiểm tra nếu người chơi đã thua
        print(f"Score: {player_score}")
        print("You busted! Dealer wins.")
        break
    choice = input("Do you want to hit or stand? (h/s): ").lower() # Nhập lựa chọn của người chơi
    if choice == 'h':
        new_card = deck.pop() 
        player_cards.append(new_card) 
    elif choice == 's':
        while dealer_score < 17:
            new_card = deck.pop()
            dealer_cards.append(new_card)
            dealer_score += card_value(new_card)
            
            print(f"Dealer's cards: {dealer_cards}, score: {dealer_score}")

        if dealer_score > 21:
            print(f"Dealer's score: {dealer_score}")
            print("Dealer busted! You win.")
            break
        elif player_score > dealer_score:
            print(f"Your score: {player_score}")
            print(f"Dealer's score: {dealer_score}")
            print("You win!")  
            break 
        elif player_score < dealer_score:
            print(f"Your score: {player_score}")
            print(f"Dealer's score: {dealer_score}")
            print("Dealer wins.")
            break
        else:
            print(f"Your score: {player_score}")
            print(f"Dealer's score: {dealer_score}")
            print("It's a tie!")
            break     
    else:
        print("Invalid choice. Please enter 'h' or 's'.") 
        continue
    
    




