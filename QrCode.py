from tkinter import *
import pyqrcode as pqr
import png
import io

code = pqr.create('https://www.youtube.com/')

w = Tk()
w.title('QRCode')

code_aux = code.xbm(scale=5)
code_bpm = BitmapImage(data = code_aux)
code_bpm.config(foreground = 'black', background = 'white')
labelQr = Label(image=code_bpm)
labelQr.pack()
w.mainloop()