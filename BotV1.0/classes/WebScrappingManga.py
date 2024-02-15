from zenrows import ZenRowsClient

class WebScappingManga:
    def repeat(caractere, qtde):
        #fiz isso pra usar como uma função pra usar específicamente pra texto, pra outros fiz é só
        #tirar aql return '' e colocar um return None
        if(qtde < 0):
            raise ValueError("repeat method not accept negative numbers")

        if(qtde == 0):
            return ''

        if(qtde > 1):
            return(caractere + WebScappingManga.repeat(caractere, qtde -1))
        else:
            return(caractere)
    
    def Scrapping(url: str, ms: str):
        client = ZenRowsClient("962b93503306712ef3dd5d4ad6fb67547171d073")
        params = {
            "js_render":"true",
            }
        response = client.get(url, params=params)
        num = response.text[response.text.index("select-paged"): response.text.index("haptertags") - 103]
        num = num.split("/")
        numPag = int(num[len(num) - 1])

        listaLinks = []
        for i in range(numPag-2):
            params = {
            "js_render":"true",
            "js_instructions": "[{\"click\":\".ts-main-image\"}" + WebScappingManga.repeat(", {\"wait\": "+ms+"}, {\"click\":\".ts-main-image\"}", i)+"]",
            }
            response = client.get(url, params=params)
            a = response.text.index("ts-main-image")
            b = response.text.index("data-server") - 2
            c = response.text[a : b]
            Link = c.split('src="')
            listaLinks.append(Link[1])

        return listaLinks