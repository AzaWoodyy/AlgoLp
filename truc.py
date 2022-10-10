
import socketio
import sys, pygame

sio = socketio.Client()
sio.connect('http://10.7.178.157:81')
playerList = []

@sio.event
def players(data):
    global playerList
    playerList = data

print("Listening.......")

pygame.init()

w,h = 1024, 768
screen = pygame.display.set_mode((w,h))
print(pygame.display.get_window_size())


# ICI ON DEFINIT DES TRUCS


play = True
clock = pygame.time.Clock()

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            pass
            # print(event.pos)
        if event.type == pygame.KEYUP:
            print(event.key, event.unicode, event.scancode)
            if event.key == pygame.K_ESCAPE:
                play = False

    screen.fill((255, 100,0))

    # ICI ON AFFICHE ET ON BOUGE DES TRUCS

    clock.tick(60)
    pygame.display.flip()