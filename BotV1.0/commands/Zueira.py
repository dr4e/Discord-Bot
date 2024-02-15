from discord.ext import commands
import discord

#Zueira com a Rapaziada
class Zueira(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="drenio", help="Só testando pra saber")
    async def Drenio(self, ctx):
        await ctx.channel.send('eukk')
    @commands.command(name="gabriel", help="Só testando pra saber")
    async def Gabriel(self, ctx):
        await ctx.channel.send('ESSE É VIADO KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK \n https://cdn.discordapp.com/attachments/1180201952919945249/1199470254498271313/a4958782-29ae-436f-aeb0-458fa64e41e7.png?ex=65c2a8b9&is=65b033b9&hm=afe6b5af8473c73fdf6c396b49e03533be6102a13735c0fd1ead43210326614b&')
    @commands.command(name="gustavo", help="Só testando pra saber")
    async def Gustavo(self, ctx):
         await ctx.channel.send("Esse é seu ADM??? \n https://cdn.discordapp.com/attachments/1074759282991575121/1198737969880776714/image.png?ex=65bffebb&is=65ad89bb&hm=f5b71212c766d0e96b2f3c94824a81d21ca47eb393db59a06a49f97b40bd4101&")
    @commands.command(name="pedrin", help="Só testando pra saber")
    async def Pedrin(self, ctx):
        await ctx.channel.send('Q POHA É ESSA ????????????????????????????????? \n https://cdn.discordapp.com/attachments/1180201952919945249/1199846711368105994/image.png?ex=65c40754&is=65b19254&hm=134aad5d5df9f3a6b6adfe7160a851669a4ca73fd84097c823bf69cf12848788& https://cdn.discordapp.com/attachments/1180201952919945249/1199846765105532988/image.png?ex=65c40760&is=65b19260&hm=66e344ae7ddb7acaa29e4968b5a260337debf340c5b2d8ef6d248b172523a266&')
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if (("OPINIÃO" and "REVOLUÇÃO" in ctx.content.upper()) or ("OPINIAO" and "REVOLUÇAO" in ctx.content.upper()) or ("OPINIAO" and "REVOLUCAO" in ctx.content.upper()) or ("OPINIÃO" and "REVOLUCÃO" in ctx.content.upper()) or ("OPINIAO" and "REVOLUCÃO" in ctx.content.upper()) or ("OPINIÃO" and "REVOLUCAO" in ctx.content.upper()) or ("OPINIAO" and "REVOLUÇÃO" in ctx.content.upper()) or ("OPINIÃO" and "REVOLUÇAO" in ctx.content.upper())) and ctx.author.name == "bito132":
            await ctx.channel.send("VAI SE FUDER BITO")
        #if ctx.content.startswith("$wa") and ctx.author.name == "trylater":
            #await ctx.channel.send("OWWNO ROUBARAM MINHA WAIFU😭 😭 😭")          
            
async def setup(bot):
    await bot.add_cog(Zueira(bot))