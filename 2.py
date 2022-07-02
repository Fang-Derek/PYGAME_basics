import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800,600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Image!")

#載入圖片物件與設定位置
bird_topleft = pygame.image.load("angrybird.png")  #載入圖案
bird_topleft_rect = bird_topleft.get_rect()  #取得圖案的大小放在變數中
bird_topleft_rect.topleft = (0,0)  #設定圖案出現的位置

bird_topright = pygame.image.load("angrybird.png")  #載入圖案
bird_topright_rect = bird_topright.get_rect()  #取得圖案的大小放在變數中
bird_topright_rect.topright = (WINDOW_WIDTH,0)  #設定圖片出現的位置

bird_bottomright = pygame.image.load("blood-drop.png")  #載入圖案
bird_bottomright_rect = bird_bottomright.get_rect()  #取得圖案的大小放在變數中
bird_bottomright_rect.bottomright = (WINDOW_WIDTH,WINDOW_HEIGHT)  #設定圖片出現的位置

bird_bottomleft = pygame.image.load("forward.png")  #載入圖案
bird_bottomleft_rect = bird_bottomleft.get_rect()  #取得圖案的大小放在變數中
bird_bottomleft_rect.bottomleft = (0,WINDOW_HEIGHT)  #設定圖片出現的位置

WHITE = (255,255,255)
GREEN = (0,255,0)
DARKGREEN = (10,50,10)

#fonts = pygame.font.get_fonts()  //取得所有pygame內建字型
system_font = pygame.font.SysFont("Century", 64)
custom_font = pygame.font.Font("AbstractGroovy.ttf", 50)

#Define Text:
show_text_1 = system_font.render("Angry Bird Game:", True, GREEN, DARKGREEN)
show_text_1_rect = show_text_1.get_rect()  #產生字體的方框
show_text_1_rect.center = (WINDOW_WIDTH//2, 30)

show_text_2 = custom_font.render("Move angry bird soon!", True, GREEN)
show_text_2_rect = show_text_2.get_rect()
show_text_2_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)

#音效
sound_1 = pygame.mixer.Sound("sound_1.wav")
sound_2 = pygame.mixer.Sound("sound_2.wav")

sound_1.play()
pygame.time.delay(2000)  #2000毫秒=2秒
sound_2.play()
pygame.time.delay(2000)

sound_2.set_volume(0.1)  #設音量0.1~1.0
sound_2.play()

#背景音樂
pygame.mixer.music.load("music.wav")  
pygame.mixer.music.play(-1, 0.0)  #-1重複播放，從頭播放
pygame.time.delay(10000)
pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        
    pygame.draw.line(displayscreen, WHITE, (0, 75), (WINDOW_WIDTH, 75), 5)
        
    displayscreen.blit(bird_topleft, bird_topleft_rect)  
    displayscreen.blit(bird_topright, bird_topright_rect)  
    displayscreen.blit(bird_bottomleft, bird_bottomleft_rect)  
    displayscreen.blit(bird_bottomright, bird_bottomright_rect)
    displayscreen.blit(show_text_1, show_text_1_rect)
    displayscreen.blit(show_text_2, show_text_2_rect)

    pygame.display.update()
    
pygame.quit()