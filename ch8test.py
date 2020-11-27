#testing suite for ch8 exercises
import test
import ch8ex

def testcc():
    test.testy(ch8ex.count_char("a","happy")==1)

def testcl():
    test.testy(ch8ex.count_lett("na","banana")==2)

def testrp():
    test.testy(ch8ex.rem_punct("hi!-You!")=="hiYou")

def testrev():
    test.testy(ch8ex.reverse("god")=="dog")

def testmir():
    test.testy(ch8ex.mirror("god")=="goddog")

def testpal():
    test.testy(ch8ex.palin("god")=="no")


testcc()
testcl()
testrp()
testrev()
testmir()
testpal()