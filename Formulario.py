#Crhistopher Isram Mancilla Laure
#Mayo 2023

from tkinter import *
from tkinter import ttk
import csv
import sqlite3

raiz = Tk()
raiz.title("Formulario")
#raiz2 = Tk()
#raiz2.title("DatosFormulario")

mainFrame = ttk.Frame(raiz, padding = "15 15 15 15")
mainFrame.grid(column= 0, row=0)
secondFrame = ttk.Frame(mainFrame, padding = "10 10 10 10", relief="raised")
secondFrame.grid(column=1, row = 1)
ttk.Label(mainFrame, text= "").grid(column=1, row=2)
thridFrame = ttk.Frame(mainFrame, padding = "8 8 8 8", relief="raised")
thridFrame.grid(column=1, row=3)
ttk.Label(mainFrame, text= "").grid(column=1, row=4)
fourthFrame = ttk.Frame(mainFrame, padding= "15 15 15 15")
fourthFrame.grid(column=2, row=1)
fifthFrame = ttk.Frame(mainFrame, padding= "7 7 7 7")
fifthFrame.grid(column=1, row=5)
sixthFrame = ttk.Frame(mainFrame, padding="10 10 10 10")
sixthFrame.grid(column=2, row=1)
eighthFrame = ttk.Frame(mainFrame, padding="15 15 15 15")
eighthFrame.grid(column=2, row=5)

#secondFrame
nombre = StringVar()
aPaterno = StringVar()
aMaterno = StringVar()
correo = StringVar()
movil = StringVar()

ttk.Label(secondFrame, text= "Nombre:").grid(column=1, row=1, sticky=(E))
ttk.Label(secondFrame, text= "").grid(column=1, row=2)
ttk.Label(secondFrame, text= "A Paterno:").grid(column=1, row=3, sticky=(E))
ttk.Label(secondFrame, text= "").grid(column=1, row=4)
ttk.Label(secondFrame, text= "A Materno:").grid(column=1, row=5, sticky=(E))
ttk.Label(secondFrame, text= "").grid(column=1, row=6)
ttk.Label(secondFrame, text= "Correo:").grid(column=1, row=7, sticky=(E))
ttk.Label(secondFrame, text= "").grid(column=1, row=8)
ttk.Label(secondFrame, text= "Móvil:").grid(column=1, row=9, sticky=(E))
ttk.Label(secondFrame, text= "    ").grid(column=2, row=1)

nombreEntry = ttk.Entry(secondFrame, width = 30, textvariable=nombre)
nombreEntry.grid(column=3, row=1)
aPaternoEntry = ttk.Entry(secondFrame, width = 30, textvariable=aPaterno)
aPaternoEntry.grid(column=3, row=3)
aMaternoEntry = ttk.Entry(secondFrame, width = 30, textvariable=aMaterno)
aMaternoEntry.grid(column=3, row=5)
correoEntry = ttk.Entry(secondFrame, width = 30, textvariable=correo)
correoEntry.grid(column=3, row=7)
movilEntry = ttk.Entry(secondFrame, width = 30, textvariable=movil)
movilEntry.grid(column=3, row=9)

#thirdFrame
aficiones1 = StringVar()
aficiones2 = StringVar()
aficiones3 = StringVar()
ttk.Label(thridFrame, text= "Aficiones:").grid(column=1, row=1)
leer = ttk.Checkbutton(thridFrame, text="Leer      ", variable=aficiones1).grid(column=1, row=2)
musica = ttk.Checkbutton(thridFrame, text="Música      ",variable=aficiones2).grid(column=2, row=2)
videojuegos = ttk.Checkbutton(thridFrame, text="Vieojuegos", variable=aficiones3).grid(column=3, row=2)

#fourthFrame 
radioB = StringVar()
estudiante = ttk.Radiobutton(fourthFrame, text="Estudiante", variable=radioB, value='estudiante', compound='center').grid(column=1, row=1, sticky=(W))
empleado = ttk.Radiobutton(fourthFrame, text="Empleado", variable=radioB, value='empleado', compound='center').grid(column=1, row=2, sticky=(W))
desempleado = ttk.Radiobutton(fourthFrame, text="Desempleado", variable=radioB, value='desempleado', compound='center').grid(column=1, row=3, sticky=(W))

#mainFrame
estado = StringVar()
comboEstados = ttk.Combobox(mainFrame, textvariable=estado)
comboEstados.grid(column=2, row=3)
comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

#fifthFrame       
def guardar(*args):
    nombreUsuario = nombre.get()
    aPaternoUsuario = aPaterno.get()
    aMaternoUsuario = aMaterno.get()
    correoUsuario = correo.get()
    movilUsuario = movil.get()
    aficiones1Usuario = aficiones1.get()
    aficiones2Usuario = aficiones2.get()
    aficiones3Usuario = aficiones3.get()   
    radioBUsuario = radioB.get()
    estadoUsuario = estado.get()
    #print(datos)

    with open('DatosFormulario.csv', 'a', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow([nombreUsuario, aPaternoUsuario, aMaternoUsuario, correoUsuario, movilUsuario, aficiones1Usuario, 
                               aficiones2Usuario, aficiones3Usuario, radioBUsuario, estadoUsuario])
    
    #nombreUsuario.set("")
    #aPaternoUsuario.set("")
    #aMaternoUsuario.set("")
    #correoUsuario.set("")
    #movilUsuario.set("")
    #aficiones1Usuario.set(False)
    #aficiones2Usuario.set(False)
    #aficiones3Usuario.set(False)
    #radioBUsuario.set("")
    #estadoUsuario.set("Estados")

def cerrar_ventana():
    raiz.destroy()
    #raiz2.destroy()

def mostrar_csv():
        ventana = Toplevel(raiz)
        ventana.title("Datos almacenados")
        
        with open("DatosFormulario.csv", mode="r") as archivo:
            lector = csv.reader(archivo)

            # Creamos la tabla utilizando un LabelFrame y Labels
            table_frame = ttk.LabelFrame(ventana, text='Datos')
            table_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

            row_num = 0
            for row in lector:
                label_1 = ttk.Label(table_frame, text=row[0], width=20, borderwidth=1, relief='solid')
                label_1.grid(row=row_num, column=0)
                
                label_2 = ttk.Label(table_frame, text=row[1], width=20, borderwidth=1, relief='solid')
                label_2.grid(row=row_num, column=1)
                
                label_3 = ttk.Label(table_frame, text=row[2], width=20, borderwidth=1, relief='solid')
                label_3.grid(row=row_num, column=2)

                label_4 = ttk.Label(table_frame, text=row[3], width=20, borderwidth=1, relief='solid')
                label_4.grid(row=row_num, column=3)
                
                label_5 = ttk.Label(table_frame, text=row[4], width=20, borderwidth=1, relief='solid')
                label_5.grid(row=row_num, column=4)
                
                label_6 = ttk.Label(table_frame, text=row[5], width=20, borderwidth=1, relief='solid')
                label_6.grid(row=row_num, column=5)

                label_7 = ttk.Label(table_frame, text=row[6], width=20, borderwidth=1, relief='solid')
                label_7.grid(row=row_num, column=6)
                
                label_8 = ttk.Label(table_frame, text=row[7], width=20, borderwidth=1, relief='solid')
                label_8.grid(row=row_num, column=7)
                
                label_9 = ttk.Label(table_frame, text=row[8], width=20, borderwidth=1, relief='solid')
                label_9.grid(row=row_num, column=8)

                label_10 = ttk.Label(table_frame, text=row[9], width=20, borderwidth=1, relief='solid')
                label_10.grid(row=row_num, column=9)

                row_num += 1


ttk.Button(fifthFrame, text="Guardar", command=guardar).grid(column=1, row=1, sticky=(W))
ttk.Label(fifthFrame, text= "                   ").grid(column=2, row=1)
ttk.Button(fifthFrame, text="Cancelar", command=cerrar_ventana).grid(column=3, row=1, sticky=(W))
ttk.Label(fifthFrame, text= "                   ").grid(column=4, row=1)
ttk.Button(fifthFrame, text="Ver csv", command=mostrar_csv).grid(column=1, row=2)  

#eigthFrame
def guardar_sqlite(*args):
    nombreUsuario = nombre.get()
    aPaternoUsuario = aPaterno.get()
    aMaternoUsuario = aMaterno.get()
    correoUsuario = correo.get()
    movilUsuario = movil.get()
    #aficiones1Usuario = aficiones1.get()
    #aficiones2Usuario = aficiones2.get()
    #aficiones3Usuario = aficiones3.get()   
    radioBUsuario = radioB.get()
    estadoUsuario = estado.get()
    datos = [(nombreUsuario, aPaternoUsuario, aMaternoUsuario, correoUsuario, movilUsuario, 
              #aficiones1Usuario, aficiones2Usuario, aficiones3Usuario, 
              radioBUsuario, estadoUsuario)]

    conexion = sqlite3.connect('DatosFormulario.db')
    c = conexion.cursor()

    #c.execute("CREATE TABLE formulario (nombre text, aPaterno text, aMaterno text, correo text, movil integer, radioB text, estado text)")
    
    c.executemany("INSERT INTO formulario VALUES (?,?,?,?,?,?,?)", datos)

    c.execute("SELECT * FROM formulario")
    print (c.fetchone())

    conexion.close()

ttk.Button(eighthFrame, text="Guardar en SQlite3", command=guardar_sqlite).grid(column=1, row=1, sticky=(W))

raiz.mainloop()