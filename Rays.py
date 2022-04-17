import math, pygame
from colors import colors


class Ray:
    def __init__(self, width, height, screen) -> None:
        self.width = width
        self.height = height
        self.screen = screen
        self.pdx = 0
        self.pdy = 0
        self.player_angle = 0
        self.player_x = self.width / 2
        self.player_y = self.height / 2
        self.position_vector = pygame.math.Vector2(self.player_x, self.player_y)

    def degToRad(self, player_angle):
        return self.player_angle * math.pi / 180

    def fixAngle(self, player_angle):
        if self.player_angle > 359:
            self.player_angle -= 360
        if self.player_angle < 0:
            self.player_angle += 360
        return self.player_angle

    def drawRays(self, walls):
        self.position_vector = pygame.math.Vector2(self.player_x, self.player_y)
        self.x1 = self.position_vector[0]
        self.y1 = self.position_vector[1]
        self.x2 = self.player_x + self.pdx * 20
        self.y2 = self.player_y + self.pdy * 20
        self.line = pygame.draw.line(
            self.screen, colors.WHITE(), (self.x1, self.y1), (self.x2, self.y2), 5
        )
        for wall in walls:
            if self.line.colliderect(wall[0]):
                self.wallx = wall[0].top
                self.wally = wall[0].bottom
                print(self.wallx, self.wally)
                print()
                print(self.x2, self.y2)
                self.x3 = self.wallx[0]
                self.y3 = self.wallx[1]
                self.x4 = self.wally[0]
                self.y4 = self.wally[1]

                print(self.x3, self.y3, self.x4, self.y4)
                den = (self.x1 - self.x2) * (self.y3 - self.y4) - (
                    self.y1 - self.y2
                ) * (self.x3 - self.x4)
                if den == 0:
                    print("there is a issue")
                t = (self.x1 - self.x3) * (self.y3 - self.y4) - (self.y1 - self.y3) * (
                    self.x3 - self.x4
                ) / den
                u = (
                    -(self.x1 - self.x3) * (self.y1 - self.y2)
                    - (self.y1 - self.y3) * (self.x1 - self.x2) / den
                )
                if (t > 0 and t < 1) and (u > 0):
                    print("correct")
                else:
                    print(t)
                    print(u)
        return self.line
