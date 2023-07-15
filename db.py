import sqlite3

class Db:
    def __init__(self) -> None:
        self.conn = sqlite3.Connection("db.db")
        self.cur = self.conn.cursor()
        self.create()
        
        
    def create(self):
        try:
            self.cur.execute("""
                             CREATE TABLE IF NOT EXISTS Items_Shop(
                                 id_object INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name VARCHAR(200), 
                                 description TEXT,
                                 price INT,
                                 level_shop INT,
                                 image varchar(500))""")
            self.conn.commit()
        except Exception as e:
            print(str(e))
            
    def init_thread(self):
        conn = sqlite3.Connection("db.db")
        cur = conn.cursor()
        return conn, cur
    

        
    def table_info(self, table: str, cur):
        cur.execute(f"PRAGMA table_info({table})")
        columnas = cur.fetchall()
        columnas.pop(0)
        columnas_str = ', '.join([columna[1] for columna in columnas])
        print(columnas_str)
        placeholders = ', '.join(['?' for _ in columnas]) 
        print(placeholders)
        return columnas_str, placeholders
    
    def insert(self, table: str, values):
        conn, cur = self.init_thread()
        columnas, placeholders = self.table_info(table, cur)
        query = f"INSERT INTO {table} ({columnas}) VALUES ({placeholders})"
        cur.execute(query, values)
        conn.commit()
        conn.close()
        
    def insert_many(self, table: str, values):
        columnas, placeholders = self.table_info(table)
        placeholders = ', '.join(['?' for _ in range(len(values[0]))])  # Crear los placeholders para los valores
        query = f"INSERT INTO {table} ({columnas}) VALUES (null,{placeholders})"
        self.cur.execute(query, values)
        self.conn.commit()
    
    def select_all(self, table):
        conn, cur = self.init_thread()
        query = f"SELECT * FROM {table}"
        cur.execute(query)
        datas = cur.fetchall()
        conn.close()
        return datas
    
if __name__ == "__main__":
    data = Db()
    columnas, holders = data.table_info("Items_Shop")
    print(columnas)