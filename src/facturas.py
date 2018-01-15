# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

___author__ = "a16sergiopc"
__date__ = "$Jan 8, 2018 10:58:38 AM$"


import os
os.environ["UBUNTU_MENUPROXY"]="0"
import gi 
import Conexion
import ModuloMunicipios
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Facturas():
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file("ventanaGlade.glade")
        #Ventana Principal
        self.ventanaPrincipal=b.get_object("window1")
        #Salir
        self.btSalir=b.get_object("butSalir1")
        #Altas Clientes
        self.entryDNI=b.get_object("entryDNI1")
        self.entryNombre=b.get_object("entryNombre1")
        self.entryApellido=b.get_object("entryApellido1")
        self.entryDIreccion1=b.get_object("entryDIreccion1")
        self.entryTelefono=b.get_object("entryTelefono1")
        self.entryEmail=b.get_object("entryEmail1")
        self.entryCategoria=b.get_object("entryCategoria1")
        self.entryLocalidad=b.get_object("entryLocalidad1")
        self.comboProvincia=b.get_object("combobox1")
        self.comboMunicipio=b.get_object("combobox2")
        #Ventana Municipios
        self.btnSeleccionarLocalidad=b.get_object("btnSeleccionarLocalidad1")
        self.VenMuni=b.get_object("VenPrinp")
        self.ventana=b.get_object("VenPrinp")
        self.CProvincia=b.get_object("combobox1")
        self.CMunicipio=b.get_object("combobox2")
        self.LProvincia=b.get_object("Provincia")
        self.LMunicipio=b.get_object("Municipio")
        dic={"on_butSalir1_clicked":self.Salir,"on_btnSeleccionarLocalidad1_clicked":self.MostrarVentanaMunicipios,"on_combobox1_changed":self.selprov,
        "on_combobox2_changed":self.CogerProvincia}
        b.connect_signals(dic)
        self.ventanaPrincipal.show()
        
    def Salir(self,widget,data=None):
        Gtk.main_quit()
    def MostrarVentanaMunicipios(self,widget,data=None):
        self.VenMuni.show()
        ModuloMunicipios.cargarcmbprov(self,widget)
    def selprov(self,widget,data=None):
        ModuloMunicipios.selprov(self,widget)
    def CogerProvincia(self,widget,data=None):
        index = self.CMunicipio.get_active()
        model = self.CMunicipio.get_model()
        localidad = model[index]
        self.entryLocalidad.set_text(localidad[0])
    
    
if __name__ == "__main__":
    main = Facturas()
    Gtk.main()