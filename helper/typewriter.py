import tkinter as tk
from tkinter.font import Font

class Typewriter():

    def __init__(self, app, canvas, file_path, id='typewriter', x=0, y=0, font='Arial', font_size = 15, color='#ffffff', *args, **kwargs) -> None:
        self.app = app
        self.canvas = canvas
        self.file_path = file_path
        self.id = id
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color=color
        self.font = Font(family = font, size=self.font_size)
        self.line_spacing = int(font_size/5)
        self.text = self.get_txt_as_list(file_path)


    def get_txt_as_list(self, path):
        list = []
        with open(path, 'r') as file:
            filecontents = file.readlines()
            
            for line in filecontents:
                current_place = line[:-1]
                list.append(current_place)
                
        return list
    
    def write(self, text_as_list=['empty'], **kwargs):
        message=''
        s = 0
        if text_as_list[0]=='empty':
            text_to_write = self.text
        else:
            text_to_write = text_as_list
        
        for line in text_to_write:
            for char in line:
                self.canvas.delete(f'{self.id}{s}')
                message += char
                self.canvas.create_text(self.x, self.y + s, text = message, tag=f'{self.id}{s}', font=self.font, fill=self.color,  **kwargs)
                self.app.update_idletasks()
                self.app.after(120)
            
            s += self.line_spacing + self.font_size
            message = ''


