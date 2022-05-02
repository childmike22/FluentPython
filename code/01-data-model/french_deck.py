import collections
from random import choice, shuffle


Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self.cards = [Card(rank, suit) for suit in self.suits
										for rank in self.ranks]


	def __len__(self):
		return len(self.cards)


	def __getitem__(self, position):
		return self.cards[position]


	def shuffle_cards(self):
		shuffle(self.cards)



beer_card = Card('7', 'diamonds')
print(beer_card)



# Create our full deck of cards

full_deck = FrenchDeck()
print(len(full_deck))

# access the first and last cards (should be a 2 of spades first and an ace of hearts last)

print(full_deck[0])
print(full_deck[-1])


# pick a random choice from the deck
print(choice(full_deck))


# lets use slicing to see the first 4 cards in our deck!
print(full_deck[0:4])

# loop through our cards and only print kings
for ind, card in enumerate(full_deck):
	if card.rank == 'K':
		print(ind, card)


# full deck of cards is a list (see below commented out line)
# print(type(full_deck.cards))

print(Card('A', 'hearts') in full_deck)
print(Card('A', 'fake_suit') in full_deck)



# lets rank the suits (starting with making the spades the most powerful)
suit_vals = {'spades':3, 
				'hearts': 2,
				'diamonds': 1, 
				'clubs': 0}

def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_vals) + suit_vals[card.suit]


# for card in sorted(full_deck, key=spades_high):
# 	print(card)

print(FrenchDeck.ranks)


# own trial and error here

words = ['cat', 'mouse', 'rat', 'alligator', 'eel']


def random_word_ranking(word):
	if 'm' in word:
		return 150
	elif 'a' in word:
		return 12
	else: 
		return 0




for word in sorted(words, key=random_word_ranking):
	print(word)



# time to play around with shuffling my cards
print("\n\n\nFIRST 5 CARDS PRE-SHUFFLE: ")
for card in full_deck.cards[0:5]:
	print(card)

full_deck.shuffle_cards()

print("\n\n\nFIRST 5 CARDS POST-SHUFFLE: ")
for card in full_deck.cards[0:5]:
	print(card)
