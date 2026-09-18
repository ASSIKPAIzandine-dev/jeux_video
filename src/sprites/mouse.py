import pygame
import random

from config import (SCREEN_WIDTH,SCREEN_HEIGH)
class Mouse(pygame.sprite.Sprite):
        image:pygame.Surface=None
        rect:pygame.Rect=None
         
        def __init__(self,position):
            super().__init__()
            # self.image=pygame.Surface((50,70))
            self.image=pygame.image.load("./images/food.png").convert_alpha()
            self.rect=self.image.get_rect(center=position)
            self.is_stick=True
            #bool(random.randint(0,1))
            
        def checkout_of_screen(self):
            if(self.rect.x>=SCREEN_WIDTH):
                self.kill()
                    
        def move_right(self): 
            self.rect.x+=random.randint(1,10)
            self.checkout_of_screen()
            
        def update(self):
            super().update()
            self.move_right()
         


            

    
    

