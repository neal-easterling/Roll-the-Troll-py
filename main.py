from game.game import GameApp

#CONSTANTS
APP_WIDTH = 800
APP_HEIGHT = 800
APP_TITLE = 'Level2Learn.com | Roll the Troll'

#WINDOW SETUP
app = GameApp()
app.title(APP_TITLE)
app.iconbitmap('images/l2l_icon.ico')

#center window calcs and window size
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app_x = int(screen_width/2)-int(APP_WIDTH/2)
app_y = int(screen_height/2) - int(APP_HEIGHT/2)

app.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{app_x}+{app_y}')



if __name__ == "__main__":
    app.mainloop()