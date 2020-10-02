# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:17:27 2020

@author: hp 
"""
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import io


#%%
''' 
LECTURA DE UNA TABLA DESDE UNA BASE DE DATOS
'''
'''Lectura completa de una tabla'''
conn = psycopg2.connect("dbname=Sesion_17 user=SciData_CDD_Py password=abcde host=localhost")

sql = "SELECT * FROM alcaldias"
ALCALDIAS = pd.read_sql(sql,con = conn)
conn.close()

ALCALDIAS.columns

#%%
'''Lectura filtrada de una tabla'''
conn = psycopg2.connect("dbname=Sesion_17 user=SciData_CDD_Py password=abcde host=localhost")

Xochimilco = pd.read_sql(sql+" WHERE description LIKE 'Xochimilco'",con = conn)
Xochimilco

conn.close()
#%%

conn = psycopg2.connect("dbname=Sesion_17 user=SciData_CDD_Py password=abcde host=localhost")
num_alcaldia = input("Ingresa el código numérico de la alcaldia:\t")
airbnb_filtrada = pd.read_sql("SELECT * FROM airbnb_cdmx"+f" WHERE neighbourhood = {num_alcaldia}",con = conn)

airbnb_filtrada.shape

conn.close()

#%%
'''
INTERACCIÓN CON PGADMIN 4 DESDE PYTHON
'''

'''
Borrado de registros
'''

conn = psycopg2.connect("dbname=Sesion_17 user=SciData_CDD_Py password=abcde host=localhost")
cur = conn.cursor()
cur.execute("DELETE FROM alcaldias WHERE description LIKE 'Xochimilco'")
cur.close()
conn.commit()
conn.close()

#%%
'''
Insertado de registros
'''

conn = psycopg2.connect("dbname=Sesion_17 user=SciData_CDD_Py password=abcde host=localhost")
cur = conn.cursor()
cur.execute("INSERT INTO alcaldias VALUES (16,'Xochimilco')")
cur.close()
conn.commit()
conn.close()

#%%
'''
PROCESAMIENTO DE DATOS UTILIZANDO AMBOS LENGUAJES
'''

conn = psycopg2.connect("dbname=Sesion_17 user=SciData_CDD_Py password=abcde host=localhost")

def lectura(tabla):
    return pd.read_sql(f"SELECT * FROM {tabla}",con = conn)

alcaldias = lectura("alcaldias")

nombres_tablas = ["airbnb_cdmx","alcaldias","tipo_habitacion","tipo_propiedad"]

bd = [lectura(x) for x in nombres_tablas]

conn.close()

bd[0].columns

airbnb = bd[0].join(bd[1].set_index(["neighbourhood"]), on = ["neighbourhood"],how = "inner")

airbnb.columns

set(airbnb["description"])

airbnb.rename(columns={"description":"alcaldia_descripcion"},inplace = True) 
airbnb.columns

bd[2].columns

airbnb = airbnb.join(bd[2].set_index(["tipo_habitacion"]), on = ["room_type"], how = "inner")
airbnb.rename(columns={"descripcion":"tipo_habitacion_descripcion"},inplace = True) 
airbnb.columns

bd[3].columns

airbnb = airbnb.join(bd[3].set_index(["tipo_de_propiedad"]), on = ["property_type"], how = "inner")
airbnb.rename(columns={"descripcion":"tipo_propiedad_descripcion"},inplace = True) 
airbnb.columns

airbnb["descripcion_extendida"] = "The airbnb id "+airbnb["id"].astype(str)+" is in " \
                                    + airbnb["alcaldia_descripcion"] \
                                    + ". It is a " + airbnb["tipo_propiedad_descripcion"] \
                                    + " of type room " + airbnb["tipo_habitacion_descripcion"]

tabla_descrp = airbnb[["id","descripcion_extendida"]]

#%%
'''
CREACIÓN Y LLENADO DE TABLAS
'''

conn = psycopg2.connect("dbname=Sesion_17 user=SciData_CDD_Py password=abcde host=localhost")

cur = conn.cursor()
cur.execute("CREATE TABLE mi_tabla(id varchar,descripcion text)")
cur.close()
conn.commit()
conn.close()

#%%

nom_tabla = "mi_tabla"# nombre de la tabla que se va a llenar

#engine = create_engine("postgresql+psycopg2://SciData_CDD_Py:abcde@localhost:5432/Sesion_17")


tabla_descrp.head(0).to_sql(nom_tabla, engine, if_exists='replace',index=False) 

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()

tabla_descrp.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()

cur.copy_from(output, nom_tabla, null="") # null values become ''
conn.commit()

cur.close()
conn.close()

