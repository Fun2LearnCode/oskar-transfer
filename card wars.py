import random
myScore=0
yourScore=0
cards=["two","three","four","five","six","seven","eight","nine","ten","Jack","Queen","King","Ace"]
suit=["heart","spades","diamonds","clubs"]
while myScore < 10 and yourScore <10:
    flip = input("Press f to flip the card. ").lower()
    if(flip == "f"):
        myCard=random.choice(cards)
        yourCard=random.choice(cards)
        mySuit = random.choice(suit)
        yourSuit=random.choice(suit)
        print("My card is: " + myCard + " of " + mySuit + ". Your card is: " + yourCard + " of " + yourSuit + ".")
        if cards.index(myCard)>cards.index(yourCard):
            print("i win")
            myScore = myScore +1
            print("my score",myScore)
        elif cards.index(myCard)<cards.index(yourCard):
            print("You win!")
            yourScore = yourScore +1
            print ("your score",yourScore)
        elif cards.index(myCard)==cards.index(yourCard):
            print ("its a tie")
    else:
        flip = input("there was an error. Press f to flip the card. ").lower
