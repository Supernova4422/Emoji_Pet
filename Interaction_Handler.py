from pygame.locals import *
import pygame
from INTERACTION import *
from typing import List, Tuple


class Interaction_Handler():
    def __init__(self):
        print("Mood")

    def get(self) -> List[Tuple[INTERACTION, int]]:
        events = pygame.event.get()
        interactions: List[Tuple[INTERACTION, int]] = []
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    interactions.append((INTERACTION.BUTTON_L, 0))
                if event.key == pygame.K_RIGHT:
                    interactions.append((INTERACTION.BUTTON_R, 0))
                if event.key == pygame.K_UP:
                    interactions.append((INTERACTION.ROLL, -8))
                if event.key == pygame.K_0:
                    interactions.append((INTERACTION.DISTANCE, 0))
                if event.key == pygame.K_1:
                    interactions.append((INTERACTION.DISTANCE, 0))
                if event.key == pygame.K_DOWN:
                    interactions.append((INTERACTION.ROLL, -8))
                if event.key == pygame.K_COMMA:
                    interactions.append((INTERACTION.BUTTON_LESS_THAN, 0))
                if event.key == pygame.K_PERIOD:
                    interactions.append((INTERACTION.BUTTON_GREATER_THAN, 0))
                if event.key == pygame.K_y:
                    interactions.append((INTERACTION.YEET, 0))
                if event.key == pygame.K_f:
                    interactions.append((INTERACTION.FEED, 0))
            elif event.type == QUIT:
                interactions.append((INTERACTION.EXIT, 0))
        return interactions
