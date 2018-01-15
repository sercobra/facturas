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

