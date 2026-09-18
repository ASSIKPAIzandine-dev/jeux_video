import pygame
from sprites.cat import Cat
from sprites.mouse import Mouse
from typing import List

class Game:
        screen:pygame.Surface=None
        clock:pygame.time.Clock=None
        
        def __init__(self,title:str,size:tuple):
                pygame.init()

                self.screen=pygame.display.set_mode(size)
                pygame.display.set_caption(title)
                self.clock=pygame.time.Clock()
                
                _,_,sw,sh=self.screen.get_rect()
                self.cats_group=pygame.sprite.Group()
                self.cat=Cat((100,600))
                self.cats_group.add(self.cat)
                
                x,y,cw,ch=self.cat.rect
                mouse_y=sh-100
                self.mouses_group=pygame.sprite.Group()
                # self.mouses_group.add(Mouse((500,mouse_y)))
                self.nb_souris=0
                
                self.font=pygame.font.Font("./fonts/mon_font/Roboto-Italic-VariableFont_wdth,wght.ttf",40)
                self.scoreTexte=self.font.render(f"Score:{self.cat.life_score}",False,(0,0,255),(0,255,0))
                self.image=pygame.image.load("./images/back.jpeg")
                self.back_image=pygame.image.load("./images/game_over.jpeg")
                self.is_run:bool=False
                
        def generate_mouse(self,nbre_mouse:int):
                _,_,sw,sh=self.screen.get_rect()
                mouse_y=sh-100
                espace=0
                for i in range (nbre_mouse):
                        self.mouses_group.add(Mouse(((300+espace),mouse_y)))
                        espace+=200
               
        def game_over(self):
                for cat in self.cats_group:
                      cat.kill()
                for mouse in self.mouses_group:
                      mouse.kill()          
                self.is_run=False
      
        def update_game(self):
                pygame.mixer.init()
                self.cats_group.update()
                self.mouses_group.update()
                if self.cat.is_in_start_position:
                        self.generate_mouse(5)
                        self.cat.set_not_in_start_position()   
                array_mouse_collision=pygame.sprite.spritecollide(self.cat,self.mouses_group,True)
                if(array_mouse_collision):
                        self.cat.eat(array_mouse_collision)     
                        pygame.mixer.Sound("./musiques/souris.mp3") 
                if(len(array_mouse_collision)!=0):
                        self.nb_souris+=1
                self.scoreTexte=self.font.render(f"Score:{self.cat.life_score}",False,(0,0,255),(0,255,0))
                if self.cat.life_score==0:
                        self.game_over()
        def restart(self):
                self.is_run=True
                self.generate_mouse(3)
                _,_,sw,sh=self.screen.get_rect()
                self.cats_group=pygame.sprite.Group()
                self.cat=Cat((100,600))
                self.cats_group.add(self.cat)
               
                
                                         
        def play_music(self):
                pygame.mixer.init()
                pygame.mixer.music.load("./musiques/son_chat.mp3")
                pygame.mixer.music.play(loops=-1)
          
        def game_run_loop(self):
            self.play_music()
            running = True

            while running:    
                #listen events
                for event in pygame.event.get():                
                        if event.type == pygame.QUIT:
                            running = False
                        if not self.is_run and event.type==pygame.MOUSEBUTTONUP:
                             self.restart()
                            
                # update
                self.update_game()
                # le rendu
                if self.is_run:
                        self.screen.blit(self.image,(0,0))
                        self.cats_group.draw(self.screen)
                        self.mouses_group.draw(self.screen)
                        self.screen.blit(self.scoreTexte,(905,0))
                else:
                        self.screen.blit(self.back_image,(0,0))
                
                pygame.display.flip()
                self.clock.tick(40)

# # quiter le jeux
        pygame.quit()

       
        
        
