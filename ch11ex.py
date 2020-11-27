#11.5
def add_vectors(x,y):
    for i in range(len(x)):
         x[i-1] = x[i-1] + y[i-1]
    return x

#11.6
def scalar(x,y):
    for i in range(len(x)):
        x[i-1] = y*x[i-1]
    return x

#11.7
def dot_prod(x,y):
    total = 0
    for i in range(len(x)):
        total = total + x[i-1]*y[i-1]
    return total
#11.8
def cross_prod(x,y):
    total = []
    subtotal1 = x[1]*y[2] - x[2]*y[1]
    subtotal2 = x[2]*y[0] - x[0]*y[2]
    subtotal3 = x[0]*y[1] - x[1]*y[0]
    total.append(subtotal1)
    total.append(subtotal2)
    total.append(subtotal3)
    return total