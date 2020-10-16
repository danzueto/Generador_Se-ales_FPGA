from tkinter import *
import tkinter.messagebox
import serial# Acceso a un puerto serie desde Python con PySerial

# COM10 puerto serie, a 9600 baudios, con 3 segundos de espera de timeout
#fpga=serial.Serial("COM10",9600,timeout=3)
# No es necesario abrir el puerto serie con open() si se configura al asignarlo
def generar():
	print ("Conexión 1 terminada")
def reinicio():
	fpga.write(b'1')
	print ("Conexión 2 terminada")
def finalizar():
	fpga.write(b'0')
	print ("Conexión 3 terminada")


#Funcion de seleccion de onda
def seleccion():
	Label(miFrame, text="                                             ").place(x=148,y=110)#borrador de texto
	lblimg=Label(miFrame, image=borrador).place(x=240,y=135)#borrador de imagen con fondo negro

	so=seleconda.get()
	if so==1:
		lblonda=Label(miFrame, text="Senoidal",font=("Arial",12)).place(x=148,y=110)
		lblimg=Label(miFrame, image=ondase).place(x=280,y=168)

	elif so==2:
		lblonda=Label(miFrame, text="Triangular",font=("Arial",12)).place(x=148,y=110)
		lblimg=Label(miFrame, image=ondat).place(x=270,y=160)

	elif so==3:
		lblondad=Label(miFrame, text="Dientes De Sierra",font=("Arial",12)).place(x=148,y=110)
		lblimg=Label(miFrame, image=ondads).place(x=280,y=160)

	elif so==4:
		lblonda=Label(miFrame, text="Pulso Gaussiano",font=("Arial",12)).place(x=148,y=110)
		lblimg=Label(miFrame, image=pulsog).place(x=253,y=160)

#Funcion que envia la señal al UART
def pulso():
	so=seleconda.get()
	sf=selecfrec.get()
	sa=selecamp.get()

	#convinciones de seleccion
	#1
	if so==1 and sf==1 and sa==1:
		print("111")
		fpga.write(b'2')
	elif so==1 and sf==1 and sa==2:
		print("112")
		fpga.write(b'6')
	elif so==1 and sf==1 and sa==3:
		print("113")
		fpga.write(b'10')
	elif so==1 and sf==2 and sa==1:
		print("121")
		fpga.write(b'14')
	elif so==1 and sf==2 and sa==2:
		print("122")
	elif so==1 and sf==2 and sa==3:
		print("123")
	#2
	elif so==2 and sf==1 and sa==1:
		print("211")
		fpga.write(b'3')
	elif so==2 and sf==1 and sa==2:
		print("212")
		fpga.write(b'7')
	elif so==2 and sf==1 and sa==3:
		print("213")
		fpga.write(b'11')
	elif so==2 and sf==2 and sa==1:
		print("221")
		fpga.write(b'15')
	elif so==2 and sf==2 and sa==2:
		print("222")
	elif so==2 and sf==2 and sa==3:
		print("223")
	#3
	elif so==3 and sf==1 and sa==1:
		print("311")
		fpga.write(b'4')
	elif so==3 and sf==1 and sa==2:
		print("312")
		fpga.write(b'8')
	elif so==3 and sf==1 and sa==3:
		print("313")
		fpga.write(b'12')
	elif so==3 and sf==2 and sa==1:
		print("321")
	elif so==3 and sf==2 and sa==2:
		print("322")
	elif so==3 and sf==2 and sa==3:
		print("323")
	#4
	elif so==4 and sf==1 and sa==1:
		print("411")
		fpga.write(b'5')
	elif so==4 and sf==1 and sa==2:
		print("412")
		fpga.write(b'9')
	elif so==4 and sf==1 and sa==3:
		print("413")
		fpga.write(b'13')
	elif so==4 and sf==2 and sa==1:
		print("421")
	elif so==4 and sf==2 and sa==2:
		print("422")
	elif so==4 and sf==2 and sa==3:
		print("423")
	#Error si el usuario no selecciona algun parametro
	else:
		tkinter.messagebox.showinfo('Error','Debe elegir todos los parametros de la onda')

#declarar interfaz
root=Tk()
root.geometry("750x550+550+250")#abrir la ventana en el centro y dimensaiones de la raiz
root.title("Selección De Onda")#Titulo de la ventana
root.iconbitmap("usac.ico")#icono

#declarar Frame
miFrame=Frame()
miFrame.pack()
miFrame.config(width=750, height=550)#dimensiones del Frame

#Imagenes
ondase=PhotoImage(file="onda-senoidal.png")
ondase=ondase.subsample(2,2)

ondat=PhotoImage(file="onda-triangular.gif")
ondat=ondat.subsample(1,1)

ondads=PhotoImage(file="onda-sierra.png")
ondads=ondads.subsample(2,2)

pulsog=PhotoImage(file="pulso-gaussiano.png")
pulsog=pulsog.subsample(1,1)

borrador=PhotoImage(file="borrador.png")
borrador=borrador.subsample(1,1)

#Textos
Label(miFrame, text="Generador De Onda",font=("Arial",24)).place(width=750)#Titulo
Label(miFrame, text="Seleccione la señal que desea generar:",font=("Arial",16)).place(x=10,y=50)
Label(miFrame, text="Forma de onda: ",font=("Arial",12)).place(x=30,y=110)
Label(miFrame, text="Seleccione la frecuencia:",font=("Arial",16)).place(x=10,y=340)
Label(miFrame, text="Seleccione la amplitud de la onda:",font=("Arial",16)).place(x=10,y=390)

#RadioButtons
seleconda=IntVar()
selecfrec=IntVar()
selecamp=IntVar()

rdbondase=Radiobutton(miFrame,text="Onda Senoidal",value=1,variable=seleconda,command=seleccion).place(x=10,y=80)
rdbondat=Radiobutton(miFrame,text="Onda Triangular",value=2,variable=seleconda,command=seleccion).place(x=210,y=80)
rdbondasi=Radiobutton(miFrame,text="Onda Dientes De Sierra",value=3,variable=seleconda,command=seleccion).place(x=410,y=80)
rdbpulso=Radiobutton(miFrame,text="Pulso Gaussiano",value=4,variable=seleconda,command=seleccion).place(x=610,y=80)
rdbf1=Radiobutton(miFrame,text="120 KHz",value=1,variable=selecfrec).place(x=250,y=370)
rdbf2=Radiobutton(miFrame,text="1000 KHz",value=2,variable=selecfrec).place(x=450,y=370)
rdba1=Radiobutton(miFrame,text="2 v",value=1,variable=selecamp).place(x=200,y=420)
rdba2=Radiobutton(miFrame,text="5 v",value=2,variable=selecamp).place(x=350,y=420)
rdba3=Radiobutton(miFrame,text="12 v",value=3,variable=selecamp).place(x=500,y=420)

#Botones
btngenerar=Button(miFrame,text="Generar Onda",font=(18),command=pulso).place(x=110,y=450,width=175,height=50)
btnreinicio=Button(miFrame,text="Reinicio",font=(18),command=reinicio).place(x=300,y=450,width=175,height=50)
btnfin=Button(miFrame,text="Finalizar El Proceso",font=(18),command=finalizar).place(x=490,y=450,width=175,height=50)

#Datos y pie de pagina
Label(miFrame, text="Universidad De San Caros De Guatemala, Facultad de ingenieria",font=("Arial",8)).place(x=10,y=510)
Label(miFrame, text="Proyecto Final, Electrónica 3. Daniel Anzueto 201318697 - Mario Najera 201245831",font=("Arial",8)).place(x=10,y=525)

root.mainloop()