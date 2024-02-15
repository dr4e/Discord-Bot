from classes.SQLConnector import connection

class BancoDeDados:
    def Consultar(tabela, ID, campo="Link"):
        try:
            query = f"SELECT {campo} FROM {tabela} WHERE ID = {ID}"
            cursor = connection.cursor()
            cursor.execute(query)
            Link = cursor.fetchall()
            return Link[0][0]
        except: return False
        
    def ConsultarTamanhoTabela(tabela):
        query = "SELECT * FROM %s" % tabela
        cursor = connection.cursor()
        cursor.execute(query)
        Link = cursor.fetchall()
        return len(Link)
    
    def Inserir(tabela, valor, campo="Link"):
        try:
            query = f"INSERT INTO {tabela} ({campo}) VALUES ('{valor}')"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            return True
        except: return False    