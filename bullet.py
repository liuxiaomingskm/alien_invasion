import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """该类对飞船的子弹进行管理"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()  # 首先找到Bullet的父类，然后把Bullet的对象self转换成父类对象，最后调用
        # 该父类对象的__init__方法，也可以写成super().__init__()
        self.screen = screen

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        # 子弹的中心位置和飞船的中心位置一致
        self.rect.centerx = ship.rect.centerx
        # 子弹的高度和飞船的高度一致，给人感觉是从飞船顶部射出
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)