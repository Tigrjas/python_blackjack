from classes.deck import Deck


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Dealer(Person):
    deck = Deck()
    cards = []

    def draw_card(self):
        return self.deck.remove_card()

    def reset_dealer(self):
        self.cards = []


class Player(Person):
    cards = []
    money = 10

    def ante(self):
        while True:
            ante = int(input(
                f"Your current balance: ${self.money}. \nHow much would you like to ante: "))
            if self.money == 0:
                print(f"Sorry you're out of money")
                break
            elif ante <= self.money:
                self.money -= ante
                return ante
            else:
                print(f"{ante} is greater than your current balance of {
                      self.money}. Please input a value lower than {self.money}.")
                continue

    def reset_player(self):
        self.cards = []
