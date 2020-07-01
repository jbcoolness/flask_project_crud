import pymysql

class Database:
    def connect(self):
        return pymysql.connect("localhost","root","Jb_123456789","test")


    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM alumnos")
            else:
                cursor.execute("SELECT * FROM alumnos where id = %s", (id,))  

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()                  

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO alumnos(NOMBRE, APELLIDO, EMAIL, EDAD) VALUES (%s, %s, %s, %s)", (data['NOMBRE'], data['APELLIDO'], data['EMAIL'], data['EDAD'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False

        finally:
            con.close()