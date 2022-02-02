from pyglet import font
import random


class Responder():
    def __init__(self, actor, health, app, x, y, width=275) -> None:
        self.health = health
        self.name = actor.upper()
        self.font = font.load(name='OCR A Extended', size = 12)
        self.app = app
        self.x = x
        self.y = y
        self.width = width

        if actor == 'troll':
            self.id='troll_txt'
            self.color = app.LG_HEX
            self.begin_list = self.get_txt_as_list('text/troll_begin.txt')
            self.eng_list = self.get_txt_as_list('text/troll_eng.txt')
            self.und_list = self.get_txt_as_list('text/troll_und.txt')
            self.ign_list = self.get_txt_as_list('text/troll_ign.txt')
        else:
            self.id='player_txt'
            self.color = app.LB_HEX
            self.eng_list = self.get_txt_as_list('text/player_eng.txt')
            self.und_list = self.get_txt_as_list('text/player_und.txt')
            self.ign_list = self.get_txt_as_list('text/player_ign.txt')
        
        
    def get_txt_as_list(self, path):
        list = []
        with open(path, 'r') as file:
            filecontents = file.readlines()
            
            for line in filecontents:
                current_place = line[:-1]
                list.append(current_place)
        file.close()    
        return list


    def response(self, action):
        if action == 'begin':
            i = random.randint(0, len(self.begin_list)-1)
            return self.begin_list[i]
        elif action == 'engage':
            i = random.randint(0, len(self.eng_list)-1)
            return self.eng_list[i]
        elif action == 'undermine':
            i = random.randint(0, len(self.und_list)-1)
            return self.und_list[i]
        else:
            i = random.randint(0, len(self.ign_list)-1)
            return self.ign_list[i]
    

    def respond(self, action, canvas, **kwargs):
        if action == 'begin':
            i = random.randint(0, len(self.begin_list)-1)
            response = self.begin_list[i]
        elif action == 'engage':
            i = random.randint(0, len(self.eng_list)-1)
            response = self.eng_list[i]
        elif action == 'undermine':
            i = random.randint(0, len(self.und_list)-1)
            response = self.und_list[i]
        else:
            i = random.randint(0, len(self.ign_list)-1)
            response = self.ign_list[i]
        
        message = ''
        for char in response:
            canvas.delete(self.id)
            message += char
            canvas.create_text( self.x, self.y, text = message, font=self.font, tag=self.id, fill=self.color, width=self.width, anchor='nw', **kwargs)
            self.app.update_idletasks()
            self.app.after(120)


    def forget(self, canvas):
        canvas.delete(self.id)
        self.app.update_idletasks()        
            