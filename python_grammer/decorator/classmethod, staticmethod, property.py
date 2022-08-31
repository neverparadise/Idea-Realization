class Point3D:
    count = 0 # 클래스 변수

    def __init__(self, x, y, z):
        self.coord = (x, y, z)
        Point3D.add_point()    

    def __del__(self):
        del self.coord
        del_point(Point3D)

    @property
    def x(self):
        return self.coord[0]

    @property
    def x(self, value):
        self.coord[0] = value

    @property
    def y(self):
        return self.coord[1]

    @property
    def z(self):
        return self.coord[2]

@classmethod
def add_point(cls):
    count += 1

@classmethod
def del_point(cls):
    count -= 1

@classmethod
def get_num_points(cls):
    return cls.count

pt1 = Point3D(1, 2, 3)
pt2 = Point3D(4, 6, 5)
Point3D.get_num_points()