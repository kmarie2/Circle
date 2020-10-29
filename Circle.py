"""
Here are some examples of the circle-overlap problem,
in which we give the "x", "y", and radius for one circle and then the other,
and need to know if there are any points that line in/on both circles.
(Note that we don't allow a circle with negative radius.)


# An obvious overlap (Sample answer #3 got this wrong):
# 3 is broken
>>> circleOverlap(100,100,30, 125,100,30)
True

# An obvious non-overlap (Sample answer #1 gets this one wrong):
# 1 is broken
>>> circleOverlap(100,100,30, 225,100,30)
False

# An example copied from the "Console" window during a run of overlap-test-graphics
# 3 is broken
>>> circleOverlap( 160 ,  152 ,  82.8070045346 ,  198 ,  167 ,  93.813645063 )
True

# I think this example of my test suite is wrong because I used the x's, y's, and r's on Desmos, a graphing interface to visualize it.
# The second circle has a much smaller radius and it is away from the first circle because of its x and y.
# Because of that, the circles are not overlapping.
# 1 is broken
>>> circleOverlap(20,25,10, 36,32,6)
False

# 3 is broken
>>> circleOverlap(15,10,5, 14,12,7)
True

# I also used the x's, y's, and r's on Desmos; both circles are too small with its x's,y's, and especially the r's.
# Because of that, there is distance between them, thus, the circles are not overlapping.
# 1 is broken
>>> circleOverlap(5,5,2.5, 2,3,1)
False

# I also used the x's, y's, and r's on Desmos; both circles are too far away from each other, based  on its x's,y's.
# Because of that, there is distance between them, thus, the circles are not overlapping.
# 3 is broken
>>> circleOverlap(20,15,5, 10,5,5)
False

# 3 is broken
>>> circleOverlap(11,9,7, 14,12,8)
True


"""

from math import *
from Logic import *
    
def circleOverlap(x1: float,y1: float,r1: float,x2: float,y2: float,r2: float) -> bool:
    precondition(r1 >= 0 and r2 >= 0)
    # postcondition: return true iff there exists x,y in both circular regions, including being on the edge

    MODE: str = 'mine'  # set to 'test samples' or 'mine'
    
    if MODE =='mine':
        distance: float = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        if distance <= r1 + r2:
            return True
        else:
            return False
    elif MODE =='test samples':
        from CircleSamples import circleOverlapSamples
# the line below only works in the QuaCS lab computers
#        from sample_answers.cs105.Intersect.CircleSamples import circleOverlapSamples
        answer: bool = circleOverlapSamples(x1,y1,r1,x2,y2,r2)
        return answer
    else:
        print('ERROR: You need to set MODE correctly in circleRectangleOverlap in circleRectangle.py')
        raise Exception

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()


