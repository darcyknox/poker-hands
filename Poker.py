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

    # create values dictionary
    for i in range(1, 14):
        for j in range(len(suits)):
            if (i == 9):
                valuesDict.update({"T" + suits[j]: i**3 + j})
            elif (i == 10):
                valuesDict.update({"J" + suits[j]: i**3 + j})
            elif (i == 11):
                valuesDict.update({"Q" + suits[j]: i**3 + j})
            elif (i == 12):
                valuesDict.update({"K" + suits[j]: i**3 + j})
            elif (i == 13):
                valuesDict.update({"A" + suits[j]: i**3 + j})
            else:
                valuesDict.update({str(i + 1) + suits[j]: i**3 + j})

    #for j in range(len(suits)):
        #valuesDict.update({"1" + suits[j]: max(valuesDict.values()) + j + 1})

    #print(valuesDict)


    cards = []

    for line in sys.stdin:

        # get line of input and convert to an array of cards (hand)
        hand = re.split("/|-|\s", line.strip().upper())

        if(len(hand) != 5):
            print("Invalid: " + line)
            break
            #exit()

        #print("Old hand: " + str(hand))

        hand = [card.replace("10", "T") for card in hand]
        hand = [card.replace("11", "J") for card in hand]
        hand = [card.replace("12", "Q") for card in hand]
        hand = [card.replace("13", "K") for card in hand]
        hand = [card.replace("1", "A") for card in hand]

        #print("New hand: " + str(hand))

        # can't have two of the same card
        # formatting non-number cards

        handDict = {}
        for card in hand:
            cardVal = valuesDict[card]
            handDict.update({card : cardVal})

        #print(handDict)
        sortedHand = sorted(handDict.items(), key= lambda cardValue: cardValue[1])

        #print(sortedHand)

        finalString = ""
        for card in sortedHand:
            finalString = finalString + card[0] + " "

        finalString = finalString.strip().replace("T", "10")
        print(finalString)




if __name__ == '__main__':
    main()
