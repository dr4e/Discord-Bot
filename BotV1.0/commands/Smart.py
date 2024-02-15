from discord.ext import commands

#Trabalhando com Operações Matemáticas
class Smart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Calcular Expressão
    @commands.command(name="calcular", help="Calcular uma expressão Matemática -- Expressão")
    async def Calcular(self, ctx, *expressao):
        expressao = "".join(expressao) #Transforma Tupla em uma unica string
        await ctx.channel.send(eval(expressao))
    #------
        
async def setup(bot):
    await bot.add_cog(Smart(bot))