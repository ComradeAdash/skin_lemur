import steam_skins
import discord
import weapon_skin
from discord.ext import commands
from discord import app_commands

theSkin = weapon_skin.Weapon_skin()

class Client(commands.Bot):
    async def on_ready(self):                      # when the bot has connected to the server
        print(f'We have logged in as {self.user}')

        try:
            guild = discord.Object(id=1277759001123360800)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guld {guild.id}.')
        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):           #  when a message is sent in the server
        if message.author == self.user:
            return                                 # the bot shouldn't respond to itself
        
        if message.content.startswith('meow'):
            await message.channel.send(f'MEOW') 

intents = discord.Intents.default()                # this is required to specify what the bot can do
intents.message_content = True
client = Client(command_prefix='!', intents=intents)
GUILD_ID = discord.Object(id=1277759001123360800)

@client.tree.command(name="hello",description="Says hello to the user", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi There!")

@client.tree.command(name="printer",description="I print whatever is given to me", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.defer()

    result = theSkin.search_skin(printer)
    if result:
        skin_name = result
        data = steam_skins.fetch_request(skin_name, steam_skins.parameters)
        await interaction.followup.send(str(data))
    else:
        await interaction.followup.send("Skin not found or invalid query.")