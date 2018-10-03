import tkinter as tk

window = tk.Tk()
window.title('Label & Button')
window.geometry('200x100')

var = tk.StringVar()
lb = tk.Label(window,
              textvariable=var,
              bg='#4285f4',
              font=('Arial', 12),
              width=15, height=2
              )
lb.pack()


on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you press me')
    else:
        on_hit = False
        var.set('')


btn = tk.Button(window,
                text="press me",
                width=15, height=2,
                command=hit_me
                )
btn.pack()

window.mainloop()
