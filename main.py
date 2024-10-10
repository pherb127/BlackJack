"""
The goal of this project is to code a BlackJack game.

1. We will first start by create the class Deck and intentiate the entire deck of cards, the rank of each card. We will also code = some basic functions such as suffling the deck and picking a card from the deck.

2. 
"""

import random


class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):  #str is used to return a string to a print statement
    return f"{self.rank['rank']} of {self.suit}"


class Deck:

  def __init__(self):
    self.cards = []
    suits = ["spades", "clubs", "hearts", "diamonds"]
    list_of_ranks = ["A"] + [i for i in range(1, 11)] + ["J", "Q", "K"]
    ranks = []

    for rank in list_of_ranks:
      if rank == "A":
        value = 11
      elif rank == "J" or rank == "Q" or rank == "K":
        value = 10
      else:
        value = int(rank)
      ranks.append({"rank": rank, "value": value})

    for suit in suits:
      for rank in ranks:
        self.cards.append(Card(suit, rank))

#We shuffle our deck of cards

  def shuffle(self):
    if len(self.cards) > 1:
      random.shuffle(self.cards)


#We distribute a card to the player

  def deal(self, number):
    cards_delt = []
    for i in range(number):
      if len(self.cards) > 0:
        card = self.cards.pop()
        cards_delt.append(card)
    return cards_delt


class Hand:

  def __init__(self, dealer = False):
    self.cards = []
    self.value = 0
    self. dealer = dealer

  def add_card(self, card_list):
    self.cards.extend(card_list)

  def calculate_value(self):
    self.value = 0
    has_ace = False
    for card in self.cards:
      self.value += int(card.rank["value"])
      if card.rank["rank"] == "A":
        has_ace = True
      
    if has_ace and self.value > 21:
      self.value -= 10
          
  def get_value(self):
    self.calculate_value()
    return self.value

  def is_blackjack(self):
    return self.get_value == 21

  def display(self, show_dealer_cards = False):
    print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
    for index, card in enumerate(self.cards):
      if index==0 and self.dealer \
      and not show_dealer_cards and not self.is_blackjack():
        print("hidden")
      else:
        print(card)

    if not self.dealer:
      print("Value :", self.get_value())
    print()


class Game:
  def play(self):
    game_number = 0
    games_to_play = 0

    while games_to_play <= 0:
      try:
        games_to_play = int(input("How many games do you want to play? "))
      except:
        print("You must enter a number.")

    while game_number < games_to_play:
      game_number += 1
      deck = Deck()
      deck.shuffle()

      player_hand = Hand()
      dealer_hand = Hand(dealer = True)

      for i in range(2):
        player_hand.add_card(deck.deal(1))
        dealer_hand.add_card(deck.deal(1))

      print()
      print("*" * 30)
      print(f"Game {game_number} of {games_to_play}")
      player_hand.display()
      dealer_hand.display()

      if self.check_winner(player_hand, dealer_hand):  #we go on to the next iteration AKA next game
        continue

      choice = ""
      while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
        choice = input("Please choose 'hit' or 'stand': ").lower()
        print()
        while choice not in ["h", "s", "hit", "stand"]:
          choice = input("Please choose 'hit' or 'stand': (or H/S)").lower()
          print()
          
        if choice in ["hit", "h"]:
          player_hand.add_card(deck.deal(1))
          player_hand.display()
          
      if self.check_winner(player_hand, dealer_hand):  #we go on to the next
        continue

      player_hand_value = player_hand.get_value()
      dealer_hand_value = dealer_hand.get_value()

      while dealer_hand_value < 17:
        dealer_hand.add_card(deck.deal(1))
        dealer_hand_value = dealer_hand.get_value()

      dealer_hand.display(show_dealer_cards = True)
      
      if self.check_winner(player_hand, dealer_hand):
        continue

      print("Final Results")
      print("Your hand:", player_hand_value)
      print("Dealer's hand:", dealer_hand_value)

      self.check_winner(player_hand, dealer_hand, True)

    print("\nThanks for playing!")



  
  def check_winner(self, player_hand, dealer_hand, game_over = False):
    if not game_over:
      if player_hand.get_value() > 21:
        print("You busted. Dealer wins!")
        return True
      elif dealer_hand.get_value() > 21:
        print("Dealer busted. You win!")
        return True
      elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
        print("Both players have blackjack. Tie!")
        return True
      elif dealer_hand.is_blackjack():
        print("Dealer has blackjack. Dealer wins!")
        return True
      elif player_hand.is_blackjack():
        print("You have blackjack. You win!")
        return True
    else:
      if player_hand.get_value() > dealer_hand.get_value():
        print("You win!")
      elif player_hand.get_value() == dealer_hand.get_value():
        print("Tie!")
      else:
        print("Dealer wins!")
      return True
    return False



g = Game()
g.play()


