#testing suites
import test
import ch6ex

def testdn():
    print("now testing dn")
    test.testy(ch6ex.day_name((-1) == "string"))

def testnd():
    print("now_testing nd")
    test.testy(ch6ex.name_day(("bad user input") == "not valid"))

def testrd():
    print("now testing rd")
    test.testy(ch6ex.return_day("sunday", 2)=="tuesday")

def testts():
    test.testy(ch6ex.to_seconds(2,30,10)==9010)


def testnew():
    test.testy(ch6ex.in_hours(9010)==2)

def testhypot():
    test.testy(ch6ex.hypotenuse(3, 4) == 5.0)

def testcompare():
    test.testy(ch6ex.compare(5, 4) == 1)

def testeo():
    test.testy(ch6ex.is_even(4)==True)
    test.testy(ch6ex.is_odd(4)==False)