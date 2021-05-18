from tkinter import *

# RAIZ DEL GUI
root = Tk()
root.title('Registrarse')
root.resizable(False,False)

# FRAME
frame = Frame(root)
frame.pack()
frame.config(padx=20, pady=20)

# SECTION DNI
lblDNI = Label(frame, text='DNI:').grid(row=0, column=0, pady=5, padx=5, sticky=E)
inputDNI = Entry(frame)
inputDNI.grid(row=0, column=1, pady=5, padx=5)
inputDNI.config(justify='center')

# SECTION NOMBRE
lblNombre = Label(frame, text='Nombre:').grid(row=1, column=0, pady=5, padx=5, sticky=E)
inputNombre = Entry(frame)
inputNombre.grid(row=1, column=1, pady=5, padx=5)
inputNombre.config(justify='center')

# SECTION EMAIL
lblEmail = Label(frame, text='Email:').grid(row=2, column=0, pady=5, padx=5, sticky=E)
inputEmail = Entry(frame)
inputEmail.grid(row=2, column=1, pady=5, padx=5)
inputEmail.config(justify='center')

# SECTION CLAVE
lblContrasenia = Label(frame, text='Contraseña:').grid(row=3, column=0, pady=5, padx=5, sticky=E)
inputContrasenia = Entry(frame)
inputContrasenia.grid(row=3, column=1, pady=5, padx=5)
inputContrasenia.config(justify='center', show='*')

# SECTION CIUDAD
lblCiudad = Label(frame, text='Ciudad:').grid(row=4, column=0, pady=5, padx=5, sticky=E)
inputCiudad = Entry(frame)
inputCiudad.grid(row=4, column=1, pady=5, padx=5)
inputCiudad.config(justify='center')

# BUTTON REGISTRARSE
btnRegistrarse = Button(frame, text='Registrarse')
btnRegistrarse.grid(row=5, column=0, columnspan=2)

# Mostrar GUI
root.mainloop()