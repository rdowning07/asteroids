import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # Immediately kill this asteroid
        self.kill()
        
        # If too small to split, we're done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Log the split event
        log_event("asteroid_split")
        
        # Generate random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)
        
        # Create velocity vectors for the two new asteroids
        # Rotate the current velocity by the random angle
        new_velocity1 = self.velocity.copy().rotate(angle)
        # Rotate in the opposite direction for the second asteroid
        new_velocity2 = self.velocity.copy().rotate(-angle)
        
        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids at the current position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set velocities and scale them up by 1.2 to make them faster
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2.velocity = new_velocity2 * 1.2
