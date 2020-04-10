import sys
import re

class Poker:
    """docstring for Poker."""

    def __init__(self, arg):
        super(Poker, self).__init__()
        self.arg = arg



def main():

    suits = ["C", "D", "H", "S"]

    valuesDict = {}

    for i in range(1, 14):
        for j in range(len(suits)):
            valuesDict.update({str(i + 1) + suits[j]: i**3 + j})


    #for j in range(len(suits)):
        #valuesDict.update({"1" + suits[j]: max(valuesDict.values()) + j + 1})

    print(valuesDict)

    cards = []

    for line in sys.stdin:

        hand = re.split("/|-|\s", line.strip().upper())

        if(len(hand) != 5):
            print("Incorrect number of cards")
            break
            #exit()

        print(hand)

        # can't have two of the same card
        # formatting non-number cards

        handDict = {}
        for card in hand:
            cardVal = valuesDict[card]
            handDict.update({card : cardVal})

        #print(handDict)
        sortedHand = sorted(handDict.items(), key= lambda cardValue: cardValue[1])

        finalString = ""
        for card in sortedHand:
            finalString = finalString + card[0] + " "

        finalString = finalString.strip()
        print(finalString)




if __name__ == '__main__':
    main()
