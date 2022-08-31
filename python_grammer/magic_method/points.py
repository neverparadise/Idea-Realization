__all__ = ['Points', 'add']

class Points:
    pt1 = (1, 2)
    pt2 = (-1, -2)

def add(pt1, pt2):
    x = pt1[0] + pt2[0]
    y = pt2[1] + pt2[1]
    return (x, y)
    
def sub(pt1, pt2):
    x = pt1[0] - pt2[0]
    y = pt2[1] - pt2[1]
    return (x, y)