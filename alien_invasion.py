import sys
import pygame
from pygame.sprite import Group
from game_stats import GameStats

from setting import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize pygame,settings and screen object.
    pygame.init()
    ai_settings= Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion -Prazwal D. Stark")
    #Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    #Make a ship ,a group of bullets, and a group of aliens.
    ship = Ship(ai_settings,screen)
    #Make a groupto store bullets in.
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen,ship,aliens)

    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(ai_settings,ship,screen,aliens, bullets)
        gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        
run_game() 

