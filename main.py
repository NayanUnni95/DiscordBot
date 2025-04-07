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
    await bot.tree.sync()


@bot.tree.command(name="ping", description="Check is the bot online")
async def ping(interaction):
    await interaction.response.send_message("Pong!", ephemeral=True, delete_after=5)


bot.run(token)
