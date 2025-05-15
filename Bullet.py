import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, bullet_group, player):
        super().__init__()

        self.VELOCITY = 20
        self.RANGE = 500

        if player.velocity.x > 0:
            self.image = pygame.transform.scale(pygame.image.load("./assets/images/player/slash.png"), (32, 32))

        else:
            self.image = pygame.transform.scale(
                pygame.transform.flip(pygame.image.load("./assets/images/player/slash.png"), True, False), (32, 32))
            self.VELOCITY = -1 * self.VELOCITY

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.starting_x = x

        bullet_group.add(self)

    def update(self):
        self.rect.x += self.VELOCITY

        if abs(self.rect.x - self.starting_x) > self.RANGE:
            self.kill()
