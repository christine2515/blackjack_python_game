############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
import random
# from replit import clear

#ask if you want to play
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

player_cards = []
comp_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cont = "y"


########

def calc_score(card_deck):
  if len(card_deck) == 2 and sum(card_deck) == 21:
    return 0
  if 11 in card_deck and sum(card_deck) > 21:
    card_deck.remove(11)
    card_deck.append(1)
    return sum(card_deck)
  else:
    return sum(card_deck)
  

def blackjack():
  player_cards.append(cards[random.randint(0, 12)])
  player_cards.append( cards[random.randint(0, 12)])

  print(f"   Your cards: {player_cards}, current score: {sum(player_cards)}")

  comp_cards.append(cards[random.randint(0, 12)])
  comp_cards.append(cards[random.randint(0, 12)])

  print(f"   Computer's first card: {comp_cards[0]}")

########

def end_game():
  player_sum = calc_score(player_cards)
  comp_sum = calc_score(comp_cards)
  if play == "n":
    return
  print(f"   Your final hand: {player_cards}, final score: {sum(player_cards)}")
  print(f"   Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
  if player_sum > 21:
    print("You went over. You lose D:")
  elif comp_sum > 21:
    print("Your opponent went over. You win :D")
  elif player_sum < comp_sum:
    print("You lose :(")
  elif player_sum == comp_sum:
    print("wow, you tied!")
  elif player_sum > comp_sum:
    print("You win :)")

#######

if play == "y":
  print(art.logo)
  blackjack()
  cont = input("Type 'y' to get another card, type 'n' to pass: ")
elif play == "n":
  cont = "n"
else:
  cont = "y"



while cont == "y":
  player_cards.append(cards[random.randint(0, 12)])
  
  print(f"   Your cards: {player_cards}, current score: {calc_score(player_cards)}")
  print(f"   Computer's first card: {comp_cards[0]}")
  if calc_score(player_cards) > 21 or calc_score(comp_cards) > 21:
    cont == "n"
    break
  comp_cards.append(cards[random.randint(0, 12)])
  cont = input("Type 'y' to get another card, type 'n' to pass: ")


end_game()

while input("Do you want to play again? Type 'y' or 'n': ") == "y":
  clear()
  blackjack()
  cont = input("Type 'y' to get another card, type 'n' to pass: ")


#things to do:
#deal with aces