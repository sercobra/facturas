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
import datetime
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
        self.ListaClientes=b.get_object("ListaClientes")
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
        #Ventana Ventas
        self.CidCliente=b.get_object("combobox3")
        self.CidProducto=b.get_object("combobox4")
        self.entryCantidad=b.get_object("entry2")
        self.ListaCliente=b.get_object("ListaCliente")
        self.listaProductos=b.get_object("listaProductos")
        self.ListaVentas=b.get_object("listaVentas")
        self.NUMFACTURA=""
        #Coger Ventas
        self.TablaVentas=b.get_object("treeview6")
        self.IDVENTAS=""
        self.LabelCliente=b.get_object("label4")
        self.LabelProducto=b.get_object("label5")
        
        dic={"on_butSalir1_clicked":self.Salir,"on_btnSeleccionarLocalidad1_clicked":self.MostrarVentanaMunicipios,"on_combobox1_changed":self.selprov,
        "on_combobox2_changed":self.CogerProvincia,"on_AltasCliente1_clicked":self.AltasCliente,"on_treeview4_cursor_changed":self.seleccionarCliente,
        "on_AltasProductos1_clicked":self.altasProductos,"on_treeview5_cursor_changed":self.CogerProducto,"on_BajasCliente1_clicked":self.BorrarCliente,
        "on_BajasProductos1_clicked":self.BorrarProducto,"on_ModificacionesCliente1_clicked":self.ModificarCliente,"on_ModificacionesProductos1_clicked":self.ModificarProducto,
        "on_AltasVentas1_clicked":self.AltaVentas,"on_BajasVentas1_clicked":self.BajasVenta,"on_treeview6_cursor_changed":self.CogerVenta,"on_ModificacionesVentas1_clicked":self.ModificarVenta,
        "on_combobox3_changed":self.MostrarDNIcliente,"on_combobox4_changed":self.MostrarNombreProd}
        b.connect_signals(dic)
        
        self.ventanaPrincipal.show()
        self.ListarClientes(self)
        self.ListarProductos(self)
        self.ListaIdCliente(self)
        self.ListaIdProducto(self)
        
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
       respuesta=ModuloMunicipios.ValidoDNI(self,widget,DNI)
       print respuesta
       
       if respuesta == True:
           if Nombre != None and Apellido !=None and Direccion !=None and Telefono !=None and Email !=None and Categoria !=None and Localidad !=None:
               Fila=(DNI,Nombre,Apellido,Direccion,Telefono,Email,Categoria,Localidad)
               Conexion2.GuardarCliente(Fila)
               ModuloMunicipios.LimpiarRegistroClientes(self,widget)
               self.ListarClientes(self,widget)
           else:
               print "Introduce todos los datos"
       else:
           print "Escribe bien el dni"
    def ListarClientes(self,widget,data=None):
            Lista=Conexion2.ListarCLientes()
            self.ListaClientes.clear()
            for registro in Lista:
                self.ListaClientes.append(registro)
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
            self.ListarClientes(self)
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
       
            respuesta=ModuloMunicipios.ValidoDNI(self,widget,DNI)
       
            if respuesta == True:
                if Nombre != None and Apellido !=None and Direccion !=None and Telefono !=None and Email !=None and Categoria !=None and Localidad !=None:
                    Fila=(DNI,Nombre,Apellido,Direccion,Telefono,Email,Categoria,Localidad,self.IDCLIENTE)
                    Conexion2.ModificarCliente(Fila)
                    ModuloMunicipios.LimpiarRegistroClientes(self,widget)
                    self.ListarClientes(self,widget)
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
            FilaProd=(Producto,Precio,Stock)
            Conexion2.GuardarProductos(FilaProd)
            ModuloMunicipios.LimpiarRegistrosProductos(self,widget)
            self.ListarProductos(self,widget)
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
            self.entryPreProducto.set_text(str(Precio))
            Stock=model.get_value(iter,3)
            self.entryStock.set_text(str(Stock))
    def BorrarProducto(self,widget,data=None):
        if self.IDPRODUCTO!=None:
            Conexion2.BorrarPRoducto(self.IDPRODUCTO)
            ModuloMunicipios.LimpiarRegistroClientes(self,widget)
            self.ListarProductos(self)
            self.LimpiarRegistrosProductos(self)
        else:
            print "Seleccione un producto para borrar"
    def ModificarProducto(self,widget,data=None):
        if self.IDPRODUCTO!=None:
            Producto=self.entryNomProducto.get_text()
            Precio=self.entryPreProducto.get_text()
            Stock=self.entryStock.get_text()
            if Producto!=None and Precio!=None and Stock!=None:
                FilaProd=(Producto,Precio,Stock,self.IDPRODUCTO)
                Conexion2.MoficarPRoductos(FilaProd)
                ModuloMunicipios.LimpiarRegistrosProductos(self,widget)
                self.ListarProductos(self,widget)
            else:
                print "Pon los datos del producto"
        else:
            print "Seleccione un producto para modificar"
    def AltaVentas(self,widget,data=None):
        index= self.CidClient.get_active()
        model= self.CidClient.get_model()
        idCliente= model[index]
        index= self.CidProducto.get_active()
        model= self.CidProducto.get_model()
        idProducto=model[index]
        Fecha=datetime.date.today()
        if self.NUMFACTURA==None:
            FilaProducto=(idCliente,Fecha)
            self.Conexion2.GuardarFactura(FilaProducto)
            Cantidad=self.entryCantidad.get_text()
            self.NUMFACTURA=Conexion2.CargarFacturaCli(idCliente)
        
            
        
        if idCliente!=None and idProducto!=None and Cantidad!=None:
            Producto=Conexion2.CogerProducto(idProducto)
            Precio = Producto[3]
            Calculo = float(Precio)*float(Cantidad)
            
            filaVenta=(self.NUMFACTURA,idCliente[0],idProducto[0],Cantidad,Calculo,idCliente)
            Conexion2.GuardarVEnta(filaVenta)
            self.ListarVentas(self,widget)
            
        else:
            print "La venta debe tener idCLiente, idProducto y cantidad"
    def ListarVentas(self,widget,data=None):
         Lista=Conexion2.ListarVEntas()
         self.ListaVentas.clear()
         for registro in Lista:
            self.ListaVentas.append(registro)
    def CogerVenta(self,widget,data=None):
         model, iter= self.TablaVentas.get_selection().get_selected()
         
         if iter!=None:
             self.IDVENTAS=model.get_value(iter,0)
             self.NUMFACTURA=model.get_value(iter,1)
             self.CidProducto.set_active(model.get_value(iter,2))
             self.CidCliente.set_active(model.get_value(iter,3))
             self.entryCantidad.set_text(str(model.get_value(iter,5)))
    def BajasVenta(self,widget,data=None):
        if self.IDVENTAS!=None:
            Conexion2.BorrarVentas(self.IDVENTAS)
        else:
            print "Elige una venta"
    def ModificarVenta(self,widget,data=None):
        index= self.CidClient.get_active()
        model= self.CidClient.get_model()
        idCliente= model[index]
        index= self.CidProducto.get_active()
        model= self.CidProducto.get_model()
        idProducto=model[index]
        Fecha=datetime.date.today()
        if self.NUMFACTURA==None:
            FilaProducto=(idCliente,Fecha)
            self.Conexion2.GuardarFactura(FilaProducto)
            Cantidad=self.entryCantidad.get_text()
            self.NUMFACTURA=Conexion2.CargarFacturaCli(idCliente)
        
            
        
        if idCliente!=None and idProducto!=None and Cantidad!=None:
            Producto=Conexion2.CogerProducto(idProducto)
            Precio = Producto[3]
            Calculo = float(Precio)*float(Cantidad)
            if self.IDVENTAS!=None:
                filaVenta=(self.NUMFACTURA,idCliente[0],idProducto[0],Cantidad,Calculo,idCliente,self.IDVENTAS)
                Conexion2.ModificarVEnta(filaVenta)
                self.ListarVentas(self,widget)
            else:
                print "Seleccione una venta"
            
        else:
            print "La venta debe tener idCLiente, idProducto y cantidad"
    def ListaIdCliente(self,widget,data=None):
         Lista=Conexion2.ListarIDcliente()
         self.ListaVentas.clear()
         for registro in Lista:
             self.ListaCliente.append(registro)
    def ListaIdProducto(self,widget,data=None):
         Lista=Conexion2.ListarIDproducto()
         self.ListaVentas.clear()
         for registro in Lista:
            self.listaProductos.append(registro)
    def MostrarDNIcliente(self,widget,data=None):
        index= self.CidCliente.get_active()
        model= self.CidCliente.get_model()
        idCliente= model[index]
        print idCliente[0]
        dato=Conexion2.CogerDNICliente(idCliente[0])
        print dato
        self.LabelCliente.set_text(dato[1])
    def MostrarNombreProd(self,widget,data=None):
        index= self.CidProducto.get_active()
        model= self.CidProducto.get_model()
        idProducto=model[index]
        dato=Conexion2.CogerNOmbreProducto(idProducto[0])
        print dato
        self.LabelProducto.set_text(dato[1])
        
if __name__ == "__main__":
    main = Facturas()
    Gtk.main()