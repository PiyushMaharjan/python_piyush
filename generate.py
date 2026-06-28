import random

coin=random.choice(["heads","tails"])
print(coin)

#unsing from

from random import choice

coin = choice(["heads", "tails"])
print(coin)


#using randint
import random

number = random.randint(1,10)
print(number)


#shuffle
import random

cards = ["jack", "king","queen"]

random.shuffle(cards)
for card in cards:
    print(card)