import discord
from discord.ext import commands
from models.bot import Assistant
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

command_prefix = "$"
intents = discord.Intents.default()

turn_on = ["dm_messages", "guild_messages", "message_content"]
for permission in turn_on:
    setattr(intents, permission, True)

bot = Assistant(
    command_prefix=command_prefix,
    intents=intents,
    token=os.environ["BOT_TOKEN"]
)

if __name__ == "__main__":
    asyncio.run(bot.main())