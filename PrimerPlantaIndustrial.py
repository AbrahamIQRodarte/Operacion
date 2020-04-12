import tkinter as tk
import schedule
#Funciones
tiempo = [0]
abertura = []
vtgl=[]
vtcl=[]
proceso = 0
def R(t = 1, vtg=100, vtc=0):
    tiempo.append(t)
    vtgl.append(vtg)
    vtcl.append(vtc)
    global proceso
    try:
        x=int(Abertura.get())
        abertura.append(x)
    except ValueError:
        x = 0
    tvtg = '{0:.2f}'.format(vtgl[-1])
    niveltg['text'] = tvtg
    tvtc = '{0:.2f}'.format(vtcl[-1])
    niveltc['text'] = tvtc
    proceso=miFrame.after(1000, R, (t+1), (vtg-(tiempo[t]-tiempo[t-1])*x/100),(vtc+(tiempo[t]-tiempo[t-1])*x/100))
    print(abertura)
    print(tiempo)
    print(vtgl)
    print(vtcl)
    if vtgl[-1]<0:
        miFrame.after_cancel(proceso)
        niveltg['text'] = 0
        niveltc['text'] = 100
    
    

root = tk.Tk()
root.title("Primera Planta Industrial")
root.geometry("600x450")
x=tk.StringVar()
#A partir de aqui de dará forma a la ventana
#Se creará un Frame

miFrame=tk.Frame(root)
miFrame.pack()
#Imagen de fondo
fondo_imagen=tk.PhotoImage(file = "Fondo.png") 
fondo = tk.Canvas(miFrame, height=450, width=600)
background_label = tk.Label(miFrame, image=fondo_imagen)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
fondo.pack()
#Nombre de los instrumentos y equipos
label_tg=tk.Label(miFrame, text="Tanque Grande")
label_tg.place(x = 90, y = 100)
label_tc=tk.Label(miFrame, text="Tanque Chico")
label_tc.place(x = 470, y = 350)
label_nivel_tg=tk.Label(miFrame, text="%Nivel=")
label_nivel_tg.place(x = 200, y = 100)
label_nivel_tc=tk.Label(miFrame, text="%Nivel=")
label_nivel_tc.place(x = 300, y = 350)
label_valvula=tk.Label(miFrame, text="%Abertura Valvula=")
label_valvula.place(x = 200, y = 300)

#Salida de Valores
niveltg=tk.Label(miFrame)
niveltg.place(x=250, y=100)
niveltc=tk.Label(miFrame)
niveltc.place(x=350,y=350)
#Entrada de Valores
Abertura=tk.Entry(miFrame, textvariable=x)
Abertura.place(x = 310, y = 300)
#Boton
botonArrancar=tk.Button(miFrame, text="Arrancar", command=R)
botonArrancar.place(x = 90, y = 380)



root.mainloop()