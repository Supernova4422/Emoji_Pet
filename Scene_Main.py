from Emoji import Emoji
from typing import List
import pygame
from pygame.locals import *
import sys
import math
from Accessory import *
from INTERACTION import *
from sys import platform
from Food import *
if platform == "linux" or platform == "linux2":
    from Arduino_Interaction_Handler import *
else:
    from Interaction_Handler import *


class Scene_Main():
    def __init__(self):
        pygame.init()

        self.w = 640
        self.h = 480
        self.windowSurface = pygame.display.set_mode(
            (self.w, self.h))

        self.emoji = Emoji(x=160, y=160, scene_width=128, scene_height=128)
        self.items: List[Entity] = [
            Accessory(x=50, y=50, w=128, h=128)
        ]

        if platform == "linux" or platform == "linux2":
            self.interaction_handler = Arduino_Interaction_Handler()
        else:
            self.interaction_handler = Interaction_Handler()

    def loop(self):
        max_counter = 10
        counter = max_counter
        while True:
            pygame.time.Clock().tick(60)
            if platform == "linux" or platform == "linux2":
                self.events = pygame.event.get()
                if (counter == 0):
                    self.input()
                    counter = max_counter
                else:
                    counter -= 1

            if platform != "linux" and platform != "linux2":
                self.input()

            self.update()
            self.render()

    def update(self):
        self.emoji.update(self.w, self.h)
        self.emoji.update_position(self.w, self.h)

        for item in self.items:
            item.update(self.w, self.h, self.emoji, self)
            item.update_position(self.w, self.h)

    def render(self):
        BLACK = (0, 0, 0)
        self.windowSurface.fill(BLACK)
        self.emoji.draw(self.windowSurface)

        for item in self.items:
            item.draw(self.windowSurface)

        self.items = [i for i in self.items if i.dead == False]

        pygame.display.flip()

    def yeet_accessory(self):
        # add accessory into frame
        # yeet it
        # change emoji mood to neutral
        if(self.emoji.mood in self.emoji.cool_moods):
            flying_hat = Accessory(
                x=self.emoji.get_pos()[0],
                y=self.emoji.get_pos()[1] - self.emoji.h,
                w=128,
                h=128,
                mood=self.emoji.mood
            )
            flying_hat.yeet()
            flying_hat.is_constrained = False
            flying_hat.lifeTime = 100
            flying_hat.noCollide(50)
            self.items.append(flying_hat)
            self.emoji.mood = "happy"

    def input(self):
        actions: List[Tuple[INTERACTION, int]] = self.interaction_handler.get()

        for interaction, arg in actions:
            if interaction is INTERACTION.BUTTON_L:
                if arg == 0:
                    self.items.append(
                        Accessory(x=10, y=50, w=128, h=128, mood="cowboy"))
                else:
                    self.items.append(
                        Accessory(x=10, y=50, w=128, h=128, mood="sunglasses"))
            elif interaction is INTERACTION.BUTTON_R:
                self.emoji.bounce()
            elif interaction is INTERACTION.ROLL:
                self.emoji.roll(arg, self)
            elif interaction is INTERACTION.BOUNCE:
                if self.emoji.mood is not "scared":
                    self.emoji.bounce()
                    if self.emoji.mood in ("cowboy", "sunglasses"):
                        self.yeet_accessory()
                    self.emoji.mood = "scared"
            elif interaction is INTERACTION.BUTTON_LESS_THAN:
                self.emoji.mood = "cowboy"
            elif interaction is INTERACTION.BUTTON_GREATER_THAN:
                self.emoji.mood = "sunglasses"
            elif interaction is INTERACTION.YEET:
                print("yeeet!s")
                self.emoji.rescale()
                self.yeet_accessory()
            elif interaction is INTERACTION.DISTANCE:
                self.hand.on_input(arg)
            elif interaction is INTERACTION.FEED:
                self.items.append(Food(x=10, y=50, w=128, h=128))
            elif interaction is INTERACTION.EXIT:
                pygame.quit()
                sys.exit()
            else:
                raise NotImplementedError()
