from tkinter import *

# RAIZ DEL GUI
root = Tk()
root.title('Registrarse')
root.resizable(False,False)

# FRAME
frame = Frame(root)
frame.pack()
frame.config(padx=20, pady=20)

# SECTION NOMBRE
lblNombre = Label(frame, text='Nombre:').grid(row=0, column=0, pady=5, padx=5, sticky=E)
inputNombre = Entry(frame)
inputNombre.grid(row=0, column=1, pady=5, padx=5)
inputNombre.config(justify='center')

# SECTION PRECIO
lblPrecio = Label(frame, text='Precio:').grid(row=1, column=0, pady=5, padx=5, sticky=E)
inputPrecio = Entry(frame)
inputPrecio.grid(row=1, column=1, pady=5, padx=5)
inputPrecio.config(justify='center')

# SECTION DESCRIPCION
lblDescripcion = Label(frame, text='Descripcion:').grid(row=2, column=0, pady=5, padx=5, sticky=NE)
txtAreaDescripcion = Text(frame,height=5, width=15)
txtAreaDescripcion.grid(row=2, column=1, pady=5, padx=5, sticky=E)
scrollVertical = Scrollbar(frame, command=txtAreaDescripcion.yview) #Scroll para la descripcion
scrollVertical.grid(row=2, column=2, sticky='nsew') #nsew => Adapta al alto del textArea
txtAreaDescripcion.config(yscrollcommand=scrollVertical.set) 



# Mostrar GUI
root.mainloop()