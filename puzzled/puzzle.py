import sys, pygame, random, time
from pygame.locals import *



#remember to init()
#window set up
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
fps = 30
#BOX set up
BOXSIZE = 50
GAPSIZE = 10
BOARDWIDTH = 7
BOARDHEIGHT = 2

XMARGIN = int((WINDOWWIDTH - ((BOXSIZE + GAPSIZE) * BOARDWIDTH))/2)
YMARGIN = int((WINDOWHEIGHT - ((BOXSIZE + GAPSIZE) * BOARDHEIGHT))/2)
#LOAD ANH
img1 = pygame.transform.scale(pygame.image.load('1.png'), (BOXSIZE, BOXSIZE))
img2 = pygame.transform.scale(pygame.image.load('2.png'), (BOXSIZE, BOXSIZE))
img3 = pygame.transform.scale(pygame.image.load('3.png'), (BOXSIZE, BOXSIZE))
img4 = pygame.transform.scale(pygame.image.load('4.png'), (BOXSIZE, BOXSIZE))
img5 = pygame.transform.scale(pygame.image.load('5.png'), (BOXSIZE, BOXSIZE))
img6 = pygame.transform.scale(pygame.image.load('6.png'), (BOXSIZE, BOXSIZE))
img7 = pygame.transform.scale(pygame.image.load('7.png'), (BOXSIZE, BOXSIZE))
img8 = pygame.transform.scale(pygame.image.load('8.png'), (BOXSIZE, BOXSIZE))
img9 = pygame.transform.scale(pygame.image.load('9.png'), (BOXSIZE, BOXSIZE))
img10 = pygame.transform.scale(pygame.image.load('10.png'), (BOXSIZE, BOXSIZE))
img11 = pygame.transform.scale(pygame.image.load('11.png'), (BOXSIZE, BOXSIZE))
img12 = pygame.transform.scale(pygame.image.load('12.png'), (BOXSIZE, BOXSIZE))
img13 = pygame.transform.scale(pygame.image.load('13.png'), (BOXSIZE, BOXSIZE))
img14 = pygame.transform.scale(pygame.image.load('14.png'), (BOXSIZE, BOXSIZE))

assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, "Tro choi can so chan cac o"





#color 
RED      = (255,   0,   0)
BLUE     = (  0,   0, 255)
GREEN    = (  0, 255,   0)
CYAN     = (  0, 255, 255)
YELLOW   = (255, 255,   0)
MAGNENTA = (255,   0, 255)
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)



def main():
    pygame.init()
    global gameSurface, fpsclock, boxx, boxy
    mousex = 0
    mousey = 0
    fpsclock = pygame.time.Clock()
    #game surface and caption
    gameSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("puzzle time")
    #boxes begin
    revealedBoxes = generateRevealedBoxesData(False)
    board = getRandomBoxes()
    
    firstSelection = None
    
                
    while True:
        mouseClick = False
        getRandomBoxes()
        gameSurface.fill(CYAN)
        #gameSurface.blit(img2, (50, 400))
        draw(board, revealedBoxes)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClick = True
            
        boxx, boxy = getBoxAtPixel(mousex, mousey)
        
        if boxx != None and boxy != None:
            if not revealedBoxes[boxx][boxy] and mouseClick == True:
                if firstSelection == None:
                    firstSelection = (boxx, boxy)
                    drawReveal(revealedBoxes, board, boxx, boxy)
                else:
                    if board[firstSelection[0]][firstSelection[1]] != board[boxx][boxy]:
                        drawReveal(revealedBoxes, board, boxx, boxy)
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                        pygame.display.update()
                        pygame.time.wait(1000)
                    else:
                        if winGame(revealedBoxes) == False:
                            revealedBoxes[firstSelection[0]][firstSelection[1]] = True
                            revealedBoxes[boxx][boxy] = True
                        else:
                            revealedBoxes[firstSelection[0]][firstSelection[1]] = True
                            revealedBoxes[boxx][boxy] = True
                            drawReveal(revealedBoxes, board, boxx, boxy)
                            fontObj = pygame.font.SysFont('Sans', 40)
                            textSurfaceObj = fontObj.render('YOU WIN!!!', True, GREEN, BLUE)
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 4))
                            gameSurface.blit(textSurfaceObj, textRectObj)
                            pygame.display.update()
                            pygame.time.wait(5000)
                            #renew game
                            revealedBoxes = generateRevealedBoxesData(False)
                            board = getRandomBoxes()
                        
                        
                    firstSelection = None
                    
                    
        pygame.display.update()
        fpsclock.tick(fps)
            
def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes
   
def getRandomBoxes():
    boxes = []
    boxes.append(img1)
    boxes.append(img2)
    boxes.append(img3)
    boxes.append(img4)
    boxes.append(img5)
    boxes.append(img6)
    boxes.append(img7)
    boxes.append(img8)
    boxes.append(img9)
    boxes.append(img10)
    boxes.append(img11)
    boxes.append(img12)
    boxes.append(img13)
    boxes.append(img14)
    random.shuffle(boxes)
    iconNum = int((BOARDWIDTH * BOARDHEIGHT) / 2)
    gameBoxes = []
    for i in range(0, iconNum):
        gameBoxes.append(boxes[i])
        gameBoxes.append(boxes[i])
    random.shuffle(gameBoxes)
    
    #add to board
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(gameBoxes[0])
            del gameBoxes[0]
        board.append(column)
    return board

def leftCoord(boxx):
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    return left
def topCoord(boxy):
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return top
def draw(board, revealedBoxes):
    for i in range(0, BOARDWIDTH):
        for j in range(0, BOARDHEIGHT):
            gameSurface.blit(board[i][j], pygame.Rect(leftCoord(i), topCoord(j), BOXSIZE, BOXSIZE))
            if revealedBoxes[i][j] == False:
                drawUnReveal(revealedBoxes, i, j)
def getBoxAtPixel(x, y):
    for i in range(BOARDWIDTH):
        for j in range(BOARDHEIGHT):
            left = leftCoord(i)
            top = topCoord(j)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y) == True:
                return (i, j)
    return (None, None)

def boxCompare(board, a, b, x, y):
    if board[a][b] == board[x][y]:
        return True
    return False

def drawUnReveal(revealedBoxes, x, y):
    if revealedBoxes[x][y] == False:
        pygame.draw.rect(gameSurface, WHITE, (leftCoord(x), topCoord(y), BOXSIZE, BOXSIZE))

def drawReveal(revealedBoxes, board, x, y):
    gameSurface.blit(board[x][y], pygame.Rect(leftCoord(x), topCoord(y), BOXSIZE, BOXSIZE))
    revealedBoxes[x][y] = True
    
def winGame(revealedBoxes):
    dem = 0
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if revealedBoxes[x][y] == True:
                dem += 1
    iconNum = BOARDHEIGHT * BOARDWIDTH - 1
    if iconNum == dem:
        return True
    return False
                
main()
        