#code provided in ch14 & selected exercise solutions at the end.
#note that accompanying words files should be filled with words to test the solutions before running!

import string


# given a file name x of clean string text, returns a list of all words (separater = " ")
def load_file(x):
    """ Read words from filename, return list of words. """
    newfile = open(x)
    content = newfile.read()
    newfile.close()
    return content.split()


# given a string x returns a sorted list of all words in lower case separated by space and cleaned of punctuation.
def text_to_word(x):
    my_subs = x.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
                          "abcdefghijklmnopqrstuvwxyz                                          ")
    clean = x.translate(my_subs)
    target = clean.split()
    return target


# removes duplicates adjascent to each other in sorted list x
def remove_adj_dups(x):
    result = []
    newel = None
    for i in x:
        if i != newel:
            result.append(i)
            newel = i
    return result


# conducts a binary search alogorithm given a sorted list x and target y.
def bsearch(x, y):
    lb = 0
    ub = len(x)
    while True:
        if lb == ub:
            return -1
        mindex = (lb + ub) // 2
        mitem = x[mindex]

        if mitem == y:
            return mindex
        if mitem < y:
            lb = mindex + 1
        else:
            ub = mindex


# returns the list of words in y that are not in list of words x.
def fwords(x, y):
    result = []
    for i in y:
        if bsearch(x, i) < 0:
            result.append(i)
    return result


# given a file name x reads the file and returns result of text_to_word
def book_words(x):
    newfile = open(x)
    clean = newfile.read()
    newfile.close()
    return text_to_word(clean)

#merges two sorted lists into 1 sorted list.
def merge(x, y):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(x):
            result.extend(y[yi:])
            return result
        if yi >= len(ys):
            result.extend(x[xi:])
            return result
        if x[xi] <= y[yi]:
            result.append(x[xi])
            xi += 1
        else:
            result.append(y[yi])
            yi += 1

#exercise 1

#exercise 1a
def fwords_two(x, y):
    result = []
    for i in y:
        if bsearch(x, i) > 0:
            result.append(i)
    return result

#exercise 1c
def fwords_three(x, y):
    result = []
    for i in y:
        if bsearch(x, i) < 0:
            result.append(i)
    return result

#exercise 1b
def fwords_four(x,y):
    result = []
    for i in x:
        if bsearch(y, i) < 0:
            result.append(i)

#exercise 1d
def fwords_four(x,y):
    result = x + y
    result.sort()
    result = remove_adj_dups(result)
    return result

#exercise 1e
def merge_two(x, y):
    result = []
    i = 0
    element = None
    while True:
        if i >= len(x):
            return x
        if len(y) == 0:
            return x
        if bsearch(y, x[i]) >= 0:
            for j in range(len(y)):
                if y[j-1] == x[i]:
                    del y[j-1]
                    del x[i]
                    continue
            print(x)
            print(y)
        else:
            i += 1


#code to test 1e
x = [1,1,2,3,4,5]
y = [1,2,3,4,6,8]
print(merge_two(x,y))

#code to test 1a-1d
#new_words = book_words("ch14-words1.txt")
#new_new_words = book_words("ch14-words2.txt")
#new_words.sort()
#new_new_words.sort()
#print(fwords_four(new_words,new_new_words))

