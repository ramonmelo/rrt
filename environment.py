
from shapely.geometry import Point, box

class Environment(object):

    def __init__(self, width, height):
        self.robots = []
        self.obstacles = []
        self.width = width
        self.height = height

        self.boundary = box(0, 0, width, height)

    def addRobot(self, x, y):
        poly = Point(x, y).buffer(30.0)

        self.robots.append(poly)

    def addObstable(self, x, y, width, height):
        self.obstacles.append(box(x, y, x + width, y + height))

    def colides(self, ref):

        point = Point(ref)

        if self.boundary.intersects(point):
            for robot in self.robots:
                if robot.intersects(point):
                    # print("robot colides")
                    return True

            for obstacle in self.obstacles:
                if obstacle.intersects(point):
                    # print("obstacle colides")
                    return True

        else:
            raise Exception('Invalid point')

        return False
