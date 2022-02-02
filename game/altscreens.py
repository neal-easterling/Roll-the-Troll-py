from tkinter import Canvas, Button, Text

class StartScreen(Canvas):

    def __init__(self, parent, controller):
        Canvas.__init__(self, parent, bd=0,bg=controller.BG_HEX, width=800, height=800)
        self.create_text(400, 375, text='Troll', fill=controller.LG_HEX, font=controller.TITLE_FONT2) 
        self.create_text(400, 300, text='Roll the', fill='#ffffff', font=controller.TITLE_FONT1)
        self.create_text(400, 460, text='Your name, challenger?', fill=controller.LG_HEX, font=controller.BUTTON_FONT)
        self.name_input = Text(self, width=200, height = 30)
        self.start_button = Button(self, text='Start', command=lambda: controller.start_trans(controller.start_screen), 
                                font=controller.BUTTON_FONT, 
                                fg=controller.DG_HEX, 
                                bg=controller.LG_HEX,
                                activebackground=controller.DG_HEX,
                                activeforeground=controller.LG_HEX
                            )
        self.create_window(400, 500, width=200, height=30, window=self.name_input)
        self.create_window(400, 550, width=200, height=50, window=self.start_button)
        self.grid(row=0, column=0, sticky="nsew")


class WinScreen(Canvas):

    def __init__(self, parent, controller):
        Canvas.__init__(self, parent, bd=0,bg=controller.BG_HEX, width=800, height=800)
        self.grid(row=0, column=0, sticky="nsew")
        
        self.retry_button = Button(self, text='Try Again?', command=lambda: controller.start_trans(controller.win_screen), 
                                font=controller.BUTTON_FONT, 
                                fg=controller.DG_HEX, 
                                bg=controller.LG_HEX,
                                activebackground=controller.DG_HEX,
                                activeforeground=controller.LG_HEX
                            )
        self.credits_button = Button(self, text='Roll Credits', command=lambda: controller.roll_credits(controller.win_screen), 
                                font=controller.BUTTON_FONT, 
                                fg=controller.DG_HEX, 
                                bg=controller.LG_HEX,
                                activebackground=controller.DG_HEX,
                                activeforeground=controller.LG_HEX
                            )


class LoseScreen(Canvas):

    def __init__(self, parent, controller):
        Canvas.__init__(self, parent, bd=0,bg=controller.BG_HEX, width=800, height=800)
        self.grid(row=0, column=0, sticky="nsew")

        self.retry_button = Button(self, text='Try Again?', command=lambda: controller.start_trans(controller.lose_screen), 
                                font=controller.BUTTON_FONT, 
                                fg=controller.DG_HEX, 
                                bg=controller.LG_HEX,
                                activebackground=controller.DG_HEX,
                                activeforeground=controller.LG_HEX
                            )
        self.credits_button = Button(self, text='Roll Credits', command=lambda: controller.roll_credits(controller.lose_screen), 
                                font=controller.BUTTON_FONT, 
                                fg=controller.DG_HEX, 
                                bg=controller.LG_HEX,
                                activebackground=controller.DG_HEX,
                                activeforeground=controller.LG_HEX
                            )


class CreditScreen(Canvas):

    def __init__(self, parent, controller):
        Canvas.__init__(self, parent, bd=0,bg=controller.BG_HEX, width=800, height=800)
        self.grid(row=0, column=0, sticky="nsew")
        
        
        


        

        