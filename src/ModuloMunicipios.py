# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "a16sergiopc"
__date__ = "$Jan 15, 2018 2:20:10 PM$"

import Conexion

def CargarMunicipio(self,widget,data=None):
        listado = Conexion.municipios(self.item[0])
        for row in listado:
            self.LMunicipio.append(row)
            
def cargarcmbmunicipios(self):
        listado = Conexion.municipios(self.item[0])
        for row in listado:
            self.LMunicipio.append(row)
            
def cargarcmbprov(self, widget,data=None):
        print "llego aqui"
        lista = Conexion.provincias()
        for row in lista:
            self.LProvincia.append(row)
    
def selprov(self, widget):
        index = self.CProvincia.get_active()
        model = self.CProvincia.get_model()
        self.item = model[index]
        # elegimos la provincia que nos indica el index
        self.LMunicipio.clear()
        #limpiamos cada vez que cambiamos de provincia
        cargarcmbmunicipios(self)

def ValidoDNI(self,widget,dni):
    try:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE" #letras del dni
        dig_ext = "XYZ" #tabla letras extranjero
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'} #letras que identifican extranjero
        numeros = "1234567890"
        dni = dni.upper() #pasa letras a mayusculas
        if len(dni) == 9: #el dni debe tener 9 caracteres
            dig_control = dni[8]
            dni = dni[:8]
        if dni[0] in dig_ext:
                # la letra
                #el numero que son los 8 primeros
                # comprueba que es extranjero
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23] ==  dig_control
       
        # devuelve true o si no devuelva false
        return False
    except:
        print 'Error con el dni'
        return None
        
def LimpiarRegistroClientes(self,widget):
    self.entryDNI.set_text("")
    self.entryNombre.set_text("")
    self.entryApellido.set_text("")
    self.entryDIreccion1.set_text("")
    self.entryTelefono.set_text("")
    self.entryEmail.set_text("")
    self.entryCategoria.set_text("")
    self.entryLocalidad.set_text("")
def LimpiarRegistrosProductos(self,widget):
    self.entryNomProducto.set_text("")
    self.entryPreProducto.set_text("")
    self.entryStock.set_text("")