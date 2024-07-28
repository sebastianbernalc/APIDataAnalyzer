from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import time

class SplashScreen:
    def __init__(self):
        self.root = Tk()
        self.width_of_window = 460
        self.height_of_window = 250
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2) - (self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2) - (self.height_of_window/2)
        self.root.geometry("%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.root.overrideredirect(1)  # For hiding titlebar

        self.setup_ui()
        self.root.mainloop()

    def setup_ui(self):
        Frame(self.root, width=427, height=250, bg='#272727').place(x=0, y=0)
        label1 = Label(self.root, text='Currency Exchanges', fg='white', bg='#272727')  # Decorate it
        label1.configure(font=("REFOLTER", 18, "bold"))  # You need to install this font in your PC or try another one
        label1.place(x=80, y=90)

        label2 = Label(self.root, text='Banco Central Europeo...', fg='white', bg='#272727')  # Decorate it
        label2.configure(font=("REFOLTER", 9))
        label2.place(x=10, y=215)

        # Making animation
        image_a = ImageTk.PhotoImage(Image.open('./Images/c2.png'))
        image_b = ImageTk.PhotoImage(Image.open('./Images/c1.png'))

        for i in range(3):  # 5 loops
            self.animate(image_a, image_b)

        self.root.destroy()


    def animate(self, image_a, image_b):
        l1 = Label(self.root, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
        l2 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        self.root.update_idletasks()
        time.sleep(0.5)

        l1 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2 = Label(self.root, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
        l3 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        self.root.update_idletasks()
        time.sleep(0.5)

        l1 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3 = Label(self.root, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
        l4 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        self.root.update_idletasks()
        time.sleep(0.5)

        l1 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3 = Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4 = Label(self.root, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
        self.root.update_idletasks()
        time.sleep(0.5)


