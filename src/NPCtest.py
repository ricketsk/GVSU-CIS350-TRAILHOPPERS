from bearlibterminal import terminal as blt
from formatted_log import MessageList, FrameWithScrollbar
import random
import math
import tracery
from tracery.modifiers import base_english

from npc import NPC
from enemy import Enemy

padding_left = 4
padding_right = 4
padding_top = 2
padding_bottom = 2
mouse_scroll_step = 2 # 2 text rows per mouse wheel step.

class World(object):
  def __init__(self):
    self._width = 80
    self._height = 24
    self._map = self.generateMap()

  def generateMap(self):
    # Prefill map with floor
    loc_map = [[1 for i in range(self._width)] for j in range(self._height)]

    # Add borders
    for i in range(self._width):
      loc_map[0][i] = 0
      loc_map[self._height-1][i] = 0
    for i in range(self._height):
      loc_map[i][0] = 0
      loc_map[i][self._width-1] = 0

    # Add some water
      loc_map[5][5] = 2
      loc_map[5][6] = 2
      loc_map[6][5] = 2
      loc_map[6][6] = 2

    return loc_map

  def getRaw(self,row,col):
    return self._map[row][col]

  def getSymbol(self,row,col):
    if self._map[row][col] == 0: # Wall
      return ('\u2588', 'white', 'bold')
      #return (0x2588, 'white', 'bold')
    elif self._map[row][col] == 1: # Walkable
      return ('\u2591', 'light gray', None)
      #return (0x2591, 'light gray', None)
    elif self._map[row][col] == 2: # Water
      return ('\u259A', 'blue', 'bold')
      #return (0x2635, 'blue', 'bold')

  def validMove(self, player_x, player_y):
    if self._map[player_y][player_x] == 1:
      return True
    else:
      return False

if __name__ == "__main__":
  world    = World()
  messages = MessageList()
  frame    = FrameWithScrollbar(messages)
  curr_npc = None

  #prompt = \
  #  "Hello adventurer!\n"\
  #  "-----------------\n"\
  #  "welcome to the MONEY PLANE"
  ##    "Use arrow keys or mouse wheel to scroll the list up and down. " \
  ##    "Try to resize the window.\n\n--- --- ---"
  #messages.append(prompt)

  blt.open()
#  blt.set("window: fullscreen=true; font: UbuntuMono-R.ttf, size=10x20") 
#  blt.set("italic font: VeraMoIt.ttf, size=10x20")
#  blt.set("bold font: VeraMoBd.ttf, size=10x20")
#  blt.set("huge font: VeraMono.ttf, size=20x40, spacing=2x2")
  blt.set("U+E100: Runic.png, size=8x16")
  blt.set("U+E200: Tiles.png, size=32x32, align=top-left")
  blt.set("U+E300: fontawesome-webfont.ttf, size=24x24, spacing=3x2, codepage=fontawesome-codepage.txt")
  blt.set("window: size=80x25, cellsize=auto, title='NPC test'; font: default")



  blt.composition(True)
#  blt.set("font: size=32x32;")

#  blt.color("light gray")
#  blt.printf(1, 1, 'Hello, world!')
  blt.refresh()

  player_x = 1
  player_y = 1

  # Generate NPCs
  npcs = []
  for i in range(10):
    npc_done = False
    while not npc_done:
      locX = random.randrange(1,80)
      locY = random.randrange(1,24)
      if world.validMove(locX, locY):
        npc_done = True
        npcs.append(NPC('no-purpose', (locX, locY)))

  # Generate enemies
  enemies = []
  for i in range(4):
    enemy_done = False
    while not enemy_done:
      locX = random.randrange(1,80)
      locY = random.randrange(1,24)
      if world.validMove(locX, locY):
        enemy_done = True
        enemies.append(Enemy('popcorn', (locX, locY)))

  # Initial update
  frame.update_geometry(
      padding_left,
      padding_top,
      blt.state(blt.TK_WIDTH) - (padding_left + padding_right + 1),
      blt.state(blt.TK_HEIGHT) - (padding_top + padding_bottom))

  frame_active = False
 
  while True:#blt.read() != blt.TK_CLOSE:
    blt.clear()

    if frame_active:
        frame.draw()
        blt.color("white")
        blt.layer(1)
        blt.puts(padding_left, padding_top + 0 - frame.offset, "│" + curr_npc.getName() + "│", frame.width)
        sep = "└"
        for x in range(len(curr_npc.getName())):
          sep += "─"
        sep += "┘\n"
        blt.puts(padding_left, padding_top + 1 - frame.offset, sep, frame.width)
        current_line = 2
        for text, height in messages:
            print(text)
            if current_line + height >= frame.offset:
                # stop when message is below frame
                if current_line - frame.offset > frame.height: break
                # drawing message
                blt.puts(padding_left, padding_top + current_line - frame.offset, text, frame.width)
            current_line += height + 1
        blt.crop(padding_left, padding_top, frame.width, frame.height)

    else: 
      # Draw map
      blt.layer(0)
      blt.color("light orange")
      for i in range(world._height):
        for j in range(world._width):
          rawval = world.getRaw(i,j)

          if rawval == 0:
            blt.put(j,i,0xE200+8)
          elif rawval == 1:
            blt.put(j,i,0xE200+0)
          elif rawval == 2:
            blt.put(j,i,0xE200+4)
          else:
            blt.put(j,i,0xE200+15)



#          symbol = world.getSymbol(i,j)
#          if symbol[2]:
#            blt.puts(j,i,"[color={0}][font={1}]{2}[/font][/color]".format(symbol[1],symbol[2],symbol[0]))
#          else:
#            blt.puts(j,i,"[color={0}]{1}[/color]".format(symbol[1],symbol[0]))


      blt.color("light gray")
      blt.printf(1, 0, 'Hello, world!')

      blt.color("yellow")
      #blt.puts(player_x, player_y, "@")
      blt.put(player_x, player_y, 0xE200+10)

      for npc in npcs:
        blt.color("light orange")
        blt.puts(npc._x, npc._y, npc._symbol)

        blt.layer(2)
        blt.puts(npc._x+1,npc._y-3,
          " ┌──────┐  \n"
          " │Hey,..└─┐\n"
          " │listen!.│\n"
          " └────────┘\n"
        )

      for enemy in enemies:
        blt.color("red")
        blt.puts(enemy._x, enemy._y, enemy._symbol)

        #blt.layer(2)
        #blt.puts(enemy._x+1,enemy._y-3,
        #  " ┌──────┐  \n"
        #  " │Hey,..└─┐\n"
        #  " │listen!.│\n"
        #  " └────────┘\n"
        #)
#────
#        "│.........┌─┘\n"
#        "│.....┌─────┘  \n"
#        "└───
#        ─┘        \n"
#        "   ┌────────┐  \n"
#        "   │Hey,....└─┐\n"
#        "┌──┘listen!...│\n"
#        "│.............│\n"
#        "│...........┌─┘\n"
#        "│.....┌─────┘  \n"
#        "└─────┘        \n"
#      )


    # Render
    blt.refresh()

    key = blt.read()
    if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
      break

    if not frame_active:

      if key == blt.TK_RIGHT:
        if world.validMove(player_x+1,player_y):
          player_x += 1
      elif key == blt.TK_LEFT:
        if world.validMove(player_x-1,player_y):
          player_x -= 1
      elif key == blt.TK_UP:
        if world.validMove(player_x,player_y-1):
          player_y -= 1
      elif key == blt.TK_DOWN:
        if world.validMove(player_x,player_y+1):
          player_y += 1
      elif key == blt.TK_H:
        frame_active = True
      elif key == blt.TK_PERIOD:
        pass
        #loadHelp()

      # Update NPCs

      # Only move if the euclidean distance is somewhat far (annoying to 'catch up' to an NPC)
      for npc in npcs:
        npc_pos = npc.getPos()
        euc_distance = int(math.sqrt(math.pow(player_x - npc_pos[0],2) + math.pow(player_y - npc_pos[1], 2)))
        if euc_distance > 2:
          move = npc.move()
          if move and world.validMove(npc._x+move[0], npc._y+move[1]):
            npc.updatePosition(move[0], move[1])

        # chet
        if player_x == npc._x and player_y == npc._y:
          frame_active = True
          curr_npc = npc

          messages.append(npc.getCurrentMessage())
          frame.update_geometry(
              padding_left,
              padding_top,
              blt.state(blt.TK_WIDTH) - (padding_left + padding_right + 1),
              blt.state(blt.TK_HEIGHT) - (padding_top + padding_bottom))

      #print((player_x, player_y), (npc._x, npc._y))

  #prompt = \
  #  "Hello adventurer!\n"\
  #  "-----------------\n"\
  #  "welcome to the MONEY PLANE"
  ##    "Use arrow keys or mouse wheel to scroll the list up and down. " \
  ##    "Try to resize the window.\n\n--- --- ---"
  #messages.append(prompt)


    else:
        if key == blt.TK_H:
          frame_active = False
          curr_npc = None
          messages.clear()

        elif key == blt.TK_UP:
            frame.scroll(-1)
            
        elif key == blt.TK_DOWN:
            frame.scroll(1)

        elif key == blt.TK_MOUSE_SCROLL:
            # Mouse wheel scroll
            frame.scroll(mouse_scroll_step * blt.state(blt.TK_MOUSE_WHEEL))

        elif key == blt.TK_MOUSE_LEFT and blt.state(blt.TK_MOUSE_X) == frame.scrollbar_column:
            py = blt.state(blt.TK_MOUSE_PIXEL_Y)
            if frame.scrollbar_offset <= py <= frame.scrollbar_offset + frame.scrollbar_height * blt.state(blt.TK_CELL_HEIGHT):
                # Clicked on the scrollbar handle: start dragging
                dragging_scrollbar = True
                dragging_scrollbar_offset = py - frame.scrollbar_offset
            else:
                # Clicked outside of the handle: jump to position
                frame.scroll_to_pixel(blt.state(blt.TK_MOUSE_PIXEL_Y) - frame.scrollbar_height * blt.state(blt.TK_CELL_HEIGHT) // 2)

        elif key == blt.TK_MOUSE_LEFT | blt.TK_KEY_RELEASED :
            dragging_scrollbar = False

        elif key == blt.TK_MOUSE_MOVE:
            if dragging_scrollbar:
                frame.scroll_to_pixel(blt.state(blt.TK_MOUSE_PIXEL_Y) - dragging_scrollbar_offset)            

            while blt.peek() == blt.TK_MOUSE_MOVE:
                blt.read()

        elif key == blt.TK_RESIZED:
            frame.update_geometry(
                padding_left,
                padding_top,
                blt.state(blt.TK_WIDTH) - (padding_left + padding_right + 1),
                blt.state(blt.TK_HEIGHT) - (padding_top + padding_bottom))




        
  blt.set("U+E100: none; U+E200: none; U+E300: none")        
  blt.composition(False)
  blt.close()

