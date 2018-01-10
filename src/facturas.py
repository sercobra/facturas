# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "a16sergiopc"
__date__ = "$Jan 8, 2018 10:58:38 AM$"

import os
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Facturas():
    def __init__(self):
        b=Gtk.Builder()
        b.add_from_file("ventanaGlade.glade")
        #Ventana Principal
        self.ventanaPrincipal=b.get_object("ventanaPrinp")
        #Salir
        self.btSalir=b.get_object("butSalir")
        
        dic={"on_butSalir_clicked":self.Salir}
        b.connect_signals(dic)
        self.ventanaPrincipal.show()
        
        
    def Salir(self,widget,data=None):
        Gtk.main_quit()








if __name__ == "__main__":
    main=Facturas()
    Gtk.main()