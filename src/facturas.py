# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

___author__ = "a16sergiopc"
__date__ = "$Jan 8, 2018 10:58:38 AM$"


import os
os.environ["UBUNTU_MENUPROXY"]="0"
import gi 
import Conexion
import Conexion2
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
        #Lista clientes
        self.ListaCliente=b.get_object("ListaCliente")
        self.TablaClientes=b.get_object("treeview4")
        self.IDCLIENTE=""
        #Altas Producto
        self.entryNomProducto=b.get_object("entryNomProducto1")
        self.entryPreProducto=b.get_object("entryPreProducto1")
        self.entryStock=b.get_object("entryStock1")
        #Lista Producto
        self.ListaProductos=b.get_object("ListaProductos")
        self.TablaProductos=b.get_object("treeview5")
        self.IDPRODUCTO=""
        
        dic={"on_butSalir1_clicked":self.Salir,"on_btnSeleccionarLocalidad1_clicked":self.MostrarVentanaMunicipios,"on_combobox1_changed":self.selprov,
        "on_combobox2_changed":self.CogerProvincia,"on_AltasCliente1_clicked":self.AltasCliente,"on_treeview4_cursor_changed":self.seleccionarCliente,
        "on_AltasProductos1_clicked":self.altasProductos,"on_treeview5_cursor_changed":self.CogerProducto,"on_BajasCliente1_clicked":self.BorrarCliente,
        "on_BajasProductos1_clicked":self.BorrarProducto,"on_ModificacionesCliente1_clicked":self.ModificarCliente,"on_ModificacionesProductos1_clicked":self.ModificarProducto}
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
    def AltasCliente(self,widget,data=None):
       DNI= self.entryDNI.get_text()
       Nombre=self.entryNombre.get_text()
       Apellido= self.entryApellido.get_text()
       Direccion= self.entryDIreccion1.get_text()
       Telefono= self.entryTelefono.get_text()
       Email= self.entryEmail.get_text()
       Categoria= self.entryCategoria.get_text()
       Localidad= self.entryLocalidad.get_text()
       print DNI
       respuesta=ModuloMunicipios.ValidoDNI(DNI,self,widget)
       
       if respuesta == True:
           if Nombre != None and Apellido !=None and Direccion !=None and Telefono !=None and Email !=None and Categoria !=None and Localidad !=None:
               Fila(DNI,Nombre,Apellido,Direccion,Telefono,Email,Categoria,Localidad)
               Conexion2.GuardarCliente(Fila)
               ModuloMunicipios.LimpiarRegistroClientes(self,widget)
               ListarClientes(self,widget)
           else:
               print "Introduce todos los datos"
       else:
           print "Escribe bien el dni"
    def ListarClientes(self,widget,data=None):
            Lista=Conexion2.ListarCLientes()
            self.ListaCliente.clear()
            for registro in Lista:
                self.ListaCliente.append(registro)
    def seleccionarCliente(self,widget,data=None):
        model, iter= self.TablaClientes.get_selection().get_selected()
        
        if iter!=None:
            self.IDCLIENTE=model.get_value(iter,0)
            DNI=str(model.get_value(iter,1))
            self.entryDNI.set_text(DNI)
            Nombre=str(model.get_value(iter,2))
            self.entryNombre.set_text(Nombre)
            Apellido=str(model.get_value(iter,3))
            self.entryApellido.set_text(Apellido)
            Direccion=str(model.get_value(iter,4))
            self.entryDIreccion1.set_text(Direccion)
            Telefono=str(model.get_value(iter,5))
            self.entryTelefono.set_text(Telefono)
            Email=str(model.get_value(iter,6))
            self.entryEmail.set_text(Email)
            Categoria=str(model.get_value(iter,7))
            self.entryCategoria.set_text(Categoria)
            Localidad=str(model.get_value(iter,8))
            self.entryLocalidad.set_text(Localidad)
    def BorrarCliente(self,widget,data=None):
        if self.IDCLIENTE!=None:
            Conexion2.BorrarCLiente(self.IDCLIENTE)
            ModuloMunicipios.LimpiarRegistroClientes(self,widget)
        else:
            print "Seleccione un cliente para borrar"
    def ModificarCliente(self,widget,data=None):
        if self.IDCLIENTE!=None:
            DNI= self.entryDNI.get_text()
            Nombre=self.entryNombre.get_text()
            Apellido= self.entryApellido.get_text()
            Direccion= self.entryDIreccion1.get_text()
            Telefono= self.entryTelefono.get_text()
            Email= self.entryEmail.get_text()
            Categoria= self.entryCategoria.get_text()
            Localidad= self.entryLocalidad.get_text()
       
            respuesta=ModuloMunicipios.ValidoDNI(DNI,self,widget)
       
            if respuesta == True:
                if Nombre != None and Apellido !=None and Direccion !=None and Telefono !=None and Email !=None and Categoria !=None and Localidad !=None:
                    Fila(DNI,Nombre,Apellido,Direccion,Telefono,Email,Categoria,Localidad,self.IDCLIENTE)
                    Conexion2.ModificarCliente(Fila)
                    ModuloMunicipios.LimpiarRegistroClientes(self,widget)
                    ListarClientes(self,widget)
                else:
                    print "Introduce todos los datos"
            else:
                print "Escribe bien el dni"
        else:
            print "Seleccione un cliente a modificar"
    def altasProductos(self,widget,data=None):
        Producto=self.entryNomProducto.get_text()
        Precio=self.entryPreProducto.get_text()
        Stock=self.entryStock.get_text()
        if Producto!=None and Precio!=None and Stock!=None:
            FilaProd(Producto,Precio,Stock)
            Conexion2.GuardarProductos(FilaProd)
            ModuloMunicipios.LimpiarRegistrosProductos(self,widget)
            ListarProductos(self,widget)
        else:
            print "Pon los datos del producto"
    def ListarProductos(self,widget,data=None):
        Lista=Conexion2.ListarPRoductos()
        self.ListaProductos.clear()
        for registro in Lista:
            self.ListaProductos.append(registro)
    def CogerProducto(self,widget,data=None):
         model, iter= self.TablaProductos.get_selection().get_selected()
         
         if iter!=None:
            self.IDPRODUCTO=model.get_value(iter,0)
            Nombre=model.get_value(iter,1)
            self.entryNomProducto.set_text(Nombre)
            Precio=model.get_value(iter,2)
            self.entryPreProducto.set_text(Precio)
            Stock=model.get_value(iter,3)
            self.entryStock.set_text(Stock)
    def BorrarProducto(self,widget,data=None):
        if self.IDPRODUCTO!=None:
            Conexion2.BorrarPRoducto(self.IDPRODUCTO)
            ModuloMunicipios.LimpiarRegistroClientes(self,widget)
        else:
            print "Seleccione un producto para borrar"
    def ModificarProducto(self,widget,data=None):
        if self.IDPRODUCTO!=None:
            Producto=self.entryNomProducto.get_text()
            Precio=self.entryPreProducto.get_text()
            Stock=self.entryStock.get_text()
            if Producto!=None and Precio!=None and Stock!=None:
                FilaProd(Producto,Precio,Stock,self.IDPRODUCTO)
                Conexion2.MoficarPRoductos(FilaProd)
                ModuloMunicipios.LimpiarRegistrosProductos(self,widget)
                ListarProductos(self,widget)
            else:
                print "Pon los datos del producto"
        else:
            print "Seleccione un producto para modificar"
            
if __name__ == "__main__":
    main = Facturas()
    Gtk.main()