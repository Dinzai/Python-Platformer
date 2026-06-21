from Entity import *
enemies = []
class Enemy(Entity):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.SetSpeed(200)
        self.SetColour(200,100,100)
        self.hp = 2
        self.DetectionZoneArea = 200 * scaleFactor
        self.center_x = self.position.x + self.size.x * 0.5
        self.center_y = self.position.y + self.size.y * 0.5
        self.can_Chase_Player = False
        
    def DoEvent(self):
        self.hp -= 1
        if self.hp <= 0:
            self.markedForDeath = True
            
    def UpdateCenter(self):
        self.center_x = self.position.x + self.size.x * 0.5
        self.center_y = self.position.y + self.size.y * 0.5
            
    def StateMachine(self, player):
        
        if player.position.x >= self.center_x - self.DetectionZoneArea:
            self.can_Chase_Player = True
        
            
        if self.can_Chase_Player:
            if player.position.x > self.position.x:
                self.direction.x = 1
            if player.position.x < self.position.x:
                self.direction.x = -1
        
    
    def Update(self, player, deltaTime):
        self.Gravity(deltaTime)
        self.StateMachine(player)
        if self.markedForDeath:
            enemies.remove(self)
        self.position.x += self.direction.x * (self.speed * scaleFactor) * deltaTime
        self.UpdateCenter()
        
            
        
        
def Spawner():
    e = Enemy(Vector2(scaleFactor * 700, scaleFactor * 200),Vector2(100, 200))
    enemies.append(e)