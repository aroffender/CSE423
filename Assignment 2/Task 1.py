x1,y1,x2,y2= 100,100,200,200
def MPLDraw(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    d= 2*dy - dx
    incE= 2dy
    incNE=2*(dy-dx)


def zonefinder(x1,y1,x2,y2):
    zone = 0
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx)>=abs(dy):
        if dx>0 and dy>0:
            zone = 0
        elif dx<0 and dy>0:
            zone = 3
        elif dx<0 and dy<0:
            zone = 4
        elif dx>0 and dy<0:
            zone = 7
    else:
        if dx>0 and dy>0:
            zone = 1
        elif dx<0 and dy>0:
            zone = 2
        elif dx<0 and dy<0:
            zone = 5
        elif dx>0 and dy<0:
            zone = 6
    return zone


