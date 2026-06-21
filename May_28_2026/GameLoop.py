import pygame
from Player import *
from Entity import *
from CollisionManager import *
from Enemy import *

class Game:
# Initialize all pygame modules
    def Run(self):
        self.GameLoop()
        
    def Init(self):
        pygame.init()
        self.player = Player(Vector2(200, 700), Vector2(100, 100))
        self.screen = pygame.display.set_mode([window_width, window_height])
        self.win = pygame.Surface((window_width * scaleFactor, window_height * scaleFactor))
        self.scaled_win = pygame.transform.smoothscale(self.win, self.screen.get_size())
        Spawner()
        self.ground = Entity(Vector2(0, window_height * scaleFactor - 100 * scaleFactor), Vector2(1000 * scaleFactor, 50 * scaleFactor))
        self.deltaTime = 0
        self.collision = CollisionManager(self.player)
        

    def GameLoop(self):
        self.Init()
        self.Update()
        pygame.quit()
        
    def Update(self):
        self.deltaTime = pygame.time.Clock().tick(60) / 1000
       # Run until the user asks to quit
        running = True
        while running:           
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            for event in pygame.event.get():
                self.player.MouseEvent(event)
                if event.type == pygame.QUIT:
                    running = False            
            self.player.FixedUpdate()
            self.collision.CheckCollision(self.player, self.ground)
            
            self.player.Update(self.deltaTime) 
            for e in enemies:
                self.collision.CheckCollision(self.player, e)
                self.collision.CheckCollisionE(e, self.ground)
                e.Update(self.player, self.deltaTime) 
            for b in bullets:
                b.Update(self.deltaTime)      
            self.Draw()             
    
    def Draw(self):
        
        self.win.fill((255, 255, 255))
        self.player.Draw(self.win)
        self.ground.Draw(self.win)
        for e in enemies:
            e.Draw(self.win)
        for b in bullets:
            b.Draw(self.win)
            
        self.scaled_win = pygame.transform.smoothscale(self.win, self.screen.get_size())
        self.screen.blit(self.scaled_win, (0, 0))

        pygame.display.flip()
        