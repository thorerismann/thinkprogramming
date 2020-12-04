#exercises for chapter 15

#ex 1/2/3/4/5 (for five have to assign p to a point on circle too)
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

#note this function requests three points not four. Three poitns is the minimum required to find (a,b)
#so why would anyone provide four points, let alone use four points in a calculation?
#thus, the solution uses three point. Could request 4 and throw 1 away otherwise :)
#also used self as one of the points!
    def find_circle_mid(self,point2,point3):
        constant1 = point2.x**2 + point2.y**2 - self.x**2-self.y**2
        constant2 = point3.x**2 + point3.y**2 - self.x**2-self.y**2
        constant3 =  2*(point3.y-self.y-((point2.y-self.y)*(point3.x-self.x)/(point2.x-self.x)))
        b = (constant2 - constant1/(point2.x-self.x))/constant3
        a = (constant1 - b * 2 * (point2.y-self.y))/(2 * (point2.x-self.x))
        return (a,b)


p = Point(0, -2)
print(p.distance_from_origin())
q = p.reflect_x()
print(q.x)
print(q.y)

print(p.get_line_to(Point(0,9)))
print(p.slope_from_origin())

center = p.find_circle_mid(Point(2,0),Point(0,1))
print(center)