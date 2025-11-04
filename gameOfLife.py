import numpy as np
import time
import pygame
import button

class Menu:
    def __init__(self, win_size, surface):
        self.surface = surface
        self.color = (0, 0, 0)
        self.menu_mode = True

        imgClearGrid = pygame.image.load("images/clearGrid.png").convert_alpha()
        imgBomber = pygame.image.load("images/bomber.png").convert_alpha()
        imgCopperhead = pygame.image.load("images/copperhead.png").convert_alpha()
        imgDart = pygame.image.load("images/dart.png").convert_alpha()
        imgDiamond = pygame.image.load("images/diamond.png").convert_alpha()
        imgGun = pygame.image.load("images/gun.png").convert_alpha()
        imgLoafer = pygame.image.load("images/loafer.png").convert_alpha()
        imgPenta = pygame.image.load("images/pentadecathlon.png").convert_alpha()

        self.buttonBomber = button.Button(360, 0, imgBomber, 1)
        self.buttonCopperhead = button.Button(0, 150, imgCopperhead, 1)
        self.buttonDart = button.Button(360, 150, imgDart, 1)
        self.buttonDiamond = button.Button(360, 300, imgDiamond, 1)
        self.buttonGun = button.Button(0, 300, imgGun, 1)
        self.buttonLoafer = button.Button(360, 450, imgLoafer, 1)
        self.buttonPenta = button.Button(0, 450, imgPenta, 1)

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
        elif self.buttonCopperhead.draw(self.surface):
            self.menu_mode = False
            self.surface.fill(self.color)
        elif self.buttonDart.draw(self.surface):
            self.menu_mode = False
            self.surface.fill(self.color)
        elif self.buttonDiamond.draw(self.surface):
            self.menu_mode = False
            self.surface.fill(self.color)
        elif self.buttonGun.draw(self.surface):
            self.menu_mode = False
            self.surface.fill(self.color)
        elif self.buttonLoafer.draw(self.surface):
            self.menu_mode = False
            self.surface.fill(self.color)
        elif self.buttonPenta.draw(self.surface):
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
    menu = Menu((800, 620), screen)
    text_font = pygame.font.SysFont("Arial", 20)
    
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    running = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if menu.menu_mode:
                menu.events()

            else:
                screen.fill(COLOR_GRID)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = not running

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        cells[pos[1] // 10, pos[0] // 10] = 1

        if not menu.menu_mode:
            if running:
                generation += 1
                cells = update(screen, cells, 10, with_pregress=True)
                print(f"Generation {generation}")
            else:
                update(screen, cells, 10)
                #Drawing map only first time. After stops it won't appear
                if(not generation):
                    pygame.draw.rect(screen, (255, 255, 255), (60,80,9,9))

            pygame.draw.rect(screen, (255, 255, 255), (0, 600, 800, 20))
            draw_text(f"Generation: {generation}",
                      text_font, (0, 0, 0), 0, 600)

        pygame.display.update()
        time.sleep(0.1)
    
if __name__ == '__main__':
    main()
