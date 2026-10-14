# Packet Sniffer for Ethical Cybersecurity with Py GUI
import pygame
import scapy
import json # Settings
import sqlite3 # Store data into dataset 


pygame.init()
window = pygame.dispaly.set_mode((500,800))
pygame.display.set_caption("-------------- Cyber Tools --------------")
run = True

WHITE = (255, 255, 255)
BLUE = (50, 150, 250)
HOVER_BLUE = (100, 180, 255)
DARK_BLUE = (20, 80, 180)
TEXT_COLOR = (255, 255, 255)



class UI():

    class Button():
        pass

    class Slider():
        pass

    class Text_Notes():
        pass
        
    class Save_Store_Data():
        pass



for event in pygame.event.get():
    if pygame.type == pygame.QUIT():
        run = False
