import os
import steam_api
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv(".env")
token = os.getenv("DISCORD_TOKEN")

# Class that pulls in the discord client, essentially how the bot actually runs

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
        
        if message.content.startswith('benzos'):
            await message.channel.send(f' YOOOOOO Shhhhhhhhh, i got some perkies but keep it on the low... :3') 

intents = discord.Intents.default()                # this is required to specify what the bot can do
intents.message_content = True
client = Client(command_prefix='!', intents=intents)
GUILD_ID = discord.Object(id=1277759001123360800)

@client.tree.command(name="hello",description="Says hello to the user", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi There!")

@client.tree.command(name="printer",description="I print whatever is given to me", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

client.run(token)            