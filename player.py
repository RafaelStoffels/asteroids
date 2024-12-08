import pygame
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, direction, dt):
        if direction == "left":
            self.rotation -= PLAYER_TURN_SPEED * dt
        elif direction == "right":
            self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.dt = dt

        if keys[pygame.K_a]:
            Player.rotate(self, "left", dt)
    
        if keys[pygame.K_d]:
            Player.rotate(self, "right", dt)

        if keys[pygame.K_w]:
            Player.move(self, "forward", dt)

        if keys[pygame.K_s]:
            Player.move(self, "backward", dt)

        if keys[pygame.K_SPACE]:
            if self.shoot_timer > 0:
                self.shoot_timer -= dt

            if self.shoot_timer <= 0:
                Player.shoot(self)
                self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def move(self, direction, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)

        if direction == "forward":
            self.position -= forward * PLAYER_SPEED * dt
        elif direction == "backward":
            self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.x, self.y, SHOT_RADIUS)
        shot.position = pygame.Vector2(self.position)
        shot.velocity = pygame.Vector2(0, PLAYER_SHOOT_SPEED).rotate(self.rotation)

     