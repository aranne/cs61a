""" When playing this game, you should connect to the database cards.db to see what cards do we have in hand in order to decide whether to get another card.
That is to say you should type in two terminal:
$ python blackjack_card_grame.py         ---> this is to start the game.

$ sqlite3 cards.db
$ SELECT * FROM cards;                  ---> to see what cards you already have.
(if you have finished playing one game, you can type this in the next game:)
$ SELECT * FROM cards where who <> "Discard";
"""
import random
import sqlite3

points = {'A': 1, 'J': 10, 'Q': 10, 'K':10}            # points is a dictionary of cards.
points.update({n: n for n in range(2, 11)})            # adds more elements in a dictionary from another dictionary

def hand_score(hand):
    """Total score for a hand."""
    total = sum([points[card] for card in hand]) # sum all card value in hand
    if total <= 11 and 'A' in hand: # 'A' is a special card and can represent two values: 1 or 11
        return total + 10
    return total

db = sqlite3.Connection('cards.db') # Create a database card.db and connect it with db.
sql = db.execute # sql is the execute function now.
sql('DROP TABLE IF EXISTS cards') # refresh table cards
sql('CREATE TABLE cards(card, who);') # create table card with columns card and who.

def play(card, who):
    """Play a card so that the player can see it."""
    sql('INSERT INTO cards VALUES (?, ?)', (card, who)) # insert (card, who) into the database and commit.
    db.commit()

def score(who):
    """Compute the hand score for the player or dealer."""
    cards = sql('SELECT * from cards where who = ?;', [who]) # get all the cards in the database that all have the same [who].
    return hand_score([card for card, who in cards.fetchall()]) # fetch all cards from database.

def bust(who):
    """Check if the player or dealer went bust."""
    return score(who) > 21

player, dealer = "Player", "Dealer"

def play_hand(deck): # you should have a deck.
    """Play a hand of Blackjack."""
    play(deck.pop(), player) # get the first card to the player.
    play(deck.pop(), dealer) # get the second to the dealer
    play(deck.pop(), player) # and then player
    hidden = deck.pop() # and next card will be hidden.

    while 'y' in input("Hit? ").lower(): # if y (means yes) is the user's input line, we deal the player another card.
        play(deck.pop(), player) # deal the player another card.
        if bust(player):
            print(player, "went bust!")
            return

    play(hidden, dealer) # Now it's dealer' turn, at the first we should face up the hidden card and insert into database

    while score(dealer) < 17:
        play(deck.pop(), dealer)
        if bust(dealer):
            print(dealer, "went bust!")
            return

    print(player, score(player), "and", dealer, score(dealer)) # we can compare the score of player and dealer.

deck = list(points.keys()) * 4    # create a deck, which have 4 cards of same type.
random.shuffle(deck) # shuffle the deck
while len(deck) > 10:
    print('\nDealing...')
    play_hand(deck) # start playing hands.
    sql('UPDATE cards SET who="Discard";') # after game, discard all cards in database.
