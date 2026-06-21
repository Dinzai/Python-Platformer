import pygame
from Game_math import *
from Entity import *

bullets = []

class Bullet(Entity):
    
    def __init__(self):
        super().__init__(0, 0)
        self.position = Vector2(0, 0)
        self.diameter = 20
        self.radius = self.diameter * 0.5
        self.angle = 0
        self.SetSpeed(200)
            
    def Manager(self):
        if self.position.x >= window_width * scaleFactor:
            self.markedForDeath = True
        if self.position.x <= 0:
            self.markedForDeath = True
        if self.position.y >= window_height * scaleFactor:
            self.markedForDeath = True
        if self.position.y <= 0:
            self.markedForDeath = True
            
        if self.markedForDeath:
            bullets.remove(self)
        
    def Update(self, deltaTime):
        self.Manager()
        
        self.position.x += cos(self.angle) * (self.speed * scaleFactor) * deltaTime
        self.position.y += sin(self.angle) * (self.speed * scaleFactor) * deltaTime
        
    def DoEvent(self, other):
        other.DoEvent()
        self.markedForDeath = True
        
    def Draw(self, screen):
        pygame.draw.circle(screen, (100, 100, 200), (self.position.x, self.position.y), self.diameter)
        
def Shoot(angle, position):
    b = Bullet()
    b.angle = angle
    b.position = Vector2(position.x, position.y)
    bullets.append(b)