import sys
import re

# COSC326 Etude-7 Poker Hands
# Author: Darcy Knox
# Date: April 2020

# 1. Creates a dictionary of card: value pairs with correct relative values.
# 2. Reads the input and checks that it can be correctly separated into 5 parts,
#    and that there are no leading or trailing whitespace.
# 3. Replace cards that have multiple key interpretations (e.g. 12 -> Q) with
#    the key that is used in the values dictionary.
# 4. Iterate through the hand checking that the card is an actual card, and
#    that there are no duplicate cards within the hand.
# 5. Check the card against a regex pattern.
# 6. Get the value of the card and add it to a dictionary that contains all
#    cards in the current hand.
# 7. Use the built in sorted() function to sort the hand (by the values for each
#    card) into an array of key:value tuples.
# 8. Print the key of each card in the hand.
#
# >  If any of the checks fail, the program stops processing and outputs the
#    invalid input as it was entered.

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


    cards = []

    for line in sys.stdin:

        finalString = ""
        validHand = True

        inputLine = line.replace("\n", "", 1)

        if (inputLine != inputLine.strip()):
            print("Invalid: " + inputLine)
            validHand = False


        if (validHand):

            line = line.strip().upper()

            hand = line.split("/")

            if (len(hand) == 1):
                hand = line.split("-")
                if (len(hand) == 1):
                    hand = line.split(" ")
                    if (len(hand) != 5):
                        print("Invalid: " + inputLine)
                        validHand = False
                elif (len(hand) != 5):
                    print("Invalid: " + inputLine)
                    validHand = False
            elif (len(hand) != 5):
                print("Invalid: " + inputLine)
                validHand = False


        if (validHand):

            hand = [card.replace("10", "T")
                        .replace("11", "J")
                        .replace("12", "Q")
                        .replace("13", "K")
                        .replace("1", "A") for card in hand]

            handDict = {}
            for card in hand:
                validCard = True
                if card in handDict:
                    print("Invalid: " + inputLine)
                    validCard = False
                    validHand = False
                    break
                elif not card in valuesDict:
                    print("Invalid: " + inputLine)
                    validCard = False
                    validHand = False
                    break

                validCardPattern = re.compile(r'^([1-9]|(10|11|12|13)|[TJQKA])[CDHS]$')
                validCard = validCardPattern.match(card)

                if validCard:
                    cardVal = valuesDict[card]
                    handDict.update({card : cardVal})
                else:
                    validHand = False
                    break


            if (validHand):
                sortedHand = sorted(handDict.items(), key= lambda cardValue: cardValue[1])

                for card in sortedHand:
                    finalString = finalString + card[0] + " "

                finalString = finalString.strip().replace("T", "10")
                # T is the only key that needs to be changed back

                print(finalString)



if __name__ == '__main__':
    main()
