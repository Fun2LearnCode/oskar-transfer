import random
suits=["hearts","spades","diamonds","clubs"]
cards=["two","three","four","five","six","7","8","9","10","Jack","Queen","king","ace"]
myCard=random.choice(cards)
yourCard=random.choice(cards)
print("My card is:"+myCard+".Your card is:"+yourCard)
if cards.index(myCard)>cards.index(yourCard):
    print("I win!")
if cards.index(myCard)<cards.index(yourCard):
    print("You win!")

