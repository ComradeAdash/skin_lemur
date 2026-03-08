
import os
import steam_api
import discord
from dotenv import load_dotenv

load_dotenv(".env")
token = os.getenv("DISCORD_TOKEN")

# Class that pulls in the discord client, essentially how the bot actually runs

class Client(discord.Client):
    async def on_ready(self):                       # this will run when the bot has connected to the server
        print(f'We have logged in as {self.user}')

intents = discord.Intents.default()                # this is required to specify what the bot can do, in this case we want it to be able to read messages
intents.message_content = True

client = Client(intents=intents)      
client.run(token)            