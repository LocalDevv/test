# import datetime
# import time

# while True:
#     print(datetime.datetime.now().strftime("%H:%M:%S"))
#     time.sleep(1)

from tkinter import Tk, Label
import time

app = Tk()
app.title("DigiSTud Clock")
app.geometry("450x150")
app.resizable(1,1)

text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label = Label(app, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def digi_clock():
    cur_time = time.strftime("%H:%M:%S")
    label.config(text=cur_time)
    label.after(200, digi_clock)

digi_clock()
app.mainloop()