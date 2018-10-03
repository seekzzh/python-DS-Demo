import tkinter as tk

window = tk.Tk()
window.title = "My window"
window.geometry('200x200')

lb = tk.Label(window, text='', bg='#4285f4')
lb.pack()

counter = 0


def do_job():
    global counter
    lb.config(text='do'+str(counter))
    counter += 1


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=do_job)
filemenu.add_command(label="Open", command=do_job)
filemenu.add_separator
filemenu.add_command(labe="Exit", command=window.quit)

window.config(menu=menubar)

window.mainloop()
