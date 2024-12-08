import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def check_asteroid_destruction(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= self.radius + other.radius:
            return True
        else:
            return False

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            self.kill()
            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            split_angle = random.uniform(20, 50)
            velocity_1 = self.velocity.rotate(split_angle) * 1.2
            velocity_2 = self.velocity.rotate(-split_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
            child_ast_1.velocity = velocity_1
            child_ast_2.velocity = velocity_2