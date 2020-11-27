#testing suite for chapter 11 exercises
import test
import ch11ex

def testad():
    test.testy(ch11ex.add_vectors([1,2,3],[2,3,4])==[3,5,7])

def testsca():
    test.testy(ch11ex.scalar([1,2,3],4)==[4,8,12])

def testdot():
    test.testy(ch11ex.dot_prod([1,2,3],[1,2,3])==14)

def testcro():
    test.testy(ch11ex.cross_prod([1,2,3],[4,5,6])== [-3,6,-3])

testad()
testsca()
testdot()
testcro()