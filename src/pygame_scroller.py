#! /usr/bin/python

# https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame

import pygame
from pygame import *
import random
import numpy as np
import tcod
from typing import Tuple, Iterator, List, TYPE_CHECKING

SCREEN_SIZE = pygame.Rect((0, 0, 800, 640))
TILE_SIZE = 32 
GRAVITY = pygame.Vector2((0, 0.3))
PRESS_DELAY = 250

class GameMap: # from TCOD tutorial
  def __init__(self, width: int, height: int):
    self.width, self.height = width, height
    self.tiles = np.full((width, height), fill_value='P', order='F')

class RectangularRoom:
  def __init__(self, x:int, y: int, width: int, height: int):
    self.x1 = x
    self.y1 = y
    self.x2 = x + width
    self.y2 = y + height

  @property
  def center(self) -> Tuple[int, int]:
    center_x = int((self.x1 + self.x2) / 2)
    center_y = int((self.y1 + self.y2) / 2)
    return center_x, center_y

  @property
  def inner(self) -> Tuple[slice, slice]:
    # Return inner area as 2D array index
    return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

  def intersects(self, other) -> bool:
    # Return true if overlappign with another room
    return (
      self.x1 <= other.x2
      and self.x2 >= other.x1
      and self.y1 <= other.y2 
      and self.y2 >= other.y1
    )

def generate_dungeon(
  max_rooms: int,
  room_min_size: int,
  room_max_size: int,
  map_width: int,
  map_height: int
) -> GameMap:
  dungeon = GameMap(map_width, map_height)

  player_x, player_y = 0,0

  rooms: List[RectangularRoom] = []

  for r in range(max_rooms):
    room_width = random.randint(room_min_size, room_max_size)
    room_height = random.randint(room_min_size, room_max_size)

    x = random.randint(0, dungeon.width - room_width - 1)
    y = random.randint(0, dungeon.height - room_height - 1)

    new_room = RectangularRoom(x, y, room_width, room_height)

    if any(new_room.intersects(other_room) for other_room in rooms):
      continue

    dungeon.tiles[new_room.inner] = ' '

    
    if len(rooms) == 0:
      player_x, player_y = new_room.center
    else:
      for x, y in tunnel_between(rooms[-1].center, new_room.center):
        dungeon.tiles[x, y] = ' '

    rooms.append(new_room)

  return dungeon, player_x, player_y

def tunnel_between(
  start: Tuple[int, int], end: Tuple[int, int]
) -> Iterator[Tuple[int, int]]:
  x1, y1 = start
  x2, y2 = end
  if random.random() < 0.5:
    corner_x, corner_y = x2, y1
  else:
    corner_x, corner_y = x1, y2

  for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
    yield x, y
  for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
    yield x, y




class CameraAwareLayeredUpdates(pygame.sprite.LayeredUpdates):
    def __init__(self, target, world_size):
        super().__init__()
        self.target = target
        self.cam = pygame.Vector2(0, 0)
        self.world_size = world_size

        if self.target:
            self.add(target)

    def update(self, *args):
        super().update(*args)
        if self.target:
            x = -self.target.rect.center[0] + SCREEN_SIZE.width/2
            y = -self.target.rect.center[1] + SCREEN_SIZE.height/2
            self.cam += (pygame.Vector2((x, y)) - self.cam) * 0.05
            self.cam.x = max(-(self.world_size.width-SCREEN_SIZE.width), min(0, self.cam.x))
            self.cam.y = max(-(self.world_size.height-SCREEN_SIZE.height), min(0, self.cam.y))

    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect.move(self.cam))
            if rec is init_rect:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty            

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()

    game_map, p_x, p_y = generate_dungeon(
      max_rooms=30,
      room_min_size=6,
      room_max_size=10,
      map_width=100,
      map_height=100
    )
   
    print(game_map.tiles)
    level = []
    for i in range(100):
      l = ""
      for j in range(100):
        l += game_map.tiles[i][j]
      level.append(l)


#    level = [
#        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
#        "P                                          P",
#        "P     N   N                                P",
#        "P                                          P",
#        "P                    PPPPPPPPPPP           P",
#        "P                                          P",
#        "P                                          P",
#        "P                                          P",
#        "P    PPPPPPPP                              P",
#        "P                                          P",
#        "P                          PPPPPPP         P",
#        "P                 PPPPPP                   P",
#        "P                                          P",
#        "P         PPPPPPP                          P",
#        "P                                          P",
#        "P                     PPPPPP               P",
#        "P                                          P",
#        "P   PPPPPPPPPPP                            P",
#        "P                                          P",
#        "P                 PPPPPPPPPPP              P",
#        "P                                          P",
#        "P                                  E       P",
#        "P                                          P",
#        "P             N                            P",
#        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]


#    level = []
#    for row in range(100):
#      x = ""
#      for col in range(100):
#        if col == 0 or row == 0 or col == 99 or row == 99:
#          x += "P"
#        else:
#          x += " "
#      level.append(x)





    print(p_x,p_y)
    p_x *= TILE_SIZE
    p_y *= TILE_SIZE

    platforms = pygame.sprite.Group()
    npcs = pygame.sprite.Group()
    player = Player(platforms, npcs, (p_x,p_y))#(TILE_SIZE, TILE_SIZE))
    level_width  = len(level[0])*TILE_SIZE
    level_height = len(level)*TILE_SIZE
    entities = CameraAwareLayeredUpdates(player, pygame.Rect(0, 0, level_width, level_height))

    # build the level
    x = y = 0
    for row in level:
        for col in row:
            if col == "P":
                Platform((x, y), platforms, entities)
            if col == "E":
                ExitBlock((x, y), platforms, entities)
            if col == "N":
                NPC((x, y), platforms, npcs, entities)
            x += TILE_SIZE
        y += TILE_SIZE
        x = 0

    while 1:

        for e in pygame.event.get():
            if e.type == QUIT: 
                return
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return
            if e.type == KEYUP:    # tile-based movement -- no holding!
              player.clearPress()

        entities.update()

        screen.fill((0, 0, 0))
        entities.draw(screen)
        pygame.display.update()
        timer.tick(60)

class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        self.image = Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

class Player(Entity):
    def __init__(self, platforms, npcs, pos, *groups):
        super().__init__(Color("#00FF00"), pos)
        self.vel = pygame.Vector2((0, 0))
        self.onGround = False
        self.platforms = platforms
        self.npcs = npcs
        self.speed = 8
        self.jump_strength = 10
        #self.keyPressed = False
        self.ticks = 0

    def clearPress(self):
      self.keyPressed = False

    def update(self):
        pressed = pygame.key.get_pressed()

        up      = pressed[K_UP]
        left    = pressed[K_LEFT]
        right   = pressed[K_RIGHT]
        running = pressed[K_SPACE]
        down    = pressed[K_DOWN]

        trigger_update = False

        if down:# and not self.keyPressed:
          now = pygame.time.get_ticks()
          if (now - self.ticks) > 100:
            self.ticks = now
            self.vel.y = 32
            trigger_update = True
        #  self.keyPressed = True
        if up:# and not self.keyPressed:
          now = pygame.time.get_ticks()
          if (now - self.ticks) > 100:
            self.ticks = now
            self.vel.y = -32
            trigger_update = True
        #  self.keyPressed = True
        if left:# and not self.keyPressed:
          now = pygame.time.get_ticks()
          if (now - self.ticks) > 100:
            self.ticks = now
            self.vel.x = -32
            trigger_update = True
        #  self.keyPressed = True
        if right:# and not self.keyPressed:
          now = pygame.time.get_ticks()
          if (now - self.ticks) > 100:
            self.ticks = now
            self.vel.x = 32
            trigger_update = True
        #  self.keyPressed = True

        if trigger_update:
          for n in self.npcs:
            n.setUpdate(True)

#        if up:
#
#            # only jump if on the ground
#            if self.onGround: self.vel.y = -self.jump_strength
#        if left:
#            self.vel.x = -self.speed
#        if right:
#            self.vel.x = self.speed
#        if running:
#            self.vel.x *= 1.5
#        if not self.onGround:
#            # only accelerate with gravity if in the air
#            self.vel += GRAVITY
#            # max falling speed
#            if self.vel.y > 100: self.vel.y = 100
#        #print(self.vel.y)
#        if not(left or right):
#            self.vel.x = 0
        # increment in x direction
        self.rect.left += self.vel.x
        # do x-axis collisions
        self.collide(self.vel.x, 0, self.platforms, self.npcs)
        # increment in y direction
        self.rect.top += self.vel.y
#        # assuming we're in the air
#        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.vel.y, self.platforms, self.npcs)
        self.vel.x = 0
        self.vel.y = 0

    def collide(self, xvel, yvel, platforms, npcs):
        for p in npcs:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, NPC):
                  print("OUCH")
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    print("WINNAR")
                    pygame.event.post(pygame.event.Event(QUIT))
                if isinstance(p, NPC):
                  print("OUCH")
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

class NPC(Entity):
    def __init__(self, platforms, npcs, pos, *groups):
        super().__init__(Color("#F0F0F0"), platforms, pos)
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        self.npcs = npcs
        self.speed = 8
        self.ticks = 0
        self.update = False

    def setUpdate(self, val):
      self.update = val


    def update(self):
        if self.update:
          if random.random() > 0.8:  # trigger a movement
            m = random.choice([0,1,2,3])
            if m == 0:
              self.vel.y = 32
            elif m == 1:
              self.vel.y = -32
            elif m == 2:
              self.vel.x = -32
            else:
              self.vel.x = 32


            # increment in x direction
            self.rect.left += self.vel.x
            # do x-axis collisions
            self.collide(self.vel.x, 0, self.platforms, self.npcs)
            # increment in y direction
            self.rect.top += self.vel.y
            # do y-axis collisions
            self.collide(0, self.vel.y, self.platforms, self.npcs)
          self.vel.x = 0
          self.vel.y = 0

    def collide(self, xvel, yvel, platforms, npcs):
        for p in npcs:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, NPC):
                  print("OUCH")
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    print("WINNAR")
                    pygame.event.post(pygame.event.Event(QUIT))
                if isinstance(p, NPC):
                  print("OUCH")
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

class Platform(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#DDDDDD"), pos, *groups)

class ExitBlock(Entity):#Platform):
    def __init__(self, pos, *groups):
        super().__init__(Color("#FF00FF"), pos, *groups)

if __name__ == "__main__":
    print("What is your favorite color?")
    main()
