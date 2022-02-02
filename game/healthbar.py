from pyglet import font
from helper.draw import round_rectangle
from helper.color_shift import color_shift

class HealthBar():

    def __init__(self, app, canvas, name, x1, y1, value = 10, maximum=20, width= 100, height= 25, margin=3, align='left', 
                fg='#00FF00', bg='#333333', warn='#FFFF00', danger='#FF0000', font='Arial' ) -> None:

        font.add_file('fonts/ARIAL.TTF')
        
        #SELECTED ATTRIBUTES
        self.app = app
        self.canvas = canvas
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.margin = margin
        self.value = value
        self.maximum = maximum
        self.align = align

        #COLOR ATTRIBUTES
        self.fg = fg
        self.bg = bg
        self.fill = self.fg
        self.warn = warn
        self.danger = danger
        self.text_readout_fill= color_shift(self.fg, -100)

        #CALC ATTRIBUTES
        self.unit = int(self.width/self.maximum)
        self.percentage = self.value/self.maximum 
        self.bg_x2 = self.x1 + self.width
        self.bg_y2 = self.y1 + self.height
        self.bg_radius = int(self.height/4)
        self.fg_radius = int(self.height/5)
        self.fg_x1 = self.x1 + self.margin
        self.fg_y1 = self.y1 + self.margin
        self.fg_x2 = self.x1 + (self.value * self.unit) - self.margin
        self.fg_y2 = self.y1 + self.height - self.margin

        #FONT ATTRIBUTES
        self.internal_font_size = self.height - (self.margin*4)
        self.internal_font = font.load(name=font, size = self.internal_font_size)
        self.name_label_font = font.load(name=font, size=15)

        #CREATE BG & Label
        if self.align == 'right':
            self.label_x = self.bg_x2
            self.label_anchor = 'se'
        else:
            self.label_x = self.x1
            self.label_anchor = 'sw'


    def draw_background(self):

        self.name_label = self.canvas.create_text(self.label_x, self.y1,text=self.name, fill=self.fg, font=self.name_label_font, anchor=self.label_anchor)
        self.bg_rect = round_rectangle(self.canvas, self.x1, self.y1, self.bg_x2, self.bg_y2, radius=self.bg_radius, fill=self.bg, outline=self.fg, width=1)
        

    def draw_slider(self, value='please_use_int'):
        if value != 'please_use_int':
            self.value = value
            self.percentage = self.value/self.maximum  
        #RESET MEASUREMENTS TO ALIGN FG RIGHT
        if self.align == 'right':
            self.fg_x2 = self.x1 + self.width - self.margin
            self.fg_y2 = self.y1 + self.height - self.margin
            self.fg_x1 = self.fg_x2 - (self.value * self.unit) + self.margin * 2
            self.fg_y1 = self.y1 + self.margin
            self.text_readout_x = self.x1 + self.margin * 3
            self.text_readout_anchor = 'sw'
        else:
            self.fg_x1 = self.x1 + self.margin
            self.fg_y1 = self.y1 + self.margin
            self.fg_x2 = self.x1 + (self.value * self.unit) - self.margin
            self.fg_y2 = self.y1 + self.height - self.margin
            self.text_readout_x = self.bg_x2 - self.margin * 3
            self.text_readout_anchor = 'se'

        # CHANGE FILL TO WARN COLOR IF BELOW 50% AND ABOVE 25%
        if self.percentage <= 0.5 and self.percentage > 0.25:
            self.fill = self.warn
            self.text_readout_fill=self.warn
        #CHANGE FILL TO DANGER COLOR IF BELOW 25%
        if self.percentage <= 0.25:
            self.fill = self.danger
            self.text_readout_fill=self.danger
        #SET TEXT
        self.text_readout = f'{self.value}/{self.maximum}'

            
        #CREATE FG    
        self.fg_rect = round_rectangle(self.canvas, self.fg_x1, self.fg_y1, self.fg_x2, self.fg_y2, radius=self.fg_radius, tag=f'{self.name}_hp_slider', fill=self.fill, width=0)

        #CREATE TEXT
        self.canvas.create_text(self.text_readout_x, self.fg_y2, text=self.text_readout, font=self.internal_font, 
                                fill=self.text_readout_fill, anchor=self.text_readout_anchor, tag=f'{self.name}_text_readout')
    
    def update(self, value, change):
        if change == 0:
            pass
        elif value < 0:
            value = 0 
        else:
            self.canvas.delete(f'{self.name}_hp_slider')
            self.canvas.delete(f'{self.name}_text_readout')
            self.draw_slider(value)
            self.text_readout = f'{value}/{self.maximum}'
            self.canvas.create_text(self.text_readout_x, self.fg_y2, text=self.text_readout, font=self.internal_font, 
                                    fill=self.text_readout_fill, anchor=self.text_readout_anchor, tag=f'{self.name}_text_readout')
            if self.align == 'right':
                x1x = self.x1 - 15      
            else:
                x1x= self.bg_x2 + 15
            y1y = self.fg_y2
            self.canvas.create_text(x1x, y1y, text=f'-{change}', fill=self.danger, tag=f'debuff_{self.name}')
            for i in range(0,10):
                self.canvas.delete(f'debuff_{self.name}')
                y1y +=1
                self.canvas.create_text(x1x, y1y, text=f'-{change}', fill=self.danger, tag=f'debuff_{self.name}')
                self.app.update_idletasks()
                self.app.after(80)
            self.canvas.delete(f'debuff_{self.name}')
