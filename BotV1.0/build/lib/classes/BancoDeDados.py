from SQLConnector import connection

class BancoDeDados:
    def Consultar(tabela, ID, campo="Link"):
        try:
            query = f"SELECT {campo} FROM {tabela} WHERE ID = {ID}"
            cursor = connection.cursor()
            cursor.execute(query)
            Link = cursor.fetchall()
            return Link[0][0]
        except:
            query = "SELECT * FROM %s" % tabela
            cursor = connection.cursor()
            cursor.execute(query)
            Link = cursor.fetchall()
            return f"Até agora só temos {len(Link)} {tabela}, mas considere adicionar usando nossos Comandos de Adicionar, mais informações $help ;)"
        
    def Inserir(tabela, valor, campo="Link"):
        query = f"INSERT INTO {tabela} ({campo}) VALUES ('{valor}')"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return f"{valor} foi adicionado com sucesso"