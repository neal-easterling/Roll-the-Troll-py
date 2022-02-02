import tkinter as tk
from tkinter import Frame
from game.altscreens import StartScreen, WinScreen, LoseScreen, CreditScreen
from game.gamescreen import GameScreen
from game.responder import Responder
from game.healthbar import HealthBar
from game.dice import d20, d6
from helper.emptyobject import EmptyObject
from helper.typewriter import Typewriter
from pyglet import font

class GameApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
       
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        font.add_file('fonts/impact.ttf')
        font.add_file('fonts/OCRAEXT.TTF')

        #CONSTANTS
        self.LG_HEX = '#5be10b'
        self.DG_HEX = '#194003'
        self.LB_HEX = '#66ffff'
        self.DB_HEX = '#1a4040'
        self.YEL_HEX ='#e5c617'
        self.BG_HEX = '#000000'
        self.TITLE_FONT1 = ('Impact', 50)
        self.TITLE_FONT2 = ('Impact', 75)
        self.BUTTON_BG = self.LB_HEX
        self.BUTTON_TEXT_COLOR = "#333333"
        self.BUTTON_FONT = ('OCR A Extended', 15)
        self.INSTRUCTION_FONT =('OCR A Extended',12)
        self.QUIT_COLOR = self.LG_HEX
         
        # creating a container
        self.container = Frame(self) 
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        #create combatants (called Responders)
        self.player_name = 'player'
        self.troll = Responder('troll', 20, self, 110, 310)
        self.player = Responder(self.player_name, 20, self, 435, 335)

        #create hp bars
        self.troll_hp_bar = EmptyObject()
        self.player_hp_bar = EmptyObject()

        #create responders dice
        self.troll_d20 = d20('troll_d20', self, 175, 525, fg=self.LG_HEX)
        self.troll_d6 = d6('troll_d6', self, 275, 525, fg=self.LG_HEX)
        self.player_d20 = d20('player_d20',self, 650, 550, fg=self.LB_HEX)
        self.player_d6 = d6('player_d6', self, 550, 550, fg=self.LB_HEX)

        #create screen variables
        self.start_screen = StartScreen(parent=self.container, controller=self)
        self.game_screen = EmptyObject()
        self.lose_screen = EmptyObject()
        self.win_screen = EmptyObject()
        self.credits_screen = EmptyObject()

        #load start screen
        self.start_screen.grid(row=0, column=0, sticky="nsew")
       
  
    #TRANSITION FROM STARTSCREEN TO GAMESCREEN
    def start_trans(self, screen_from):
        print('start_trans began')
        if screen_from == self.start_screen:
            self.player_name = self.start_screen.name_input.get(1.0, "end-1c")
            if self.player_name == '':
                self.player_name = 'PLAYER'
            self.player.name = self.player_name
        self.troll.health = 20
        self.player.health = 20
        self.after(100)
        screen_from.forget()
        self.after(100)
        self.game_screen = GameScreen(parent=self.container, controller=self)
        self.game_screen.grid(row=0, column=0, sticky="nsew")
        self.troll_hp_bar = HealthBar(self, self.game_screen, self.troll.name, 125, 435,value = self.troll.health, maximum=20, width=200, fg=self.LG_HEX)
        self.player_hp_bar = HealthBar(self,self.game_screen, self.player.name, 500, 460, value = self.player.health, maximum=20, width=200, align='right', fg=self.LB_HEX)
        self.troll_hp_bar.draw_background()
        self.player_hp_bar.draw_background()
        self.troll_hp_bar.draw_slider()
        self.player_hp_bar.draw_slider()
        self.troll.respond('begin', self.game_screen)
        print('start_trans finished')
    

    def transition_to_end(self, state):
        
        print('trans began')
        self.after(100)
        self.game_screen.forget()
        self.after(100)

        if state == 'win':
            print('win thread')
            self.win_screen = WinScreen(parent=self.container, controller=self)
            current_screen = self.win_screen
            text1 = f'{self.player.name}:'
            text2 = 'You Rolled'
            text3 = 'the Troll'
            color = self.LB_HEX
        elif state == 'lose':
            print('lose thread') 
            self.lose_screen = LoseScreen(parent=self.container, controller=self)
            current_screen =self.lose_screen
            text1 = f'{self.troll.name}:'
            text2 = 'You got Rolled'
            text3 = 'by the Troll'
            color = self.LG_HEX

        current_screen.grid(row=0, column=0, sticky="nsew")
        current_screen.create_text(400, 175, text=text1, fill=color, font=self.BUTTON_FONT) 
        self.end_typewriter = Typewriter(self, current_screen, 'text/end_message.txt', id='end', x=400, y=200, font='OCR A Extended', color=color)
        self.end_typewriter.write()
        current_screen.create_text(400, 500, text=text3, fill=self.LG_HEX, font=self.TITLE_FONT2) 
        current_screen.create_text(400, 425, text=text2, fill='#ffffff', font=self.TITLE_FONT1)
        current_screen.create_window(400, 600, width=200, height=40, window=current_screen.retry_button)
        current_screen.create_window(400, 650, width=200, height=40, window=current_screen.credits_button)
        print('trans ended')
    

    def roll_credits(self, screen_from):
        print('credits began')
        self.after(100)
        screen_from.forget()
        self.after(100)
        self.credits_screen = CreditScreen(parent=self.container, controller=self)
        self.credits_screen.grid(row=0, column=0, sticky="nsew")
        self.credits_screen.create_text(400, 175, text='Troll', fill=self.LG_HEX, font=self.TITLE_FONT2) 
        self.credits_screen.create_text(400, 100, text='Roll the', fill='#ffffff', font=self.TITLE_FONT1)
        self.credits_typewriter = Typewriter(self, self.credits_screen, 'text/credits.txt',id='credits', x=400, y=250, font='OCR A Extended', font_size=20 )
        self.credits_typewriter.write()
        print('credits end')

    

    def take_action(self, action,):
        #DISABLE BUTTONS
        self.game_screen.engage_button['state'] = 'disabled'
        self.game_screen.undermine_button['state'] = 'disabled'
        self.game_screen.ignore_button['state'] = 'disabled'
        self.game_screen.quit_button['state'] = 'disabled'
        self.game_screen.engage_button.update()
        self.game_screen.undermine_button.update()
        self.game_screen.ignore_button.update()
        self.game_screen.quit_button.update()
        
        #PLAYER RESPONDS
        self.player.respond(action, self.game_screen)
        
        #ROLL THE DICE AND DISPLAY
        td20 = self.troll_d20.draw_graphic(self.game_screen)
        td6 = self.troll_d6.draw_graphic(self.game_screen)
        pd20 = self.player_d20.draw_graphic(self.game_screen)
        pd6= self.player_d6.draw_graphic(self.game_screen)
        t_damage = 0
        p_damage = 0
    
        #CALCULATE RESULTS
        #if engage - troll +4 test, player gets -2 damage if lose
        if action == 'engage':
            td20 += 4
            if td6 < 2:
                td6 = 0
            else:
                td6 -= 2
        
        #if undermine - player + 3 test, troll gets -2 damage
        if action == 'undermine':
            pd20 += 3
            if pd6 < 2:
                pd6 = 0
            else:
                pd6 -= 2
        
        #if ignore - player get +5 test, player takes -1 damage
        if action == 'ignore':
            pd20 += 5
            p_damage += 1
        
        #compare rolls with buffs and debuffs
        if td20 >= pd20:
            p_damage += td6
        else:
            t_damage += pd6
        
        self.troll.health -= t_damage
        self.player.health -= p_damage
        print(f'player health: {self.player.health}')
        print(f'troll health: {self.troll.health}')
        

        #troll responds
        self.troll.respond(action, self.game_screen)

        #deal damage
        self.troll_hp_bar.update(self.troll.health, t_damage)
        self.player_hp_bar.update(self.player.health, p_damage)
        if t_damage == 0 and p_damage == 0:
            no_change_y = 445
            self.game_screen.create_text(400, no_change_y, text='NO DAMAGE', fill='#FFFF00', tag=f'no_change')
            for i in range(0,10):
                self.game_screen.delete(f'no_change')
                no_change_y +=1
                self.game_screen.create_text(400, no_change_y, text='NO DAMAGE', fill='#FFFF00', tag=f'no_change')
                self.update_idletasks()
                self.after(80)
            self.game_screen.delete(f'no_change')

        #clear player response
        self.player.forget(self.game_screen)

        #check for game status (win or lose)
        #win condition
        if self.troll.health <= 0 and self.player.health > self.troll.health:
            self.transition_to_end('win')
        #lose condition
        if self.player.health <= 0 and self.player.health < self.troll.health:
            self.transition_to_end('lose')
        
        #ENABLE BUTTONS
        self.game_screen.engage_button.update()
        self.game_screen.undermine_button.update()
        self.game_screen.ignore_button.update()
        self.game_screen.quit_button.update()
        self.game_screen.engage_button['state'] = 'normal'
        self.game_screen.undermine_button['state'] = 'normal'
        self.game_screen.ignore_button['state'] = 'normal'
        self.game_screen.quit_button['state'] = 'normal'

