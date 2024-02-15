import os
from discord.ext import commands
import discord
import asyncio
from decouple import config

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot('$', intents=intents, case_insensitive=True)
TOKEN = config("SECRET_TOKEN")

async def loadCogs(bot):
    await bot.load_extension("Gerenciar")   
    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f"commands.{cog}")

async def main():
    async with bot:
        await loadCogs(bot)
        await bot.start(TOKEN)

asyncio.run(main())