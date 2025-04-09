import discord
from discord import app_commands
from discord.ext.commands import Cog


class LevelCog(Cog):
    def init(self, bot):
        self.bot = bot

    @app_commands.command(name="level", description="Explore different levels details")
    async def level(self, interaction: discord.Integration):
        await interaction.response.send_message("Levels Details")


async def setup(bot):
    await bot.add_cog(LevelCog(bot))
