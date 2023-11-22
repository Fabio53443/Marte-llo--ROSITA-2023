#V1:

def forwardCareful(units):
    for i in range(units):
        d = obstacleDistance(0)
        if d < 1:
            turn(30)
            forwardCareful(1)
            turn(-30)
            forwardCareful(1)
        forward(1)


#v2
def forwardCareful(units):
    for i in range(2*units):
        d = obstacleDistance(0)
        if d < 1:
            turn(30)
            forwardCareful(int(d+1))
            turn(-60)
            forward(0.5)
            forwardCareful(1)
        forward(0.5)

