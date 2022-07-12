from tile_map import TileMap
from venv import create
import pygame
from pygame.locals import *
# ---------------------------
# other imports
import math
import sys
import time
import random

# constants
SCREENSIZE = WIDTH, HEIGHT = 1000, 1000

_VARS = {'surf': False}


def main():
    pygame.init()
    pygame.font.init()

    my_font = pygame.font.SysFont('Comic Sans MS', 12)
    origin = [460, -100]
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    tile_map = TileMap(origin=origin, tile_size=50, tile_amount=8)
    tile_map.create_tile_list()

    while True:
        mouse_pos = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
        x, y = mouse_pos
        mouse_tile_index = tile_map.check_which_tile(x, y)

        if mouse_tile_index is not None:
            mouse_tile = tile_map.tile_list[mouse_tile_index]
            mouse_tile.toggle_hover()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_tile_index is not None:
                        tile_map.select_tile(mouse_tile_index)
                        if not mouse_tile.selected:
                            mouse_tile.toggle_hover()
                elif event.button == 3: 
                    tile_map.add_collisions([[0,1], [1,1], [2,2]])
                    print(tile_map.collision_map)

        _VARS['surf'].fill((115, 115, 115))
        for tile in tile_map.tile_list:
            tile.draw_tile()

        for index, tile in enumerate(tile_map.tile_list):
            # display tile indicies
            txt_surface = my_font.render(f'{index}', False, (0, 0, 0))
            _VARS['surf'].blit(txt_surface, tile.centre)
            _VARS['surf'].blit(txt_surface, (100, 0))
            pygame.draw.circle(_VARS['surf'], (0, 0, 0),
                               tile.centre, 2)
            
        
        if tile_map.path: 
            # tile_map.draw_path()
            for index, node_index in enumerate(tile_map.path):
                if index - 1 > -1: 
                    pygame.draw.line(_VARS['surf'], (255,255,255), tile_map.tile_list[tile_map.path[index-1]].centre, tile_map.tile_list[tile_map.path[index]].centre)

        # pygame.draw.line(_VARS['surf'], (255, 255, 255), [510, 217.5], [485, 230])
        pygame.display.update()
        if mouse_tile_index is not None:
            mouse_tile.toggle_hover()
        pygame.time.Clock().tick(144)


if __name__ == '__main__':
    main()
