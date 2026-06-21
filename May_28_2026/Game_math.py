from math import *
window_width = 800
window_height = 600
scaleFactor = 3

class Vector2:
    def __init__(self, x, y):
            self.x = x
            self.y = y
            
def GetDistance(lhs, rhs):
    return Vector2(lhs.x - rhs.x, lhs.y - rhs.y)

def GetMagnitude(lhs, rhs):
    distanceVec = GetDistance(lhs, rhs)
    return sqrt((distanceVec.x * distanceVec.x) + (distanceVec.y * distanceVec.y))
    
def GetAngle(lhs, rhs):
    distanceVec = GetDistance(lhs, rhs)
    return atan2(distanceVec.y, distanceVec.x)
    
def GetLength(single):
    return sqrt((single.x * single.x) + (single.y * single.y))

def Normalize(single):
    length = GetLength(single)
    dx = single.x / length
    dy = single.y / length
    return Vector2(dx, dy)

def RadialCollision(eLhs, eRhs):
    sumRadius = eLhs.radius + eRhs.radius
    mag = GetMagnitude(eLhs.position, eRhs.position)
    if sumRadius >= mag:
        return True
    return False
    
def AABB(eLhs, eRhs):
    #Entity Left Hand Side
    eLhs_LeftEdge = eLhs.position.x
    eLhs_RightEdge = eLhs.position.x + eLhs.size.x
    eLhs_TopEdge = eLhs.position.y
    eLhs_BottomEdge = eLhs.position.y + eLhs.size.y
    #Entity Right Hand Side
    eRhs_LeftEdge = eRhs.position.x
    eRhs_RightEdge = eRhs.position.x + eRhs.size.x
    eRhs_TopEdge = eRhs.position.y
    eRhs_BottomEdge = eRhs.position.y + eRhs.size.y
    
    if eLhs_LeftEdge > eRhs_RightEdge:
        return False
    if eLhs_RightEdge < eRhs_LeftEdge:
        return False
    if eLhs_TopEdge > eRhs_BottomEdge:
        return False
    if eLhs_BottomEdge < eRhs_TopEdge:
        eLhs.isGrounded = False
        return False
    if eLhs_BottomEdge > eRhs_TopEdge:
        eLhs.isGrounded = True
    return True

def RadialToBox(eC, eB):
    #Entity Box
    eb_Left_Edge = eB.position.x
    eb_Right_Edge = eB.position.x + eB.size.x
    eb_Top_Edge = eB.position.y
    eb_Bottom_Edge = eB.position.y + eB.size.y
    #Entity Cirlce
    eC_Left_Edge = eC.position.x - eC.diameter
    eC_Right_Edge = eC.position.x + eC.diameter
    eC_Top_Edge = eC.position.y - eC.diameter
    eC_Bottom_Edge = eC.position.y + eC.diameter
    
    if eC_Left_Edge > eb_Right_Edge:
        return False
    if eC_Right_Edge < eb_Left_Edge:
        return False
    if eC_Top_Edge > eb_Bottom_Edge:
        return False
    if eC_Bottom_Edge < eb_Top_Edge:
        return False
    return True
