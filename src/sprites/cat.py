import pygame
import os
from config import (SCREEN_WIDTH,SCREEN_HEIGH)
print(os.getcwd)
from sprites.mouse import Mouse
class Cat(pygame.sprite.Sprite):
    
        image:pygame.Surface=None
        rect:pygame.Rect=None
        frames:list[pygame.Surface]
        current_cat_x=0
        current_frame_index:int
    
        def __init__(self,position):
                super().__init__()
                self.load_sprite_sheet()     
                self.current_frame_index=0
                self.image = self.frames[self.current_frame_index]
                # self.position=position
                self.life_score=7
                self.rect=self.image.get_rect(center=position)
                self.nb_eat_food=0
                self.is_in_start_position=True
                         
        def eat(self,mouses:list[Mouse]):
                for mouse in mouses: 
                         if mouse.is_stick:
                                 self.decrementer_life()
                         else:
                                 self.incremente_life()                             
        def incremente_life(self):
                self.life_score+=1 if self.life_score<7 else 0
                                
        def decrementer_life(self):
                self.life_score-=1 if self.life_score>=1 else 0
                                            
        def set_not_in_start_position(self):
                self.is_in_start_position=False
                
        def set_in_start_position(self):
                self.is_in_start_position=True
                  
        def update(self):
                super().update()
                keys=pygame.key.get_pressed()
                if(keys[pygame.K_RIGHT]):
                  self.move_right()
                if(keys[pygame.K_LEFT]):
                  self.move_left()
               

        def load_sprite_sheet(self):
                sprite_sheets=pygame.image.load("./images/cat_spritesheet.png").convert_alpha()
                FRAME_WITDH=204
                FRAME_HEIGH=204
                self.frames=[]  
                # 0 a 2
                for i in range (3):
                     frame= sprite_sheets.subsurface((i*FRAME_WITDH,0,FRAME_WITDH,FRAME_HEIGH))
                     self.frames.append(frame)
        

        def move_right(self):
                self.rect.x+=15
                if(self.rect.x>=SCREEN_WIDTH):
                        self.reset_position()
                self.animate_right()
               
        def move_left(self):
            self.animated_left()
           
        def  animate_right(self):
               
                self.current_frame_index+=1
                if(self.current_frame_index==len(self.frames)):
                    self.current_frame_index=0
                self.image = self.frames[self.current_frame_index]

        def animated_left(self):
                 self.rect.x-=25
                 self.current_frame_index+=1
                 if(self.current_frame_index==len(self.frames)):
                     self.current_frame_index=0
                 self.image = self.frames[self.current_frame_index]
                 
        def reset_position(self):
                self.rect.x=0
                self.set_in_start_position()
                
                

             


        
        
        
        
        
        
        