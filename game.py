from microbit import *
import time
import random

blocks = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
player = [2, 4]
updateInterval = 1.5 #in seconds
updateTime = time.time() + updateInterval

def updateBlockLogic():
   global updateTime, blocks
   if time.time() >= updateTime:
      updateTime = time.time() + updateInterval

      for b in blocks:
         if b[1] != -1:
            b[1] += 1
         if b[1] == 5:
            b[1] = -1

      rblock = blocks[random.randint(0, len(blocks)-1)]
      if rblock[1] == -1:
         rblock[0] = random.randint(0, 5) # random x position
         rblock[1] = 0

def draw():
   global blocks, player
   display.clear()   
   for b in blocks:
      if b[1] != -1:
         display.set_pixel(b[0], b[1], 5)

   display.set_pixel(player[0], player[1], 9)


while True:
   updateBlockLogic()
   draw()