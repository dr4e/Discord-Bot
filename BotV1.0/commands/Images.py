import discord
import cv2
import numpy as np
import requests 
import os
from discord.ext import commands
from classes.BancoDeDados import BancoDeDados
from zenrows import ZenRowsClient
from classes.Torneio import repeat_c

#Trabalhando com Images
class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Memes Gabriel
    @commands.command(name="gabrielmemes", help="Alguns Memes relacionados ao nosso mano -- 1-∞")
    async def MemesGabriel(self, ctx, ID):
        response = BancoDeDados.Consultar("BielleonMemes", ID)
        if response:
            await ctx.channel.send(response)
        else:
            await ctx.channel.send(f"Até agora só temos {BancoDeDados.ConsultarTamanhoTabela("BielleonMemes")} Memes, use $adicionarmemegabriel caso queira adiciomar.")
    
    @commands.command(name="adicionarmemegabriel", help="Adicione um meme do Bielleon -- Link Discord")
    async def AdicionarMemeGabriel(self, ctx, Link):
        try:
            request = requests.get(Link)
        except:
            await ctx.channel.send("Insira Valor Valido Por Favor")
            return
        if request.status_code != 200:
            await ctx.channel.send("Insira um Link Valido Por Favor")
            return
        
        response = BancoDeDados.Inserir("BielleonMemes", Link)
        if response:
            await ctx.channel.send("Meme Adicionado com Sucesso")
        else:
            await ctx.channel.send("Houve um Erro")
    #---------
    
    #Fotos Rapaziada
    @commands.command(name="fotos", help="Algumas fotos da Rapaziada ;) -- 1-∞")
    async def FotosRapaziada(self, ctx, ID):
        response = BancoDeDados.Consultar("ImagesRapaziada", ID)
        if response:
            await ctx.channel.send(response)
        else:
            await ctx.channel.send(f"Até agora só temos {BancoDeDados.ConsultarTamanhoTabela("ImagesRapaziada")} Imagens da Rapazida, use $adicionarfoto caso queira adicionar uma foto.")

    @commands.command(name="adicionarfoto", help="Adicione uma Foto da Rapaziada -- Link Discord")
    async def AdicionarFoto(self, ctx, Link):
        SplitLink = Link.split("?")
        
        try: 
            request = requests.get(Link)
            SplitLink[1]
        except:
            await ctx.channel.send("Insira uma Imagem Valida Por Favor, Lembrando que deve ser um Link do tipo discord")
            return

        if len(SplitLink[1]) != 92:
            await ctx.channel.send("Insira uma Imagem Valida Por Favor, Lembrando que deve ser um Link do tipo discord")
            return
        
        if request.status_code != 200:
            await ctx.channel.send("Insira um Link Valido Por Favor")
            return
        
        response = BancoDeDados.Inserir("ImagesRapaziada", Link)
        if response:
            await ctx.channel.send("Imagem Adicionada com Sucesso")
        else:
            await ctx.channel.send("Houve um Erro")
    #---------

    #Imagem em Desenho
    @commands.command(name="desenho", help="Transforme sua Imagem em Desenho! -- Img(link) e Qtd Filtro")
    async def Desenhar(self, ctx, url, qtdFiltro = 95):
        try:
            qtdFiltro = int(qtdFiltro)
        except:
            await ctx.channel.send("Selecione um Filtro Valido Por Favor ;)")
            return
        
        if qtdFiltro%10 == 0:
            qtdFiltro+=1

        if url.isdigit():
            id = url
            url = BancoDeDados.Consultar("ImagesRapaziada", id)
        try:     
            req = requests.get(url)
            arr = np.asarray(bytearray(req.content), dtype=np.uint8)
            img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)
            imgInvertida = cv2.bitwise_not(img)
            imgBlur = cv2.GaussianBlur(imgInvertida, (qtdFiltro , qtdFiltro), 0)
            imgBlurInvertida = cv2.bitwise_not(imgBlur)
            desenho = cv2.divide(img, imgBlurInvertida, scale=256.0)
            cv2.imwrite("desenho.jpg", desenho)
            
            await ctx.send(url)
            await ctx.send(file=discord.File(r"C:\Users\andre\OneDrive\Documentos\Projetos VSCode\Python\BotDisc\BotV1.0\desenho.jpg"))
            os.unlink(r"C:\Users\andre\OneDrive\Documentos\Projetos VSCode\Python\BotDisc\BotV1.0\desenho.jpg")
        except:
            await ctx.channel.send("Coloque um link ou número valido ;)")
    #--------
            
    #Buscar Avatar
    @commands.command(name="avatar", help="Veja o Avatar da Pessoa que Desejar ;) -- ID")
    async def avatar(self, ctx, id = None):
        if id is None:
            user = ctx.author
        else:
            user = await self.bot.fetch_user(id)
        await ctx.send(user)
        await ctx.channel.send(user.avatar)
    #--------
    @commands.command(name="manga", help="Leia Um Manga pelo discord usando um link do manga-chan! -- Link ms")
    async def Manga(self, ctx, link, ms="250"):
        try:
            client = ZenRowsClient("151f0a4782ad413c487f149cbcb3786793c8619d")
            params = {
                "js_render":"true",
                }
            response = client.get(link, params=params)
            num = response.text[response.text.index("select-paged"): response.text.index("haptertags") - 103]
            num = num.split("/")
            numPag = int(num[len(num) - 1])
            print(numPag)
        except:
            await ctx.channel.send("Houve um Erro ao Pegar a Quantidade de Páginas")

        try:
            for i in range(numPag-1):
                params = {
                "js_render":"true",
                "js_instructions": "[{\"click\":\".ts-main-image\"}" + repeat_c(", {\"wait\": "+ms+"}, {\"click\":\".ts-main-image\"}", i)+"]",
                }
                response = client.get(link, params=params)
                a = response.text.index("ts-main-image")
                b = response.text.index("data-server") - 2
                c = response.text[a : b]
                Link = c.split('src="')
                print(Link[1])
                await ctx.channel.send(Link[1])
        except:
            await ctx.channel.send("Houve um Erro")
        await ctx.channel.send("Câbo")

async def setup(bot):
    await bot.add_cog(Images(bot))