# add in GUI calendar application
# being able to select a certain date
# a pop out on the date so that you can add events to it
# being able to save and load the same calendar each time the program runs
from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk

def Events():

    top = tk.Toplevel(root)

    cal = Calendar(top, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Meeting', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Homework Due', 'homework')

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Light Blue = Today\n Red = Homework \n Blue = Meeting").pack()

root = tk.Tk()
ttk.Button(root, text='Calendar with events', command=Events).pack(padx=10, pady=10)
root.mainloop()