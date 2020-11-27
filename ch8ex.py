#8.1
# y; g; 9; Myst; True; True; True; True; True

#8.2
def prefixes():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if(letter== "O" or letter == "Q"):
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)
#prefixes()

#8.3
def count_char(x,y):
    count = 0
    for i in y:
        if(i == x):
            count += 1
    return count

#8.4
def count_lett(x,y):
    count = 0
    gui = "yes"
    while gui == "yes":
        count = y.find(x)
        print(count)
        gui = input("continue? yes/no")
    return count

#8.5
x = '''"Eh bien la chose importante à vous dire, citation de Michelet, qui est un grand écrivain, mais mon estime pour l'historien n'a cessé de décroître ; Michelet vous affirme ceci, "Ce qu'il importe de savoir, c'est à quel point les idées d'intérêt furent étrangères au mouvement de 89"'''
import string
def rem_punct(x):
    clean = ""
    for i in x:
        if i not in string.punctuation:
            clean += i
    return clean

def ex85(x):
    counte = 0
    countw = 0
    x = x.split()
    for i in x:
        countw += 1
        if (i.find("e") > 0):
            counte+=1
    return "Yout text contains {0} words, of which {1}, ({2}%) contain an e".format(countw, counte, int((counte/countw)*100))

print(ex85(rem_punct(x)))

#8.6
def mult_table(y,x):
    clean = ""
    for i in range(1,x+1):
        if(y*i>9 and y*i < 100):
            clean = clean + "   " + str(y*i)
        elif(y*i>=100):
            clean = clean + "  " + str(y*i)
        else:
            clean = clean + "    " + str(y*i)
    return clean
def print_table(x):
    top1 = "       "
    top2 = "-----"
    clean = ""
    for i in range(1, x+1):
        if(i>8):
            top1 = top1 + str(i) + "   "
            top2 += "-----"
        else:
            top1 = top1 + str(i) + "    "
            top2 += "-----"
    print(top1)
    print(top2)

    for i in range(1, x+1):
        if (i>9):
            print("{0}:".format(i)+mult_table(i,x))
        else:
            print("{0}: ".format(i) + mult_table(i, x))

print_table(5)

#8.7
def reverse(x):
    clean = ""
    for i in range(len(x)):
        clean = clean + x[len(x)-1-i]
    return clean

#8.8
def mirror(x):
    return x + reverse(x)

#8.9
def remove(x,y):
    clean = ""
    for i in y:
        if not(x==i):
            clean += i
    return clean

#8.10
def palin(x):
    clean = ""
    if len(x)%2 == 0:
        clean = x[:int(len(x)/2)]
    else:
        clean = x[:int(len(x)/2)] + x[int(len(x)/2)]
        x = x[:int(len(x)/2)] + x[int(len(x)/2)] + x[int(len(x)/2):]
    if x == mirror(clean):
        return "yes"
    else:
        return "no"

