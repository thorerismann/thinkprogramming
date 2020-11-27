import test

import ch7ex

def testco():
    test.testy(ch7ex.count_odd([3, 4, 5, 6]) == 2)

def testce():
    test.testy(ch7ex.count_even([3, 4, 5, 6]) == 2)

def testsn():
    test.testy(ch7ex.sum_neg([3, -4, -5, 6]) == 9)

def testwl():
    test.testy(ch7ex.word_length(["happy", "sad", "cools", "r"]) == 2)

def testso():
    test.testy(ch7ex.sum_odd([3, 4, 5, 6]) == 3)

def testts():
    test.testy(ch7ex.to_sam(["happy", "sad", "sam", "r"]) == 2)

def testsqrt():
    test.testy(int(ch7ex.sqrt(30))==5)

testco()
testce()
testsn()
testwl()
testso()
testts()
testsqrt()