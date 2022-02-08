import sys, pygame
import numpy as np

pygame.init()

widht = 800
height = 600
size = 800, 600
Rojo = 255, 0, 0
White = 255, 255, 255
Black = 0, 0, 0
Verde = 0, 255, 0
Dorado = 216, 195, 12
Color_de_fondo = 28, 170, 156
widht_linea = 15
LINE_COLOR = 56, 114, 108
filas = 3
columnas = 3
RADIO = 60
ANCHO_C = 15
ANCHO_CRUZ = 25
ESPACIOS = 55

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe :)")

menufont = pygame.font.SysFont("ROG Fonts",60)
menufont2 = pygame.font.SysFont("Comic Sans MS", 30)
menufont3 = pygame.font.SysFont("Comic Sans MS", 20)
pygame.mixer.music.load("music/sound1.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

sonidocirculo = pygame.mixer.Sound("music/circulo.wav")
sonidocruz = pygame.mixer.Sound("music/cruz.wav")
#tablero
tablero = np.zeros((filas, columnas))
jugador = 1
game_over = True

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
            print("a")


def creditos():
    pygame.display.set_caption("Créditos")
    fondo_menu = pygame.image.load("images/background.jpg")
    screen.blit(fondo_menu, (0, 0))




def marcar_casilla(fila, columna, jugador):
    tablero[fila][columna] = jugador

def casillas_sin_marcar(fila, columna):
    if tablero[fila][columna] == 0:
        return True
    else:
        return False

def tablero_lleno():
    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] == 0:
                return False
    return True

def ganador(jugador):
    for columna in range(columnas):
        if tablero[0][columna] == jugador and tablero[1][columna] == jugador and tablero[2][columna] == jugador:
            lineas2(columna, jugador)
            return True

    for fila in range(filas):
        if tablero[fila][0] == jugador and tablero[fila][1] == jugador and tablero[fila][2] == jugador:
            lineas3(fila, jugador)
            return True

    if tablero[2][0] == jugador and tablero[1][1] == jugador and tablero[0][2] == jugador:
        lineas4(jugador)
        return True

    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        lineas5(jugador)
        return True

def lineas2(columna, jugador):
    posicionX = columna * 200 + 100

    if jugador == 1:
        color = Rojo
    elif jugador == 2:
        color = Rojo

    pygame.draw.line( screen, color, (posicionX, 15), (posicionX, height-15), 15)

def lineas3(fila, jugador):

    posicionY = fila*200+100

    if jugador == 1:
        color = Rojo
    elif jugador ==2:
        color = Rojo
    pygame.draw.line(screen, color, (15, posicionY), (widht-215, posicionY), 15 )
def lineas4(jugador):

    if jugador == 1:
        color = Rojo
    elif jugador == 2:
        color = Rojo

    pygame.draw.line(screen, color, (15, height-15), (585,15), 15)

def lineas5(jugador):

    if jugador == 1:
        color = Rojo
    elif jugador == 2:
        color = Rojo

    pygame.draw.line(screen, color, (15,15), (585,585), 15)

def reseteo():
    screen.fill(Color_de_fondo)
    lineas()
    for fila in range(filas):
        for columna in range(columnas):
            tablero[fila][columna] = 0


def lineas():
    #1 horizontal
    pygame.draw.line(screen, Black, (0, 0), (600, 0), widht_linea)
    #2 horizontal
    pygame.draw.line(screen, Black, (0, 200), (600,200), widht_linea)
    #3 horiontal
    pygame.draw.line(screen, Black, (0, 400), (600,400), widht_linea)
    #4 horizontal
    pygame.draw.line(screen, Black, (0, 600), (600, 600), widht_linea)
    #1 vertical
    pygame.draw.line(screen, Black, (0, 0), (0, 600), widht_linea)
    #2 vertical
    pygame.draw.line(screen, Black, (200, 0), (200,600), widht_linea)
    #3 vertical
    pygame.draw.line(screen, Black, (400, 0), (400,600), widht_linea)
    #4 vertical
    pygame.draw.line(screen, Black, (600, 0), (600,600), widht_linea)

def figuras():
    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] == 1:
                pygame.draw.circle( screen, Rojo, (int(columna*200+100),int(fila*200+100)), RADIO, ANCHO_C)

            elif tablero[fila][columna] == 2:
                pygame.draw.line( screen, Rojo, (columna*200+ESPACIOS, fila*200+200-ESPACIOS), (columna*200+200-ESPACIOS, fila*200+ESPACIOS), ANCHO_CRUZ)
                pygame.draw.line(screen, Rojo, (columna*200+ESPACIOS,fila*200+ESPACIOS), (columna*200+200-ESPACIOS, fila*200+200-ESPACIOS), ANCHO_CRUZ)

def intromenu():
    point = 0
    while 1:
        fondo_menu = pygame.image.load("images/background.jpg")
        screen.blit(fondo_menu, (0, 0))
        tic_tac_toe = menufont.render("TIC TAC TOE", True, Verde )
        screen.blit(tic_tac_toe, (165,60))
        if point == 0:
            start = menufont2.render("*Jugar*", True, Dorado)
            quit = menufont2.render("*Salir*", True, White)
            credits = menufont2.render("*Créditos*", True, White)
        elif point == 1:
            start = menufont2.render("*Jugar*", True, White)
            credits = menufont2.render("*Créditos*", True, Dorado)
            quit = menufont2.render("*Salir*", True, White)
        elif point == 2:
            start = menufont2.render("*Jugar*", True, White)
            credits = menufont2.render("*Créditos*", True, White)
            quit = menufont2.render("*Salir*", True, Dorado)
        screen.blit(start, (340,200))
        screen.blit(credits, (320,300))
        screen.blit(quit, (340, 400))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    point += 1
                elif evento.key == pygame.K_UP:
                    point -= 1
                elif evento.key == pygame.K_RETURN:
                    if  point == 0:
                        return True
                    elif point == 1:
                        return creditos()
                    elif point == 2:
                        pygame.quit()
                        sys.exit()
        point = point % 3
        pygame.display.update()







if intromenu() == True:
    pygame.display.set_caption("Controles")
    fondo_menu = pygame.image.load("images/controles 1.png")
    screen.blit(fondo_menu, (100, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                pygame.display.set_caption("Juego")
                game_over = False
                screen.fill(Color_de_fondo)
                lineas()
    pygame.display.update()




while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mousex = evento.pos[0]
            mousey = evento.pos[1]

            fila_selec = int(mousey // 200)
            columna_selec = int(mousex // 200)
            if fila_selec <=2 and columna_selec <=2:
                if casillas_sin_marcar(fila_selec, columna_selec):
                    if jugador == 1:
                        marcar_casilla(fila_selec, columna_selec, 1)
                        sonidocirculo.play()
                        if ganador(jugador):
                            game_over = True
                        jugador = 2
                    elif jugador == 2:
                        marcar_casilla(fila_selec, columna_selec, 2)
                        sonidocruz.play()
                        if ganador(jugador):
                            game_over = True
                        jugador = jugador % 2 + 1
                        jugador = 1

                    figuras()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("music/music1.wav")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)
                reseteo()
                game_over = False

    pygame.display.update()


