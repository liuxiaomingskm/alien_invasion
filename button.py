import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性, msg是要在按钮中显示的文本"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 600, 50
        # 亮绿色
        self.button_color = (0, 255, 0)
        # 文本颜色为白色
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #创建按钮的rect对象， 并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像， 并使其在按钮上居中"""
        # 方法font.render()中的bool参数，该实参数指定开启翻锯齿功能
        # 从而让文本的边缘更平滑，余下两个参数分别是文本颜色和背景色，
        # 如果没有指定背景色， pygame将以透明背景的方式渲染文本
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮， 再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
