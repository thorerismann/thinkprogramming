#chapter 12 last exercise test suite
import test
import ch12ex

def testcw():
    test.testy(ch12ex.cleanword("!dkdjd%")=="dkdjd")
    test.testy(ch12ex.cleanword("what?") == "what")
    test.testy(ch12ex.cleanword("'now!'") == "now")
    test.testy(ch12ex.cleanword("?+='w-o-r-d!,@$()'") == "word")

def testhd():
    test.testy(ch12ex.has_dash("distance--but"))
    test.testy(not ch12ex.has_dash("several"))
    test.testy(ch12ex.has_dash("spoke--"))
    test.testy(ch12ex.has_dash("-yo-yo-"))

def testew():
    test.testy(ch12ex.extract_words("hey!")==["hey"])
    test.testy(ch12ex.extract_words("hey you")==["hey", "you"])
    test.testy(ch12ex.extract_words("Now is the time! 'Now', is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
    test.testy(ch12ex.extract_words("she tried to curtsey as she spoke--fancy") == ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])

def testwc():
    test.testy(ch12ex.wordcount("now", ["now","is","time","is","now","is","is"])==2)
    test.testy(ch12ex.wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
    test.testy(ch12ex.wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
    test.testy(ch12ex.wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)

def testws():
    test.testy(ch12ex.wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
    test.testy(ch12ex.wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
    test.testy(ch12ex.wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])

def testlw():
    test.testy(ch12ex.longestword(["a", "apple", "pear", "grape"]) == 5)
    test.testy(ch12ex.longestword(["a", "am", "I", "be"]) == 2)
    test.testy(ch12ex.longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
    test.testy(ch12ex.longestword([]) == 0)

testcw()
testhd()
testew()
testwc()
testws()
testlw()