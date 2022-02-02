import random
from helper.color_shift import color_shift
from helper.draw import round_rectangle
import tkinter as tk
from tkinter.font import Font

class d6():
    def __init__(self, id, app, x_center, y_center, height=50, fg='#ffffff') -> None:
        self.num = self.roll('num')
        self.id = id
        self.app = app
        self.x_center = x_center
        self.y_center = y_center
        self.height = height
        self.offset = int(self.height/2)
        self.fg = fg
        self.dot_fill = '#333333'
        #BACKGROUND CALCS
        self.x1 = self.x_center - self.offset
        self.y1 = self.y_center - self.offset
        self.x2 = self.x_center + self.offset
        self.y2 = self.y_center + self.offset
        #DOT CALCS
        self.dot_size = int(self.height/6)  
        #columns
        self.left_col_x1 = self.x_center - int(self.dot_size/2) - int(self.dot_size * 2)
        self.left_col_x2 = self.left_col_x1 + self.dot_size
        self.center_col_x1 = self.x_center - int(self.dot_size/2)
        self.center_col_x2 = self.x_center + int(self.dot_size/2)
        self.right_col_x2 = self.x_center + int(self.dot_size/2) + int(self.dot_size * 2)
        self.right_col_x1 = self.right_col_x2 - self.dot_size 
        #rows
        self.top_row_y1 = y_center - int(self.dot_size/2) - int(self.dot_size * 2)
        self.top_row_y2 = self.top_row_y1 + self.dot_size
        self.center_row_y1 = self.y_center - int(self.dot_size/2)
        self.center_row_y2 = self.y_center + int(self.dot_size/2)
        self.bottom_row_y2 = self.y_center + int(self.dot_size/2) + int(self.dot_size * 2)
        self.bottom_row_y1 = self.bottom_row_y2 - self.dot_size
    

    def roll(self, type):
        i = random.randint(1,6)
        if type == 'str':
            num = str(i)
        else:
            num = i
        return num
    

    def draw_graphic(self, canvas, ):
        
        
        #CREATE BACKGROUND
        round_rectangle(canvas, self.x1, self.y1, self.x2, self.y2, radius=10, fill=self.fg, width=0)

        #CREATE DOTS
        self.num = self.roll('num')
        print(self.id + ': '  + str(self.num))
        if self.num == 1:
            #center dot
            canvas.create_oval(self.center_col_x1, self.center_row_y1, self.center_col_x2, self.center_row_y2, fill=self.dot_fill, width=0)

        elif self.num == 2:
            #bottom left dot
            canvas.create_oval(self.left_col_x1, self.bottom_row_y1, self.left_col_x2, self.bottom_row_y2, fill=self.dot_fill, width=0)
            #top right dot
            canvas.create_oval(self.right_col_x1, self.top_row_y1, self.right_col_x2, self.top_row_y2, fill=self.dot_fill, width=0)
            
        elif self.num == 3:
            #bottom left dot
            canvas.create_oval(self.left_col_x1, self.bottom_row_y1, self.left_col_x2, self.bottom_row_y2, fill=self.dot_fill, width=0)
            #center dot
            canvas.create_oval(self.center_col_x1, self.center_row_y1, self.center_col_x2, self.center_row_y2, fill=self.dot_fill, width=0)
            #top right dot
            canvas.create_oval(self.right_col_x1, self.top_row_y1, self.right_col_x2, self.top_row_y2, fill=self.dot_fill, width=0)

        elif self.num == 4:
            # top left dot
            canvas.create_oval(self.left_col_x1, self.top_row_y1, self.left_col_x2, self.top_row_y2, fill=self.dot_fill, width=0)
            # bottom left dot
            canvas.create_oval(self.left_col_x1, self.bottom_row_y1, self.left_col_x2, self.bottom_row_y2, fill=self.dot_fill, width=0)
            # top right dot
            canvas.create_oval(self.right_col_x1, self.top_row_y1, self.right_col_x2, self.top_row_y2, fill=self.dot_fill, width=0)
            # bottom right dot
            canvas.create_oval(self.right_col_x1, self.bottom_row_y1, self.right_col_x2, self.bottom_row_y2, fill=self.dot_fill, width=0)

        elif self.num == 5:
            # top left dot
            canvas.create_oval(self.left_col_x1, self.top_row_y1, self.left_col_x2, self.top_row_y2, fill=self.dot_fill, width=0)
            # bottom left dot
            canvas.create_oval(self.left_col_x1, self.bottom_row_y1, self.left_col_x2, self.bottom_row_y2, fill=self.dot_fill, width=0)
            #center dot
            canvas.create_oval(self.center_col_x1, self.center_row_y1, self.center_col_x2, self.center_row_y2, fill=self.dot_fill, width=0)
            # top right dot
            canvas.create_oval(self.right_col_x1, self.top_row_y1, self.right_col_x2, self.top_row_y2, fill=self.dot_fill, width=0)
            # bottom right dot
            canvas.create_oval(self.right_col_x1, self.bottom_row_y1, self.right_col_x2, self.bottom_row_y2, fill=self.dot_fill, width=0)
        else:
            # top left dot
            canvas.create_oval(self.left_col_x1, self.top_row_y1, self.left_col_x2, self.top_row_y2, fill=self.dot_fill, width=0)
            #center left dot
            canvas.create_oval(self.left_col_x1, self.center_row_y1, self.left_col_x2, self.center_row_y2, fill=self.dot_fill, width=0)
            # bottom left dot
            canvas.create_oval(self.left_col_x1, self.bottom_row_y1, self.left_col_x2, self.bottom_row_y2, fill=self.dot_fill, width=0)
            # top right dot
            canvas.create_oval(self.right_col_x1, self.top_row_y1, self.right_col_x2, self.top_row_y2, fill=self.dot_fill, width=0)
            #cemter right dot
            canvas.create_oval(self.right_col_x1, self.center_row_y1, self.right_col_x2, self.center_row_y2, fill=self.dot_fill, width=0)
            # bottom right dot
            canvas.create_oval(self.right_col_x1, self.bottom_row_y1, self.right_col_x2, self.bottom_row_y2, fill=self.dot_fill, width=0)

        return self.num



class d20():

    def __init__(self, id, app, x_center, y_center, height=80, fg='#ffffff', font='Arial') -> None:
        self.num = self.roll('num')
        self.id = id
        self.num_color = '#333333'
        self.app = app
        self.x_center = x_center
        self.y_center = y_center
        self.height = height
        self.fg = fg
        self.font = Font(family=font, weight='bold')


    def roll(self, type):
        i = random.randint(1,20)
        if type == 'str':
            num = str(i)
        else:
            num = i
        return num
        

    def draw_graphic(self, canvas):
        self.font.size=int(self.height/6)
        #COLOR VARIANTS FOR SHADING
        c1=self.fg
        c2=color_shift(self.fg, -50)
        c3=color_shift(self.fg, -100)
        c4= color_shift(self.fg, -125)

        #MEASUREMENTS AND EDGES
        width = int((self.height/6) * 5)
        trig_diam = int((width/5 )* 3)     
        top_x = self.x_center
        bottom_x = self.x_center
        right_x = self.x_center + int(width/2)
        left_x = self.x_center - int(width/2)
        top_y = self.y_center - int(self.height/2)
        upper_y = self.y_center - int(self.height/4)
        lower_y = self.y_center + int(self.height/4)
        bottom_y = self.y_center + int(self.height/2)
        tri_r_x = self.x_center + int(trig_diam/2)
        tri_l_x = self.x_center - int(trig_diam/2)
   
        #DRAW BG POLYGON
        d20_bg_points =[
            top_x, top_y,       #top
            right_x, upper_y,   #top right
            right_x, lower_y,   #bottom right
            bottom_x, bottom_y, #bottom
            left_x, lower_y,    #bottom left
            left_x, upper_y     #top left
            ]
        canvas.create_polygon(d20_bg_points, fill=c3, outline=c3)

        #DRAW BOTTOM SHADED TRIANGLE
        d20_bottom_points =[
            right_x, lower_y,   #bottom right
            bottom_x, bottom_y, #bottom
            left_x, lower_y     #bottom left
            ]
        canvas.create_polygon(d20_bottom_points, fill=c4, outline=c4)

        #DRAW BOTTOM BRIGHTER TRIANGLE
        d20_bottom_tri_points =[
            tri_r_x, lower_y,   #center right
            bottom_x, bottom_y, #bottom
            tri_l_x, lower_y    #center left
            ]
        canvas.create_polygon(d20_bottom_tri_points, fill=c3, outline=c3)

        #DRAW CENTER MID COLOR TRIANGLES WITH POLYGON
        d20_mid_points=[
            right_x, upper_y, #top right
            tri_r_x, lower_y, #center right
            tri_l_x, lower_y, #center left
            left_x, upper_y   #top left
            ]
        canvas.create_polygon(d20_mid_points, fill=c2, outline=c2)

        #DRAW CENTER TRIANGLE
        ftrig_points = [
            #triangle
            top_x, upper_y,   #center top
            tri_r_x, lower_y, #center right
            tri_l_x, lower_y  #center left
            ]
        canvas.create_polygon(ftrig_points, fill=c1, outline=c1)

        #ADD TEXT NUMBER
        self.num = self.roll('num')
        print(self.id + ': ' + str(self.num))
        canvas.create_text(self.x_center, self.y_center + int(self.height/10), fill=self.num_color, text=str(self.num), font=self.font)
        
        return self.num