import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

command_prefix = "$"
intents = discord.Intents.default()

turn_on = ["dm_messages", "guild_messages", "message_content"]
for permission in turn_on:
    setattr(intents, permission, True)

bot = commands.Bot(
    command_prefix=command_prefix,
    intents=intents
)

@bot.event
async def on_ready():
    print(f"登入為 {bot.user}")

    print("已註冊指令")
    for cmd in bot.commands:
        print(f"\t${cmd.name}", end=" ")
    print("")

async def load_ext():
    for filename in os.listdir("./cmds"):
        await bot.load_extension(f"cmds.{filename[:-3]}")

async def main():
    discord.utils.setup_logging()
    await bot.start(os.environ["BOT_TOKEN"])

if __name__ == "__main__":
    asyncio.run(main())