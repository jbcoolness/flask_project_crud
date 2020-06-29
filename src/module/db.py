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

