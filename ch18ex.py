import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(7)
alex.shape("turtle")

def fractalk(t,order,size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            fractalk(t, order - 1, size / 3)
            t.left(angle)

def fractale(t,order,size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [-80, 160, -80, 0]:
            fractale(t,order-1, size/2)
            t.left(angle)

def fractalst(t, order,size):
    if order==0:
        for i in range(0,3):
            t.fd(size)
            t.left(120)
    else:
        fractalst(t, size/2,order-1)
        t.forward(size/2)
        fractalst(t, size/2,order-1)
        t.bk(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(60)
        fractalst(t, size/2,order-1)
        t.left(60)
        t.bk(size/2)
        t.right(60)

fractalst(alex, 3,100)
##for i in range(3):
  ##  fractalk(alex,1,1000)
   ## alex.right(120)
##fractale(alex, 2, 100)

for i in range(4):
    fractale(alex,1,100)
    alex.right(90)

def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

def r_max(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

#directories
def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

#directories
def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)                    # Print the line
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname, prefix + "| ")

def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t



wn.mainloop()