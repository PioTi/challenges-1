from data import DICTIONARY, LETTER_SCORES
import os
import operator


def load_words():
    """Load dictionary into a list and return list"""
    fn = os.path.join(os.path.dirname(__file__), DICTIONARY)
    print(fn)
    dictlist = []
    with open(fn) as dictfile:
        dictlist = [line.strip('\r\n') for line in dictfile.readlines()]

    return dictlist


dictList1 = load_words()


def calc_word_value(wordused):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0

    for letter in (wordused):

        if letter in LETTER_SCORES.keys():

            score += LETTER_SCORES[letter]

        else:
            print('do not match')
    return score


def max_word_value(listOfWords=dictList1):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    dictionarynew = {}
    for list1 in listOfWords:
        scoredict = 0

        for letter in list1:
            if letter.upper() in LETTER_SCORES.keys():
                scoredict += LETTER_SCORES[letter.upper()]

            dictionarynew[list1] = scoredict

    value = max(dictionarynew.keys(), key=(lambda k: dictionarynew[k]))

    return value


if __name__ == "__main__":
    # pass # run unittests to validate
    #dictList1 = []
    print(len(dictList1))
    score1 = calc_word_value('Pious'.upper())
    print('score1 word is {}'.format(score1))
    TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
    maxword = max_word_value(TEST_WORDS)
    print('max word is {}'.format(maxword))
    maxword = max_word_value()
    print('max word from dictionary is  {}'.format(maxword))

    #print('the dictionary list is :{}'.format(dictList1))
