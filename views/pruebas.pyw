from tkinter import *

# RAIZ DEL GUI
root = Tk()
root.title('Pruebas con la libreria Tkinter')
root.resizable(False,False)
#root.iconbitmap('iconoParaLaVentana.icon')
#La root se tiene que adaptar al contenedor del frame
#root.geometry('600x400')
#root.config(bg='blue')

# FRAME
frame = Frame(root, width=500, height=300)
frame.pack()

# LABEL
Label(frame, text='Ingrese su nombre:').place(x=30,y=100)

# INPUT
Entry(frame).place(x=30,y=120)

# Mostrar GUI
root.mainloop()