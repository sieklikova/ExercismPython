"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)
print(f'The value of the card is {value_of_card('2')}')
print(f'The value of the card is {value_of_card('5')}')
print(f'The value of the card is {value_of_card('8')}')
print(f'The value of the card is {value_of_card('A')}')
print(f'The value of the card is {value_of_card('10')}')
print(f'The value of the card is {value_of_card('J')}')
print(f'The value of the card is {value_of_card('Q')}')
print(f'The value of the card is {value_of_card('K')}')

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)

    if value_of_card_one > value_of_card_two:
        return card_one
    elif value_of_card_one < value_of_card_two:
        return card_two
    else:
        return card_one, card_two

print(f'The higher card is {higher_card('A','A')}')
print(f'The higher card is {higher_card('10','J')}')
print(f'The higher card is {higher_card('3','A')}')
print(f'The higher card is {higher_card('3','6')}')
print(f'The higher card is {higher_card('Q','10')}')
print(f'The higher card is {higher_card('4','4')}')
print(f'The higher card is {higher_card('9','10')}')
print(f'The higher card is {higher_card('6','9')}')
print(f'The higher card is {higher_card('4','8')}')

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    def current_value(card):
        if card in 'JQK': return 10
        if card == 'A': return 11
        return int(card)

    sum_of_both_cards = current_value( card_one) + current_value(card_two)

    if sum_of_both_cards + 11 <= 21:
        return 11
    else:
        return 1

print(f'The value of the ace card is {value_of_ace('2', '3')}')
print(f'The value of the ace card is {value_of_ace('3', '6')}')
print(f'The value of the ace card is {value_of_ace('5', '2')}')
print(f'The value of the ace card is {value_of_ace('8', '2')}')
print(f'The value of the ace card is {value_of_ace('5', '5')}')
print(f'The value of the ace card is {value_of_ace('Q', 'A')}')
print(f'The value of the ace card is {value_of_ace('10', '2')}')
print(f'The value of the ace card is {value_of_ace('7', '8')}')
print(f'The value of the ace card is {value_of_ace('J', '9')}')
print(f'The value of the ace card is {value_of_ace('K', 'K')}')
print(f'The value of the ace card is {value_of_ace('2', 'A')}')
print(f'The value of the ace card is {value_of_ace('A', '2')}')

def is_blackjack(card_one, card_two):

   ten_cards = ['10', 'J', 'Q', 'K']

   if card_one == 'A' and card_two in ten_cards:
    return True
   if card_two == 'A' and card_one in ten_cards:
    return True
   else:
    return False

print(f'The hand is a blackjack: {is_blackjack('A', 'K')}')
print(f'The hand is a blackjack: {is_blackjack('10', 'A')}')
print(f'The hand is a blackjack: {is_blackjack('10', '9')}')
print(f'The hand is a blackjack: {is_blackjack('A', 'A')}')
print(f'The hand is a blackjack: {is_blackjack('4', '7')}')
print(f'The hand is a blackjack: {is_blackjack('9', '2')}')
print(f'The hand is a blackjack: {is_blackjack('Q', 'K')}')

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)

    if value_of_card_one == value_of_card_two:
        return True
    else:
        return False
print(f'The hand can be split into two pairs: {can_split_pairs("Q", "K")}')
print(f'The hand can be split into two pairs: {can_split_pairs('6', '6')}')
print(f'The hand can be split into two pairs: {can_split_pairs('A', 'A')}')
print(f'The hand can be split into two pairs: {can_split_pairs('10', 'A')}')
print(f'The hand can be split into two pairs: {can_split_pairs('10', '9')}')

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    sum = value_of_card(card_one) + value_of_card(card_two)
    if sum == 9 or sum == 10 or sum == 11:
        return True
    else:
        return False

print(f'The hand can be doubled down: {can_double_down('A', '9')}')
print(f'The hand can be doubled down: {can_double_down('K', 'A')}')
print(f'The hand can be doubled down: {can_double_down('4', '5')}')
print(f'The hand can be doubled down: {can_double_down('A', 'A')}')
print(f'The hand can be doubled down: {can_double_down('10', '2')}')
print(f'The hand can be doubled down: {can_double_down('10', '9')}')
