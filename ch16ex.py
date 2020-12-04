class Point:
    """Declaration of the Class"""

    def __init__(self, x=0, y=0):
        """create a new point at the origin, default is (0,0) else provide initial values"""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def reflect_x(self):
        return Point((-1)*self.x, self.y)

    def slope_from_origin(self):
        if self.x == 0:
            return None
        return self.y/self.x

    def get_line_to(self,pointy):
        if pointy.x-self.x == 0:
            return (None, None)
        m = (pointy.y-self.y)/(pointy.x-self.x)
        b = self.y - m*self.x
        return (m, b)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def find_circle_mid(self,point2,point3):
        constant1 = point2.x**2 + point2.y**2 - self.x**2-self.y**2
        constant2 = point3.x**2 + point3.y**2 - self.x**2-self.y**2
        constant3 =  2*(point3.y-self.y-((point2.y-self.y)*(point3.x-self.x)/(point2.x-self.x)))
        b = (constant2 - constant1/(point2.x-self.x))/constant3
        a = (constant1 - b * 2 * (point2.y-self.y))/(2 * (point2.x-self.x))
        return (a,b)

    def same(self, pointy):
        return (self.x == pointy.x and self.y == pointy.y)

class Rectangle:
    def __init__(self, posn, w,h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "{0}, {1}, {2}".format(self.corner, self.width, self.height)

    def grow(self, w,h):
        """Change height and width of the rectangle"""
        self.width += w
        self.height += h

    def move(self, x,y):
        self.corner.x += x
        self.corner.y += y


    def area(self):
        """Exercise 1"""
        return self.height * self.width

    def perimeter(self):
        "Exercise 2"
        return 2*(self.height + self.width)

    def flip(self):
        "Exercise 3"
        temp = self.width
        self.width = self.height
        self.height = temp

    def inside(self, pointy):
        "Exercise 4 - author reverses convention for rectangle naming in tests he gives. "
        if pointy.x < self.corner.x:
            return False
        if pointy.y < self.corner.y:
            return False
        if pointy.y >= self.corner.y + self.height:
            return False
        if pointy.x >= self.corner.x + self.width:
            return False
        else:
            return True

def getcorners(recty):
    """Get corners for Exercise 5"""
    corners = []
    Point1 = recty.corner
    Point2 = Point(recty.corner.x + recty.width, recty.corner.y)
    Point3 = Point(recty.corner.x + recty.width, recty.corner.y + recty.height)
    Point4 = Point(recty.corner.x, recty.corner.y + recty.height)
    corners.append(Point1)
    corners.append(Point2)
    corners.append(Point3)
    corners.append(Point4)
    return corners

def bounding(r1, r2):
    """Exercise 5: Lemme - if two rectangles overlap, then at least one corner of each rectange overlaps"""
    r1_corners = getcorners(r1)
    r2_corners = getcorners(r2)
    for i in r1_corners:
        if r2.inside(i):
            return True
    for j in r2_corners:
       if r1.inside(j):
           return True
    return False


r = Rectangle(Point(1,1),2,2)
s = Rectangle(Point(2,2),1,1)
t = Rectangle(Point(4,4),1,1)

print(bounding(r,s))
print(bounding(r,t))