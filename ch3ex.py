#ch3 and turtle exercises
import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(1)
alex.shape("turtle")

#exercise 1
##for i in range(1000):
  ##  print("we love python")

#exercise 2
"""attributes: shape, size, color; methods: sms, call, file manager"""

#exercise 3 - skipped

#exercise 4 tess turns around 10 times and ends turngin 45° more

#exercise 5 a,b,c,d
"""xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0
product = 1
for i in range(len(xs)):
    print(xs[i])
    print(xs[i], xs[i]**2)
    total = total + xs[i]
    product = product*xs[i]
print(total)
print(product)"""
"""
#excercie 6 - note instead of octagon, user inputs number of sides of polygon to draw
for i in range(3):
    alex.left(120)
    alex.forward(10)

for i in range(4):
    alex.left(90)
    alex.forward(20)

for i in range(6):
    alex.left(60)
    alex.forward(30)

s = input("number of sides of polygon")
x = int(s)
for i in range(x):
    alex.left(360/x)
    alex.forward(40)


#exercise 7 & 8 (8 just the basics, I know I should %360 to print the true angle.
direction = 0
xs = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in xs:
    alex.left(i)
    alex.forward(100)
    direction = direction + i
    print(direction)
"""
#exercise 9 360 / 18 = 20°, see final for loop in exercise 6

#exercise 10 - all correct.

#exercise 11
alex.left(72)
alex.forward(100)
alex.left(-144)
alex.forward(100)
alex.left(-144)
alex.forward(100)
alex.left(-144)
alex.forward(100)
alex.left(-144)
alex.forward(100)


for c in ["yellow", "red", "purple", "blue"]:
    alex.color(c)
    alex.forward(50)
    alex.left(90)
wn.mainloop()