import math


def distance(x1, y1, x2, y2):
    x_cord = (x2 - x1)**2
    y_cord = (y2 - y1)**2
    sums = x_cord + y_cord
    result = math.sqrt(sums)
    return result


# print distance(1, 2, 4, 6)

#radius = distance(1, 2, 4, 6)

def circle(x1, y1, x2, y2):
    radius = distance(x1, y1, x2, y2)
    return math.pi*(radius**2)

print circle(1, 2, 4, 6)
