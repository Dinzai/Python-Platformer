import pygame
from Entity import *
from Projectile import *


class Player(Entity):
    def __init__(self, position, size):
        super().__init__(position, size)
        
        self.lastPosition = Vector2(0, 0)
        self.previousMouseState = False
        self.currentMouseState = False
        self.hasJumped = False
        self.canJump = True
        self.SetColour(80,100,200)
        self.SetSpeed(100)
        self.jumpSpeed = 2500
        self.jumpTimer = 0
        self.increaseAmount = 20
        self.airTime = 100
        self.hp = 3
        
        
    def MouseEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.currentMouseState = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.currentMouseState = False
        
    def FixedUpdate(self):       
        keys = pygame.key.get_pressed()
        self.direction = Vector2(0, 0)
        if keys[pygame.K_SPACE]:
            self.direction.y = -1
            if self.canJump:
                self.hasJumped = True
                self.canJump = False
            self.direction = Normalize(self.direction)     
        if keys[pygame.K_s]:
            self.direction.y = 1
            self.direction = Normalize(self.direction)     
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.direction = Normalize(self.direction)     
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.direction = Normalize(self.direction)     
        if self.currentMouseState and not self.previousMouseState:
            Shoot(GetAngle(Vector2(pygame.mouse.get_pos()[0] * scaleFactor, pygame.mouse.get_pos()[1] * scaleFactor), self.position), Vector2(self.position.x + self.size.x * 0.5, self.position.y + self.size.y * 0.5))
        self.previousMouseState = self.currentMouseState

    def Jump(self, deltaTime):
        self.jumpTimer += self.increaseAmount * deltaTime
        if self.jumpTimer <= self.airTime:
            self.position.y += self.jumpSpeed * self.direction.y * scaleFactor * deltaTime + self.jumpTimer
        self.hasJumped = False

    def Update(self, deltaTime):
        self.Gravity(deltaTime)
        if self.isGrounded:
            self.canJump = True
            
        if(self.position.x < 0 or self.position.x > (window_width * scaleFactor) - self.size.x):
            self.position.x = self.lastPosition.x
             
        if(self.position.y < 0 or self.position.y > (window_height * scaleFactor) - self.size.y):
            self.position.y = self.lastPosition.y
        
        self.lastPosition = Vector2(self.position.x, self.position.y)  
        self.position.x += self.direction.x * (self.speed * scaleFactor) * deltaTime 
        if self.hasJumped:
            self.Jump(deltaTime)
            
           
        
        

    