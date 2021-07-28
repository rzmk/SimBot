import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")

intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} is online.')
    await client.change_presence(activity=discord.Streaming(name="SimBot!", url="https://www.twitch.tv/bh4tti"))
    

@client.event
async def on_member_update(before, after):
    if [i.id for i in before.roles].count(855615839537594400):
        if not [i.id for i in after.roles].count(855615839537594400):
            colors = {
                "white1": 849391461127553024,
                "black": 849391477191606282,
                "charcoal": 849391474960629811,
                "blue": 849404913950785536,
                "dark_orange": 849391480002707476,
                "royal_purple": 849391482636468264,
                "rose": 849391485061562399,
                "hot_pink": 849391487745916930,
                "white2": 849391491138846750,
                "dark_purple": 849391493697110046,
                "beige": 849391497329246298,
                "lemon": 849391500559515708,
                "red": 849391503041757204,
                "maroon": 849391504891052062,
                "pink": 849391506548195398,
                "lime": 849391507932708925,
                "green": 849391514169114665,
                "gold": 849391516317122600,
                "orange": 849391510114140190,
                "midnight": 849391512214437888,
                "baby_blue": 849391519945064488,
            }
            for color in colors.values():
                try:
                    role = discord.utils.get(after.guild.roles, id=color)
                    await after.remove_roles(role)
                except:
                    print("Error!")

client.run(TOKEN)