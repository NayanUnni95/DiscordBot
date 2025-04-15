import discord
from discord import app_commands
from discord.ext.commands import Cog

url = "https://images.unsplash.com/photo-1743656619958-68d85790bdb4?q=80&w=1530&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
thumbnail = "https://images.unsplash.com/photo-1743077318835-cfd9c273b450?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"


class Button(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Button 1", style=discord.ButtonStyle.green)
    async def button_one_callback(self, interaction: discord.Integration, button):
        self.value = "Button 1 Clicked"
        await interaction.response.send_message(self.value)

    @discord.ui.button(label="Button 2", style=discord.ButtonStyle.green)
    async def button_two_callback(self, interaction: discord.Integration, button):
        self.value = "Button 2 Clicked"
        await interaction.response.send_message(self.value)


class Modal(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)
        self.add_item(
            discord.ui.TextInput(
                label="Your Response", placeholder="Enter something here"
            )
        )

    async def on_submit(self, interaction: discord.Integration):
        await interaction.response.send_message(f"You said {self.children[0].value}")


class UICog(Cog):
    def init(self, bot):
        self.bot = bot

    @app_commands.command(name="embed", description="React as a Embed")
    async def embed(self, interaction: discord.Integration, name: str, age: int = None):
        embed = discord.Embed(
            title="embed",
            description=f"Hello {name}, is you {age} years old!",
            color=discord.Colour.blue(),
        )
        embed.set_image(url=url)
        embed.set_thumbnail(url=thumbnail)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="button", description="button ui test")
    async def button(self, interaction: discord.Integration):
        btnView = Button()
        await interaction.response.send_message(view=btnView)

    @app_commands.command(name="modal", description="modal ui test")
    async def modal(self, interaction: discord.Integration):
        modal = Modal(title="Enter your response")
        await interaction.response.send_modal(modal)


async def setup(bot):
    await bot.add_cog(UICog(bot))
