from Projectile import *
from Game_math import *

class CollisionManager:
    def __init__(self, player):
        self.player = player
        self.lastPosition = Vector2(self.player.position.x, self.player.position.y)
     
    def CheckCollision(self, player, other):
        if AABB(player, other):
            if not player.isGrounded:
                self.player.position.x = self.lastPosition.x
                self.player.position.y = self.lastPosition.y
        else:
            self.lastPosition = Vector2(self.player.position.x, self.player.position.y)
        
        for b in bullets:    
            if RadialToBox(b, other):
                b.DoEvent(other)
                
                
    def CheckCollisionE(self, enemy, other):
        if AABB(enemy, other):
            if not enemy.isGrounded:
                self.player.position.x = self.lastPosition.x
                self.player.position.y = self.lastPosition.y
        else:
            self.lastPosition = Vector2(self.player.position.x, self.player.position.y)


        
        