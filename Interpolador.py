#Bienvenidos a mi aplicación para interpolar datos de tablas
from tkinter import *
from tkinter import messagebox               #Este paquete es para importar las ventanas emergentes
def R():
    y1=float(Y1.get())
    x1=float(X1.get())
    y2=float(Y2.get())
    x2=float(X2.get())
    x=float(X.get())
    R=y1+(x-x1)*((y2-y1)/(x2-x1))
    Y.delete(0, END)
    Y.insert(0,R)

root = Tk()                         #Aqui generaremos la ventana con el paquete tkinter previamente importado
root.title("Interpolador")            #Este es el título de la aplicación
root.resizable(False,False)


var=StringVar()
y1=StringVar()
x1=StringVar()
y2=StringVar()
x2=StringVar()
x=StringVar()

def clr():
    try:
        y1.set("")
        x1.set("")
        y2.set("")
        x2.set("")
        x.set("")
        var.set("")
    except ValueError:
        pass
#A partir de aqui generare un menu de ayuda para explicar el función de la aplicación
#-------------------------------Ayuda----------------------------
def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto con licencia pirata llama a la policía")
def infoAdicional():
    messagebox.showinfo("Respecto a que valor interpolar???", "Utilice el valor más cercano a los datos experimetales en la pareja 1 para una mayor exactitud ya que respecto a ese valor se calculara b de la formula de la recta Y=MX+b")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#A partir de aqui de dará forma a la ventana
#Se creará un Frame
miFrame=Frame(root)
miFrame.pack()

a=3

XLabel=Label(miFrame, text="X")
XLabel.grid(row=0, column=2, padx=a, pady=a)

YLabel=Label(miFrame, text="Y")
YLabel.grid(row=0, column=3, padx=a, pady=a)


X1=Entry(miFrame, textvariable=x1)
X1.grid(row=1, column=2)

Y1=Entry(miFrame, textvariable=y1)
Y1.grid(row=1, column=3)

X2=Entry(miFrame, textvariable=x2)
X2.grid(row=2, column=2)

Y2=Entry(miFrame, textvariable=y2)
Y2.grid(row=2, column=3)

Texto1Label=Label(miFrame, text="1")
Texto1Label.grid(row=1, column=1, sticky="e", padx=a, pady=a)

Texto2=Label(miFrame, text="2")
Texto2.grid(row=2, column=1, sticky="e", padx=a, pady=a)

ResultadoLabel=Label(miFrame, text="Resultado")
ResultadoLabel.grid(row=3, column=3, sticky="e", padx=a, pady=a)

ValorLabel=Label(miFrame, text="Valor X")
ValorLabel.grid(row=3, column=2, sticky="e", padx=a, pady=a)

X=Entry(miFrame, textvariable=x)
X.grid(row=4, column=2)

Y=Entry(miFrame, textvariable=var, borderwidth=5)
Y.grid(row=4, column=3, sticky="e", padx=a, pady=a)
Y.config(bg="Black", fg="White")

botonCalcular=Button(miFrame, text="Calcular", command=R)
botonCalcular.grid(row=5, column=2, sticky="e", padx=a, pady=a)

botonLimpiar=Button(miFrame, text="Limpiar", command=clr)
botonLimpiar.grid(row=5, column=3, sticky="e", padx=a, pady=a)


root.config(cursor="pirate")   #Todo lo que le aplicas al Frame se lo puedes aplicar a la raiz 
root.mainloop()