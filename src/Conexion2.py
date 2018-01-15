# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "a16sergiopc"
__date__ = "$Jan 15, 2018 3:12:43 PM$"

try:
    import os, sqlite3
    bbdd = 'Basefacturas.sqlite'
    conex = sqlite3.connect(bbdd)
    conex.text_factory= str
    cur = conex.cursor()
except:
    print "Posibles errores de importacion"
    sys.exit(1)
    
def GuardarCliente(file):
    