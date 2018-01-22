# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "a16sergiopc"
__date__ = "$Jan 15, 2018 3:12:43 PM$"

try:
    import os, sqlite3
    bbdd = 'Basefacturas'
    conex = sqlite3.connect(bbdd)
    conex.text_factory= str
    cur = conex.cursor()
except:
    print "Posibles errores de importacion"
    sys.exit(1)
    
def GuardarCliente(file):
   try: 
    print file
    cur.execute("insert into cliente(DNI,nombre,apellido,direccion,telefono,email,categoria,localidad) values(?,?,?,?,?,?,?,?)",file)
    conex.commit()
   except:
       print "Error al guardar clientes"
       conex.rollback
def ListarCLientes():
    try:
       cur.execute("select * from cliente")
       listado = cur.fetchall()
       conex.commit()
       return listado
    except:
        print "Error al listar los clientes"
        conex.rollback
def BorrarCLiente(idCliente):
    try:
       cur.execute("delete from cliente where id_cliente=?",(idCliente,))
       conex.commit()
    except:
        print "Error al borrar el cliente"
        conex.rollback
def ModificarCliente(Fila):
    try:
        cur.execute("Update cliente SET DNI=?,nombre=?,apellido=?,direccion=?,telefono=?,email=?,categoria=?,localidad=? where id_cliente=?",Fila)
        conex.commit()
    except:
        print "Error al modificar el cliente"
        conex.rollback
def GuardarProductos(Fila):
    try: 
        cur.execute("insert into producto(nombre,precio,stock) values(?,?,?)",Fila)
        conex.commit()
    except:
       print "Error al guardar producto"
       conex.rollback
def ListarPRoductos():
    try:
       cur.execute("select * from producto")
       listado = cur.fetchall()
       conex.commit()
       return listado
    except:
        print "Error al listar los productos"
        conex.rollback
def BorrarPRoducto(idProducto):
    try:
       cur.execute("delete from producto where id_producto=?",(idProducto,))
       conex.commit()
    except:
        print "Error al borrar el producto"
        conex.rollback
def MoficarPRoductos(fila):
    try:
        cur.execute("Update producto SET nombre=?,precio=?,stock=? where id_producto=? ",Fila)
        conex.commit()
    except:
        print "Error al modificar el producto"
        conex.rollback
def CogerProducto(idProducto):
    try:
        cur.execute("select * from producto where id_producto=?",(idProducto))
        listado = cur.fetchone()
        conex.commit()
        return listado
    except:
        print "Error al coger producto"
        conex.rollback
def GuardarFactura(filaFactura):
    try: 
        cur.execute("insert into Factura(id_cliente,fecha) values(?,?,?)",filaFactura)
        conex.commit()
    except:
       print "Error al crear factura"
       conex.rollback
def CargarFacturaCli(idCLiente):
    try:
        cur.execute("select * from Factura where id_cliente=?",(idCLiente))
        listado = cur.fetchone()
        conex.commit()
        return listado
    except:
        print "Error al coger numero factura"
        conex.rollback
def GuardarVEnta(filaVentas):
    try: 
        cur.execute("insert into Ventas(id_factura,idProducto,cantidad,precio,idCliente) values(?,?,?,?)",filaVentas)
        conex.commit()
    except:
       print "Error al guardar venta"
       conex.rollback
def ListarVEntas():
    try:
        cur.execute("select * from Ventas")
        listado = cur.fetchall()
        conex.commit()
        return listado
        
    except:
        print "Error al listar la venta"
        conex.rollback()
def ModificarVEnta(ListaVEnta):
    try:
        cur.execute("Update ventas id_factura=?,idProducto=?,cantidad=?,precio=?,idCliente=? where num_detalle=?",ListaVEnta)
        conex.commit()
    except:
       print "Error al modificar venta"
       conex.rollback
def BorrarVentas(IDVENTA):
    try:
        cur.execute("Delete from ventas where num_detalle=?",IDVENTA)
        conex.commit()
    except:
        print "Error al borrar la venta"
        conex.rollback
def ListarIDcliente():
    try:
        cur.execute("select id_cliente from cliente")
        listado = cur.fetchall()
        conex.commit()
        return listado
        
    except:
        print "Error al listar la venta"
        conex.rollback()
        
def ListarIDproducto():
    try:
        cur.execute("select id_producto from producto")
        listado = cur.fetchall()
        conex.commit()
        return listado
        
    except:
        print "Error al listar la venta"
        conex.rollback()
def CogerDNICliente(id):
    try:
        cur.execute("select * from cliente where id_cliente=?",id)
        listado = cur.fetchall()
        conex.commit()
        return listado
        
    except:
        print "Error al mostrar DNI cliente"
        conex.rollback()
def CogerNOmbreProducto(id):
    try:
        cur.execute("select * from producto where id_producto=?",id)
        listado = cur.fetchall()
        conex.commit()
        return listado
        
    except:
        print "Error al mostrar nombre cliente"
        conex.rollback()