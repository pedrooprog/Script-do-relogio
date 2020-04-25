from tkinter import *
import time

def times():
    relogio = time.strftime("%I:%M:%S:%P")
    clock_lbl = Label(janela, font = 'berlin 80', bg = 'black', fg = 'red', text = relogio)
    clock_lbl.after(200,times)
    clock_lbl.grid(row = 0, column = 1)


janela = Tk()
janela.title("relogio digital")
janela.resizable(False,False)
times()
janela.mainloop()
