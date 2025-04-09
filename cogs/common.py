import discord
from discord import app_commands
from discord.ext.commands import Cog


class CommonCog(Cog):
    def init(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check is the bot online")
    async def ping(self, interaction: discord.Integration):
        await interaction.response.send_message("Pong!", ephemeral=True, delete_after=5)

    @app_commands.command(name="hi", description="say hi to the bot!")
    async def hai(self, interaction: discord.Integration):
        await interaction.response.send_message(
            f"Hello👋, {interaction.user.global_name}", delete_after=5
        )


async def setup(bot):
    await bot.add_cog(CommonCog(bot))
