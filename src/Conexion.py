# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


try:
    import os, sqlite3
    bbdd = 'act17.sqlite'
    conex = sqlite3.connect(bbdd)
    conex.text_factory= str
    cur = conex.cursor()
except:
    print "Posibles errores de importacion"
    sys.exit(1)
    
    
def provincias():
    try:
        cur.execute("select provincia from provincias")
        listado = cur.fetchall()
        return listado
    except:
        print("hubo un error ")
        conex.rollback
        
def municipios(prov):
    try:
        print prov
        cur.execute("select id from provincias where provincia=?", (prov,))
        id = cur.fetchone()
        cur.execute("select municipio from municipios where provincia_id=?", (id[0],))
        listado = cur.fetchall()
        return listado
    except:
        print("hubo un errormunicipios")
        conex.rollback
