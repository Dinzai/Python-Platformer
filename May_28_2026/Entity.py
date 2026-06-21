import pygame
from Game_math import *
#used for ground for now
class Entity:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.direction = Vector2(0, 0)
        self.speed = 0
        self.colour = (0, 200, 0)
        self.markedForDeath = False
        self.isGrounded = False
        self.gravity = 0
        self.increaseAmount = 20
        self.hp = 0
        
    def Gravity(self, deltaTime):
        if not self.isGrounded:
            self.gravity += self.increaseAmount * deltaTime
            if self.gravity >= 200:
                self.gravity = 200   
            self.position.y += self.speed * scaleFactor * self.gravity * deltaTime
        if self.isGrounded:
            self.gravity = 0
         
    def SetColour(self, r,g,b):
        self.colour = (r,g,b)
        
    def SetSpeed(self, velocity):
        self.speed = velocity
        
    def DoEvent(self):
        return
        
    def Draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.position.x, self.position.y, self.size.x, self.size.y))
        

