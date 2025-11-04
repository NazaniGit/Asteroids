import math
import random
import pygame
from pygame.math import Vector2
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Randomize the angle of the split
        random_angle = random.uniform(20, 50)
        
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = a * 1.2

        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = b * 1.2

    def bounce(self, other):
        # Compute the normal vector between the two asteroids
        delta = self.position - other.position
        distance = delta.length()

        if distance == 0:
            # Avoid divide-by-zero errors
            return

        # Normalize the normal vector
        normal = delta / distance

        # Relative velocity
        relative_velocity = self.velocity - other.velocity

        # Project relative velocity onto the normal
        vel_along_normal = relative_velocity.dot(normal)

        # If they are moving apart, don't bounce
        if vel_along_normal > 0:
            return

        # Simple elastic collision (assuming equal mass)
        self.velocity -= vel_along_normal * normal
        other.velocity += vel_along_normal * normal

        # Optional: separate them slightly to prevent overlap
        overlap = self.radius + other.radius - distance
        if overlap > 0:
            correction = normal * (overlap / 2)
            self.position += correction
            other.position -= correction
