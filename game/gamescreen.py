from tkinter import Canvas, Button, PhotoImage
from helper.draw import round_rectangle
from helper.readfile import read_file

class GameScreen(Canvas):

    def __init__(self, parent, controller, *args, **kwargs):
        Canvas.__init__(self, parent, bd=0,bg=controller.BG_HEX, width=800, height=800, *args, **kwargs)
        

        #DRAW THE MAIN GAME BACKGROUND OF ROLL THE TROLL
        #bg frame
        round_rectangle(self, 25, 50, 750, 725, fill=controller.BG_HEX, outline=controller.YEL_HEX, width=4)
        #title
        self.create_rectangle(525, 45, 700, 55, fill=controller.BG_HEX, width=0)
        self.create_text(600, 125, text='Troll', fill=controller.LG_HEX, font=controller.TITLE_FONT2) 
        self.create_text(600, 50, text='Roll the', fill='#ffffff', font=controller.TITLE_FONT1) 
        #instructions
        self.instruction_txt = read_file('text/instructions.txt')
        self.create_text(500, 175, text=self.instruction_txt, fill='#ffffff', font=controller.INSTRUCTION_FONT, anchor='nw')
        # troll face 
        self.troll_face_png = PhotoImage(file='images/TrollFace.png')
        self.create_image(15, 20, image=self.troll_face_png, anchor='nw')
        # troll_response_box  
        round_rectangle(self, 100, 300, 400, 400, fill=controller.DG_HEX, outline=controller.LG_HEX, width=3)
        #player_response_box
        round_rectangle(self, 425, 325, 725, 425, fill=controller.DB_HEX, outline=controller.LB_HEX, width=3)
        self.create_text(425, 325, width=200, fill=controller.LG_HEX, anchor='nw', tag='player_txt')    
        #player_GUI_Box
        round_rectangle(self, 50, 625, 775, 775, fill=controller.DB_HEX, outline=controller.LB_HEX, width=3)

        self.grid(row=0, column=0, sticky="nsew")

        # DISPLAY DICE
        controller.troll_d20.draw_graphic(self)
        controller.troll_d6.draw_graphic(self)
        controller.player_d20.draw_graphic(self)
        controller.player_d6.draw_graphic(self)
        

        #CREATE BUTTONS
        self.engage_button = Button(self, text ='Engage', command = lambda: controller.take_action('engage')  ,
                                    font=controller.BUTTON_FONT, 
                                    fg=controller.BUTTON_TEXT_COLOR, 
                                    bg=controller.BUTTON_BG, 	
                                    activebackground=controller.DB_HEX,
                                    activeforeground=controller.LB_HEX
                                    )
        self.undermine_button = Button(self, text='Undermine', command = lambda: controller.take_action('undermine')  ,
                                        font=controller.BUTTON_FONT, 
                                        fg=controller.BUTTON_TEXT_COLOR, 
                                        bg=controller.BUTTON_BG, 	
                                        activebackground=controller.DB_HEX,
                                        activeforeground=controller.LB_HEX
                                        )
        self.ignore_button = Button(self, text='Ignore', command = lambda: controller.take_action('ignore') ,
                                    font=controller.BUTTON_FONT, 
                                    fg=controller.BUTTON_TEXT_COLOR, 
                                    bg=controller.BUTTON_BG, 	
                                    activebackground=controller.DB_HEX,
                                    activeforeground=controller.LB_HEX
                                    )
        self.quit_button = Button(self, text='Roll Over', command = lambda: controller.transition_to_end('lose')  ,
                                    font=controller.BUTTON_FONT, 
                                    fg=controller.BUTTON_TEXT_COLOR, 
                                    bg=controller.QUIT_COLOR, 	
                                    activebackground=controller.DG_HEX,
                                    activeforeground=controller.LG_HEX
                                    )
                                    
        #DISPLAY BUTTONS
        self.create_window(175, 680, width=200, height=40, window=self.engage_button)
        self.create_window(400, 680, width=200, height=40, window=self.undermine_button)
        self.create_window(625, 680, width=200, height=40, window=self.ignore_button)
        self.create_window(400, 740, width=200, height=40, window=self.quit_button)

        
        


        #controller.troll.respond('begin', controller, self, 425, 215, width=200,  anchor='nw')
        

        