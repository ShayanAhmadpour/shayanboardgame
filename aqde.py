import pygame
pygame.init()
WIDTH = 455
HEIGHT = 665
DEMENSION1 = 7
DEMENSION2 = 5
SQ_SIZE = WIDTH // DEMENSION2
DGREEN =(90, 143, 10)
LGREEN =(158, 245, 27)
WHITE=(255,255,255)
BLACK=(0,0,0)
FPS = 30
screen = pygame.display.set_mode((WIDTH+40, HEIGHT+202))
pygame.display.set_caption("Derby")
class GameState():
    def __init__(self):
        self.board = [
            ["b1"],
            ["b2","b3","b4","b5","b6"],
            ["b4","b5","b6","b2","b3"],
            ["__","__","__","__","__"],
            ["__","__","__","__","__"],
            ["__","__","__","__","__"],
            ["r2","r3","r4","r5","r6"],
            ["r4","r5","r6","r2","r3"],
            ["r1"]]
        self.redToMove = True
    def drawBoard(self, screen):
        screen.fill(DGREEN)
        for row in range(DEMENSION2 ):
            for coloumn in range(row % 2,DEMENSION1,2):
                pygame.draw.rect(screen,LGREEN,(20+row*SQ_SIZE, 101+coloumn*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        darvazeh=pygame.Rect(202,0,SQ_SIZE, SQ_SIZE)
        darvazeh2=pygame.Rect(202,748,SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(screen,WHITE,darvazeh)
        pygame.draw.rect(screen,WHITE,darvazeh2)
        khate_darvazeh=pygame.Rect(20,91,WIDTH,10)
        khate_darvazeh2=pygame.Rect(20,738,WIDTH,10)
        khate_darvazeh3=pygame.Rect(10,91,10,HEIGHT-8)
        khate_darvazeh4=pygame.Rect(20+WIDTH,91,10,HEIGHT-8)
        pygame.draw.rect(screen,WHITE,khate_darvazeh)
        pygame.draw.rect(screen,WHITE,khate_darvazeh2)
        pygame.draw.rect(screen,WHITE,khate_darvazeh3)
        pygame.draw.rect(screen,WHITE,khate_darvazeh4)

def main():
    run = True
    clock = pygame.time.Clock()
    gs = GameState()
    
    while run:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                pass
        gs.drawBoard(screen)

        pygame.display.update()
    pygame.quit()


def drawGameState(screen,gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)

        
def drawBoard(self, screen):
    screen.fill(DGREEN)
    for row in range(DEMENSION2 ):
        for coloumn in range(row % 2,DEMENSION1,2):
            pygame.draw.rect(screen,LGREEN,(20+row*SQ_SIZE, 101+coloumn*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    darvazeh=pygame.Rect(202,0,SQ_SIZE, SQ_SIZE)
    darvazeh2=pygame.Rect(202,748,SQ_SIZE, SQ_SIZE)
    pygame.draw.rect(screen,WHITE,darvazeh)
    pygame.draw.rect(screen,WHITE,darvazeh2)
    khate_darvazeh=pygame.Rect(20,91,WIDTH,10)
    khate_darvazeh2=pygame.Rect(20,738,WIDTH,10)
    khate_darvazeh3=pygame.Rect(10,91,10,HEIGHT-8)
    khate_darvazeh4=pygame.Rect(20+WIDTH,91,10,HEIGHT-8)
    pygame.draw.rect(screen,WHITE,khate_darvazeh)
    pygame.draw.rect(screen,WHITE,khate_darvazeh2)
    pygame.draw.rect(screen,WHITE,khate_darvazeh3)
    pygame.draw.rect(screen,WHITE,khate_darvazeh4)

def drawPieces(screen,board):
    for row in range(DEMENSION2):
        for coloumn in range(DEMENSION1):
            piece = board [row][coloumn]
            
        

        

main()
