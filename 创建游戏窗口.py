import pygame
def main():
    pygame.init()
    FPSLOCK = pygame.time.Clock()                    # 创建时钟对象
    WINSET = pygame.display.set_mode((640,480))      # 创建窗体
    # WINSET.fill((255,255,0))                         # 背景颜色填充
    imge = pygame.image.load(("D:/bg.jpg"))       # 导入图片文件
    WINSET.blit(imge,(0,0))                          # 绘制图形
    BAS = pygame.font.Font("STKAITI.TTF",20)
    msgsurf = BAS.render("初始化...",True,(3,54,73),(255,255,193))
    WINSET.blit(msgsurf,(0,0))
    autosurf = BAS.render("重启",True,(3,54,73),(255,255,193))
    autorect = autosurf.get_rect()
    autorect.x = (640 - autorect.width-20)
    autorect.y = (480 - autorect.height-20)
    WINSET.blit(autosurf,autorect)
    SYB = BAS.render("上一步",True,(3,54,73),(255,255,193))
    SYBrect = SYB.get_rect()
    SYBrect.x = (640 - SYBrect.width-20)
    SYBrect.y = (480 - SYBrect.height-140)
    WINSET.blit(SYB,SYBrect)
    gamemode = BAS.render("游戏模式",True,(3,54,73),(255,255,193))
    gamemoderect = gamemode.get_rect()
    gamemoderect.x = (640 - gamemoderect.width-20)
    gamemoderect.y = (480 - gamemoderect.height-80)
    WINSET.blit(gamemode,gamemoderect)

    pygame.display.set_caption("推盘游戏")             # 设置窗口标题
    pygame.display.update()                          # 刷新窗口
    i = 0
    while True:
        i += 1
        print(i)
        FPSLOCK.tick(60)
    pygame.quit()                                    # 退出模块
if __name__ == '__main__':
    main()
