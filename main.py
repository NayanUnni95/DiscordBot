import discord
import decouple
from discord.ext import commands

token = decouple.config("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all(), case_insensitive=True, self_bot=True)

bot.run(token)
