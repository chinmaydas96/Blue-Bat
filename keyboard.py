from pygame import *
import serial

init()
window = display.set_mode((800, 600))

display.set_caption("Window")

endProgram = False
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
while not endProgram:
    for e in event.get():
        if e.type == KEYDOWN:
            if (e.key == K_w):
                print "W is pressed"
                ser.write('1')
            elif (e.key == K_s):
                print "S is pressed"
                ser.write('2')
            elif (e.key == K_a):
                print "A is pressed"
                ser.write('7')
            elif (e.key == K_d):
                print "D is pressed"
                ser.write('6')
            else:
                print "error"


# black = (0, 0, 0)
# white = (255, 255, 255)

# x, y = 0, 0

# moveX, moveY = 0, 0

# clock = pygame.time.Clock()

# gameLoop = True
# while gameLoop:
#     for event in pygame.event.get():
#         if (event.type == pygame.QUIT):
#             gameLoop = False
#         if (event.type == pygame.KEYDOWN):
#             if (event.key == pygame.K_LEFT):
#                 moveX = -5
#             if (event.key == pygame.K_RIGHT):
#                 moveX = 5
#             if (event.key == pygame.K_UP):
#                 moveY = -5
#             if (event.key == pygame.K_DOWN):
#                 moveY = 5
#         if (event.type == pygame.KEYUP):
#             if (event.key == pygame.K_LEFT):
#                 moveX = 0
#             if (event.key == pygame.K_RIGHT):
#                 moveX = 0
#             if (event.key == pygame.K_UP):
#                 moveY = 0
#             if (event.key == pygame.K_DOWN):
#                 moveY = 0
#     window.fill(black)
#     x += moveX
#     y += moveY
#     pygame.draw.rect(window, white, (x, y, 50, 50))
#     clock.tick(50)
#     pygame.display.flip()

# pygame.quit()
