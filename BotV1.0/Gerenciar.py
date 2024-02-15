from discord.ext import commands

class Gerenciar(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logado como {self.bot.user}")

async def setup(bot):
    await bot.add_cog(Gerenciar(bot))
