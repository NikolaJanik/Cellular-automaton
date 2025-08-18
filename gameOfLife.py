import numpy as np
import time
import pygame
import button

class Menu:
    def __init__(self, win_size, surface):
        self.surface = surface
        self.color = (0, 0, 0)
        self.menu_mode = True

        imgClearGrid = pygame.image.load("clearGrid.png").convert_alpha()
        imgBomber = pygame.image.load("bomber.png").convert_alpha()
        imgCopperhead = pygame.image.load("copperhead.png").convert_alpha()
        imgDart = pygame.image.load("dart.png").convert_alpha()
        imgDiamond = pygame.image.load("diamond.png").convert_alpha()
        imgGGG = pygame.image.load("gosperGlinderGun.png").convert_alpha()
        imgKickback = pygame.image.load("kickback.png").convert_alpha()
        imgLoafer = pygame.image.load("loafer.png").convert_alpha()
        imgPenta = pygame.image.load("pentadecathlon.png").convert_alpha()

        self.buttonClearGrid = button.Button(0, 0, imgClearGrid, 2)
        self.buttonBomber = button.Button(0, 50, imgBomber, 1)
        self.buttonCopperhead = button.Button(0, 0, imgCopperhead, 1)
        self.buttonDart = button.Button(0, 50, imgDart, 1)
        self.buttonDiamond = button.Button(0, 0, imgDiamond, 1)
        self.buttonGGG = button.Button(0, 50, imgGGG, 1)
        self.buttonKickback = button.Button(0, 0, imgKickback, 1)
        self.buttonLoafer = button.Button(0, 50, imgLoafer, 1)
        self.buttonPenta = button.Button(0, 0, imgPenta, 1)

    def events(self):
        self.surface.fill(self.color)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.buttonClearGrid.draw(self.surface):
            self.menu_mode = False
            self.surface.fill(self.color)
        elif self.buttonBomber.draw(self.surface):
            self.menu_mode = False
            self.surface.fill(self.color)
        pygame.display.update()


COLOR_BG = (10,10,10)
COLOR_GRID = (40,40,40)
COLOR_DIE_NEXT = (0,0,0)
COLOR_ALIVE_NEXT = (255,255,255)

def update(screen, cells, size, with_pregress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row,col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT
        
        if cells[row,col] == 1:
            if alive < 2 or alive >3:
                if with_pregress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_pregress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_pregress:
                    color = COLOR_ALIVE_NEXT
                
                
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))
        
    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 620))
    cells = np.zeros((60, 80))
    screen.fill(COLOR_GRID)
    generation = 0
    update(screen, cells, 10)
    
    text_font = pygame.font.SysFont("Arial", 20)
    
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    
    pygame.display.flip()
    pygame.draw.rect(screen, (255,255,255), (0, 600, 800, 20))
    draw_text(f"Generation: {generation}", text_font, (0,0,0), 0, 600)
    pygame.display.update()
    
    

    running = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.draw.rect(screen, (255,255,255), (0, 600, 800, 20))
                    draw_text(f"Generation: {generation}", text_font, (0,0,0), 0, 600)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] //10] = 1
                update(screen, cells, 10)
                pygame.draw.rect(screen, (255,255,255), (0, 600, 800, 20))
                draw_text(f"Generation: {generation}", text_font, (0,0,0), 0, 600)
                pygame.display.update()
                
        screen.fill(COLOR_GRID)
        
        if running:
            generation +=1
            cells = update(screen, cells, 10, with_pregress=True)
            pygame.draw.rect(screen, (255,255,255), (0, 600, 800, 20))
            draw_text(f"Generation: {generation}", text_font, (0,0,0), 0, 600)
            pygame.display.update()
            
            print(f"Generation {generation}")
            
            
        time.sleep(0.2)
    
if __name__ == '__main__':
    main()
