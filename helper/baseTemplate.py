from tkinter import *
from tkinter import ttk

#setup
window = Tk()
window.title('My App | a Level2Learn.com App')
window.iconbitmap('images/l2l_icon.ico')
window.geometry('800x800')

#content
main_frame = ttk.Frame(window, padding=10).grid()
hello_txt = ttk.Label(main_frame, text="Hello World!").grid(column=0, row=0)

if __name__ == "__main__":
    window.mainloop()