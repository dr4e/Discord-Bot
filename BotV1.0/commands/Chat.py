from discord.ext import commands
from classes.Torneio import Torneio
from classes.WebScrappingAttribute import WebScrappingAttribute
import discord

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="torneio", help="Crie um Torneio com Chaveamento Aleatório -- Nomes")
    async def CriarTorneio(self, ctx, *participantes):
        participantes = list(participantes)
        torneio = Torneio(participantes)
        description = torneio.chaveamento()

        embed = discord.Embed(title='Torneio', description=description, colour=discord.Colour.gold())
        await ctx.channel.send(embed=embed)

    @commands.command(name="carregarvideoifunny", help="Carregue um Video Ifunny pra mandar pra rapaziada -- Link")
    async def CarregarVideoIfunny(self, ctx, link):
        if not "video" in link:
            await ctx.channel.send("Coloque um Video Por Favor ;)")
            return

        web = WebScrappingAttribute()
        await ctx.channel.send(web.getAttributeByXPATH(link, "/html/head/meta[16]", "content"))
async def setup(bot):
    await bot.add_cog(Chat(bot))