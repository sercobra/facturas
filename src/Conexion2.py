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