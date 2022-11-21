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


    blockrect1 = pygame.Rect(300, 100, 50, 50)  # 创建矩形
    pygame.draw.rect(WINSET, (50, 255, 173), blockrect1)    # 绘制矩形
    numsurf = BAS.render("1", True, (3, 54, 73), (50, 255, 173))    # 绘制数字
    numrect = numsurf.get_rect()
    numrect.x = blockrect1.x + 0.5*(50 - numrect.width)
    numrect.y = blockrect1.y + 0.5*(50 - numrect.height)
    basesurf1 = WINSET.copy()
    WINSET.blit(numsurf, blockrect1)  # 渲染数字矩形框



    pygame.display.set_caption("推盘游戏")             # 设置窗口标题
    pygame.display.update()                          # 刷新窗口
    i = 0
    while True:
        i += 1
        pygame.draw.rect(WINSET,(50,255,173),blockrect1)
        WINSET.blit(numsurf,blockrect1)
        pygame.display.update()
        WINSET.blit(basesurf1,(0,0))
        blockrect1.y += 1
        numrect.y += 1
        FPSLOCK.tick(20)



    pygame.quit()                                    # 退出模块
if __name__ == '__main__':
    main()
