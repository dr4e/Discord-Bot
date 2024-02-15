from discord.ext import commands
from classes.BancoDeDados import BancoDeDados

#Trabalhando com Videos
class Video(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Videos Rapaziada
    @commands.command(name="videos", help="Alguns Videozinhos da Rapaziada ;) -- 1-∞")
    async def VideosRapaziada(self, ctx, ID):
        response = BancoDeDados.Consultar("Videos", ID)
        if response:
            await ctx.channel.send(response)
        else:
            await ctx.channel.send(f"Até agora so temos {BancoDeDados.ConsultarTamanhoTabela("Videos")} Videos, use $adicionarvideo caso queira adicionar")
    
    @commands.command(name="adicionarvideo", help="Adicione um video da Rapaziada -- Link Discord")
    async def AdicionarVideo(self, ctx, Link):
        SplitLink = Link.split("?")
        
        try:
            SplitLink[1]
        except:
            await ctx.channel.send("Insira um Video Valido Por Favor, Lembrando que deve ser um Link do tipo discord")
            return

        if len(SplitLink[1]) != 92 or len(Link) < 100:
            await ctx.channel.send("Insira um Video Valido Por Favor, Lembrando que deve ser um Link do tipo discord")
            return
        
        response = BancoDeDados.Inserir("Videos", Link)
        if response:
            await ctx.channel.send("Video Adicionado com Sucesso")
        else:
            await ctx.channel.send("Houve um Erro")
    #-------

async def setup(bot):
    await bot.add_cog(Video(bot))