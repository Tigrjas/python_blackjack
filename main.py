from classes.person import Dealer, Player
import time
import sys

# ------------- System adjustments ---------------- #
TIME_SLEEP = 1
TIME_TEXT_ANIMATION = 0.05

TEST = True

if TEST == True:
    TIME_SLEEP = 0
    TIME_TEXT_ANIMATION = 0

# ------------- System adjustment ends ----------- #


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(TIME_TEXT_ANIMATION)


def game(player, dealer):

    # Check if player has money
    if player.money < 0:
        return

    # Initial game setup
    delay_print(
        f"The game of blackjack has started! Your dealer will be {dealer}!\n\n")
    time.sleep(TIME_SLEEP)

    # Betting Phase
    print("--- Betting Phase ---\n")
    delay_print("Everyone start your antes\n")
    time.sleep(TIME_SLEEP)

    ante = player.ante()

    delay_print(f"\n{player} has wagered ${ante}. Good luck!\n\n")

    # Dealing phase
    print("--- Dealing Phase ---\n")
    player.cards = [dealer.draw_card()[0], dealer.draw_card()[0]]
    dealer.cards = [dealer.draw_card()[0], dealer.draw_card()[0]]

    def hand_value(cards: list) -> int:
        face_cards = ["jack", "queen", "king"]
        total = 0
        for card in cards:
            if card == "ace" and total + 11 <= 21:
                total += 11
            elif card == "ace":
                total += 1
            elif card in face_cards:
                total += 10
            else:
                total += int(card)
        return total

    # Check for Blackjack
    if hand_value(player.cards) == 21 and hand_value(dealer.cards) == 21:
        return player.ante
    elif hand_value(player.cards) == 21:
        return player.ante * 2
    elif hand_value(dealer.cards) == 21:
        return 0

    print(f"Your hand: {player.cards[0]}, {
          player.cards[1]} ({hand_value(player.cards)})")
    print(f"Dealer's hand: face down card, {player.cards[1]}")


def main():
    dealer = Dealer("Kevin")
    player = Player("Jason")
    game(player, dealer)


if __name__ == "__main__":
    main()
    # test()
