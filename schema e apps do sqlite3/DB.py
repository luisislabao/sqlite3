import sqlite3

con = sqlite3.connect("CandyCakes_DB.db", check_same_thread=False)
cursor = con.cursor()

    
def menu(o = 0, id = 0, objeto = {}):
    if o ==1:
        cursor.execute("DROP TABLE products")
        con.commit()
        
        cursor.execute("""CREATE TABLE "products" (
	        "id"	INTEGER NOT NULL DEFAULT 1 UNIQUE,
	        "name"	TEXT,
	        "type"	TEXT,
	        "price"	REAL,
	        "qnt"	INTEGER,
	        PRIMARY KEY("id" AUTOINCREMENT)
            );""")
        con.commit()

        for propriedade in objeto:
            for registro in objeto[propriedade]:
               cursor.execute(f"INSERT INTO products (name, type, price, qnt) VALUES ('{registro['nome']}', '{registro['tipo']}','{registro['price']}','{registro['quantidade']}')")
        con.commit()
        


    #Select all from 
    elif o == 2:
        iten = cursor.execute("SELECT * from products")
        cruds = []
        for row, element in  enumerate(iten):
            cruds.append(element)
        return cruds


    #Exclui linha de dados
    elif o == 3:
        cursor.execute(f"DELETE FROM Products WHERE ID LIKE {id}")
        con.commit()
        print(id)

    elif o ==4:
        cursor.execute("DROP TABLE [IF EXISTS] cesta")
        con.commit()
        
        cursor.execute("""CREATE TABLE "cesta" (
	        "id"	INTEGER NOT NULL DEFAULT 1 UNIQUE,
	        "name"	TEXT,
	        "type"	TEXT,
	        "price"	REAL,
	        "qnt"	INTEGER,
	        PRIMARY KEY("id" AUTOINCREMENT)
            );""")
        con.commit()

        for propriedade in objeto:
            cursor.execute(f"INSERT INTO products (name, type, price, qnt) VALUES ('{registro['nome']}', '{registro['tipo']}','{registro['price']}','{registro['quantidade']}')")
        con.commit()
        

    # Close the DATABASE
    # elif o == 5:
    #     con.close()
    

        
# VIDEO AULA https://youtu.be/YihFOnFCMI4?t=816