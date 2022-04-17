import pygame
from colors import colors


class DrawMap:
    def __init__(self, screen):
        self.MAP = [
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            [
                1,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            [
                1,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            [
                1,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            [
                1,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
        ]

        self.bricks = []
        self.lines = []
        self.brick_width = 128
        self.brick_height = 96
        self.screen = screen

    def initialiseMap(self):

        for y in range(0, len(self.MAP)):
            for x in range(len(self.MAP[y])):

                if self.MAP[y][x] == 1:
                    color = colors.GREEN()
                    x_pos = x * self.brick_width
                    y_pos = y * self.brick_height
                    self.bricks.append(
                        (
                            pygame.Rect(
                                x_pos, y_pos, self.brick_width, self.brick_height
                            ),
                            color,
                        )
                    )
                    self.lines.append(
                        (
                            pygame.Rect(x_pos, y_pos, 5, self.brick_height),
                            colors.BLACK(),
                        )
                    )
                    self.lines.append(
                        (pygame.Rect(x_pos, y_pos, self.brick_width, 5), colors.BLACK())
                    )

                if self.MAP[y][x] == 2:
                    color = colors.RED()
                    x_pos = x * self.brick_width
                    y_pos = y * self.brick_height
                    self.bricks.append(
                        (
                            pygame.Rect(
                                x_pos, y_pos, self.brick_width, self.brick_height
                            ),
                            color,
                        )
                    )
                    self.lines.append(
                        (
                            pygame.Rect(x_pos, y_pos, 5, self.brick_height),
                            colors.BLACK(),
                        )
                    )
                    self.lines.append(
                        (pygame.Rect(x_pos, y_pos, self.brick_width, 5), colors.BLACK())
                    )
                    self.lines.append(
                        (
                            pygame.Rect(
                                x_pos + self.brick_width,
                                y_pos,
                                5,
                                self.brick_height + 5,
                            ),
                            colors.BLACK(),
                        )
                    )
                    self.lines.append(
                        (
                            pygame.Rect(
                                x_pos, y_pos + self.brick_height, self.brick_width, 5
                            ),
                            colors.BLACK(),
                        )
                    )

    def returnWalls(self) -> list:
        return self.lines

    def drawBricks(self):
        for objs in self.bricks:
            pygame.draw.rect(self.screen, objs[1], objs[0])

    def drawGrid(self):
        for line in self.lines:
            pygame.draw.rect(self.screen, line[1], line[0])

    def draw(self):
        self.initialiseMap()
        self.drawBricks()
        self.drawGrid()
