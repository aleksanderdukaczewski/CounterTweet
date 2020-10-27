import datetime
from tkcalendar import *
from tkinter import *

today = datetime.date.today()

root = Tk()

cal = DateEntry(root, width=12, background='darkblue',
                    foreground='white', borderwidth=2)

print(cal.get_date())

cal.pack()

root.mainloop()