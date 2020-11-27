#in lieu of the normal ch12 exercises (which are mainly word based, this file is the solution to the final
#exercise, exercise 8 of chapter 12 asking for a "word tools" file.
import string

def cleanword(x):
    clean = ""
    if has_dash:
        for i in x:
            if i == "-":
                clean += " "
            if i not in string.punctuation:
                clean += i
        return clean
    for i in x:
        if i not in string.punctuation:
            clean += i
    return clean

def has_dash(x):
    for i in x:
        if i == "-":
            return True
    return False

def extract_words(x):
    clean = cleanword(x)
    clean = clean.lower()
    return clean.split()

def wordcount(x,y):
    count = 0
    for i in y:
        if i == x:
            count+=1
    return count

def wordset(x):
    clean = ""
    return clean

def longestword(x):
    total = 0
    return total