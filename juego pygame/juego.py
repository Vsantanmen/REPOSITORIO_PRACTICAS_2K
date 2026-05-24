import pygame
import sys
import math
from pygame.locals import QUIT

resolution = (640, 480)
white = (252, 243, 207)
black = (0, 0, 0)
red = (255, 0, 0)

class Ball:
    def __init__(self, xPos = resolution[0] / 2, yPos = resolution[1] / 2, xVel = 4, yVel = -4, rad = 15):
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.type = "ball"
        self.clock = pygame.time.Clock()
        self.time_accumulator = 0

    def draw(self, surface):
        pygame.draw.circle(surface, black, (int(self.x), int(self.y)), self.radius)

    def update(self, gameObjects):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius <= 0:
            self.x = self.radius
            self.dx *= -1
        elif self.x + self.radius >= resolution[0]:
            self.x = resolution[0] - self.radius
            self.dx *= -1

        if self.y - self.radius <= 0:
            self.y = self.radius
            self.dy *= -1
        elif self.y + self.radius >= resolution[1]:
            self.y = resolution[1] - self.radius
            self.dy *= -1

        dt = self.clock.tick()
        self.time_accumulator += dt

        if self.time_accumulator > 7500:
            self.time_accumulator = 0
            decay = 0.95
            if abs(self.dx) > 0.5:
                self.dx *= decay
            if abs(self.dy) > 0.5:
                self.dy *= decay

class Player:
    def __init__(self, rad = 20):
        self.x = resolution[0] / 2
        self.y = resolution[1] - 60
        self.dx = 0
        self.dy = 0
        self.radius = rad
        self.type = "player"
        self.speed = 5

    def draw(self, surface):
        pygame.draw.circle(surface, red, (int(self.x), int(self.y)), self.radius)

    def update(self, gameObjects):
        keys = pygame.key.get_pressed()
        self.dx = 0
        self.dy = 0

        if keys[pygame.K_LEFT]:
            self.dx = -self.speed
        if keys[pygame.K_RIGHT]:
            self.dx = self.speed
        if keys[pygame.K_UP]:
            self.dy = -self.speed
        if keys[pygame.K_DOWN]:
            self.dy = self.speed

        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius < 0:
            self.x = self.radius
        elif self.x + self.radius > resolution[0]:
            self.x = resolution[0] - self.radius

        if self.y - self.radius < 0:
            self.y = self.radius
        elif self.y + self.radius > resolution[1]:
            self.y = resolution[1] - self.radius

        for gameObj in gameObjects:
            if gameObj.type == "ball":
                ball = gameObj
                distance_x = ball.x - self.x
                distance_y = ball.y - self.y
                distance = math.sqrt(distance_x**2 + distance_y**2)
                min_distance = ball.radius + self.radius

                if distance <= min_distance:
                    if distance == 0:
                        nx, ny = 1, 0
                    else:
                        nx = distance_x / distance
                        ny = distance_y / distance

                    overlap = min_distance - distance
                    ball.x += nx * overlap

                    if keys[pygame.K_SPACE]:
                        ball.dx = self.dx if self.dx != 0 else nx * 5
                        ball.dy = self.dy if self.dy != 0 else ny * 5
                    else:
                        kx = ball.dx - self.dx
                        ky = ball.dy - self.dy
                        p = 2 * (kx * nx + ky * ny)
                        ball.dx = ball.dx - p * nx
                        ball.dy = ball.dy - p * ny

class game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption("Haxball POO Avanzado")
        self.clock = pygame.time.Clock()
        self.gameObjects = [Ball(), Player()]

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.handleEvents()

            for gameObj in self.gameObjects:
                gameObj.update(self.gameObjects)

            self.screen.fill(white)

            for gameObj in self.gameObjects:
                gameObj.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

game().run()