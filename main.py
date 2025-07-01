import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 800, 800
FPS = 6
BACKGROUND = "#133408"
GRID = "#565656"
BLOCK_SIZE = 40

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

pause = False
win = False 
defeat = False 
run = True

while run: 
    clock.tick(FPS)
    
    #? События
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT: # Выход из игры
                run = False
            case pygame.KEYDOWN: # Нажата клавиша клавиатуры
                match event.key:
                    case pygame.K_RETURN: # Клавиша - это ENTER
                        pause = False if pause else True # Пауза - это ложь если пауза - истина, иначе все же истина (Перевод)
                        
    #? Отрисовка
    
    
    #? Обновление объектов
    
    
pygame.display.quit()   
pygame.quit()
