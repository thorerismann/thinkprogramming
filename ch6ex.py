#how to think like a computer programmer
#chapter 6 solutions to most problems
# problem 2
def day_name(x):
    name = "string"
    if (x<0 or x>6):
        print("outside of range")
        return ("not valid")
    if (x==0):
        name = "sunday"
    elif (x==1):
        name = "monday"
    elif (x==2):
        name = "tuesday"
    elif (x==3):
        name = "wednesday"
    elif (x == 4):
        name = "thursday"
    elif (x==5):
        name = "friday"
    else:
        name = "saturday"
    return name
# problem 3
def name_day(x):
    name = 0
    if (x=="sunday"):
        name = 0
    elif (x=="monday"):
        name = 1
    elif (x=="teusday"):
        name = 2
    elif (x=="wednesday"):
        name = 3
    elif (x == "thursday"):
        name = 4
    elif (x=="friday"):
        name = 5
    elif(x=="saturday"):
        name = 6
    else:
        print("outside of range")
        return ("not valid")
    return name

# problem 4 & 5.
def return_day(x,y):
    if(name_day(x) == "not valid"):
        print("invalid")
        return None
    y = int(y)
    x = name_day(x)
    y = y%7
    if(x+y <= 6):
        return day_name(x+y)
    else:
        return day_name((x + y) % 7)


#7 and 8
def to_seconds(x,y,z):
    y = y*60
    x = x*3600
    x = int(x)
    y = int(y)
    z = int(z)
    return x+y+z
#9
def in_hours(x):
    return int(x/3600)

def in_minutes(x):
    x = x - in_hours(x)*3600
    return int(x/60)

def in_seconds(x):
    x = x - in_hours(x)*3600 - in_minutes(x)*60
    return int(x)
#11
def compare(a,b):
    if(a>b):
        return 1
    if(a==b):
        return 0
    if(a<b):
        return -1
    else:
        return None

#12
def hypotenuse(x,y):
    return (x**2 + y**2)**0.5

#14 and #15
def is_even(x):
    if (x%2 == 0):
        return True
    return False
def is_odd(x):
    return not(is_even(x))
