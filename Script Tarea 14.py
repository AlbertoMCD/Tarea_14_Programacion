import pyodbc
import pandas as pd
import tkinter as tk

from tkinter import *
from tkinter import ttk #Importamos todas las funciones que contiene tkinter
from tkinter.ttk import *
from tkinter import messagebox

class General:
	def __init__(self, raiz):
		#Crear combobox elemento
		self.elemento = StringVar()
		self.label_elemento = Label(raiz, text = "Tipo elemento")
		self.label_elemento.grid(column=0, row=0)
		self.elemento = Combobox(raiz, values=('LOS', 'LOH', 'LR', 'LP', 'PC', 'TS'), width=10)
		self.elemento.grid(column=0, row=1)

		#Crear combobox condicion
		self.condicion = StringVar()
		self.label_condicion = Label(raiz, text = "Condición")
		self.label_condicion.grid(column=0, row=5)
		self.condicion = Combobox(raiz, values=('DESGASTE', 'FIN DE TIRO', 'GOLPE'), width=10)
		self.condicion.grid(column=0,row=6)

		#Crear botón buscar
		self.boton_buscar= Button(raiz, text="Buscar", command=self.buscar)
		self.boton_buscar.grid(column=0, row=30)

		#Crear botón borrar
		self.boton_borrar=Button(raiz, text="Borrar", command=self.borrar)
		self.boton_borrar.grid(column=0, row=40)

		#Crear listbox resultados
		self.lista= Listbox(raiz,width=20, height=10)
		self.lista.grid(column=0,row=20)


		#Definir función buscar
	def buscar(self):

		#Datos para conexión SQL Server
		server = 'LAPTOP-047T74PO'
		usuario = 'Usuario1'
		contrasena= '12345'
		bd = 'DB_Propia'

		#Obtener datos de combobox
		elemento_valor = "'" + self.elemento.get() + "'"
		condicion = "'" + self.condicion.get() + "'"

		#Conectar a base de datos
		try:
				conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +server+';DATABASE='+bd+';UID='+usuario+';PWD=' + contrasena, autocommit=True)
				print('Conexión exitosa')
		except:
				print('La conexión no fué exitosa')

		#Crear cursor y realizar búsqueda
		cursor = conexion.cursor()
		cursor.execute("SELECT Id FROM Datos_PC WHERE Elemento= " + elemento_valor + "AND Condicion = " + condicion)
		datos = cursor.fetchall()
		conexion.commit()
		#Cerrar conexión
		conexion.close()

		#Convertir datos en tupla
		tupla_datos=tuple(datos)
		self.lista.delete(0,tk.END)
		self.lista.insert(0,*tupla_datos)

		#Definir función borrar
	def borrar(self):
		self.elemento.set("")
		self.condicion.set("")
		self.lista.delete(0,tk.END)


raiz = Tk()
raiz.title("Filtro Elementos")
raiz.geometry('150x330')
#raiz.resizable(1,1)
raiz.config(bg="#49A")
raiz.config(bd=8)
raiz.config(relief="ridge")
estructura = General(raiz)

raiz.mainloop()