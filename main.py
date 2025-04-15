import discord
import decouple
from discord.ext import commands

token = decouple.config("DISCORD_TOKEN")

bot = commands.Bot(
    command_prefix="/",
    intents=discord.Intents.all(),
    case_insensitive=True,
    self_bot=True,
)


@bot.event
async def on_ready():
    print("Bot is ready to use!")
    await bot.load_extension("cogs.common")
    await bot.load_extension("cogs.level")
    await bot.load_extension("cogs.ui")
    await bot.tree.sync()


bot.run(token)
