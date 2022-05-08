# bot.py
import os
import discord
from dotenv import load_dotenv
import json
import requests
from keepalive import keep_alive
from discord.ext import commands
import random

#this bot provides members with inspirational quotes from an API 
#this bot is hosted with replit & uptime robot
# benchmarks: 
# 1. Your bot should recognize a "help" message and reply with user instructions. --> responds to !Help
# 2. Your bot should provide at least three commands or functions. --> contains three commands
# 3. Your bot should reply promptly with an intelligent response or an informative error
# message. --> !help command or quote response
# 4. Your bot should integrate with at least one external data source that you can document 
# and
# describe. This could be a database system or API. --> quote API


load_dotenv()

TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']

#pulls API quote
def get_quote():
    URL = "https://api.quotable.io/random"
    try:
        response = requests.get(URL)
    except:
        print("Error while calling API...")
    res = json.loads(response.text)
    return res['content'] + "-" + res['author']
  

bot = commands.Bot(command_prefix='!')

@bot.command(name='Stop', help="Makes me sad by telling me to stop giving you inspiration")
async def stop(ctx):
    stop_messages = [
        'RU sure? Ur gonna wanna hear my quotes!',
        'That hurts my feelings. My quotes are cool, I promise!', 'Fine. Guess you wont be inspired today.'
    ]

    response = random.choice(stop_messages)
    await ctx.send(response)

@bot.command(name='Hello', help="Makes me happy by encouraging me to send some inspiration")
async def inspire(ctx):
    response_2 = get_quote()
    await ctx.send(response_2)

@bot.command(name='sad', help="Makes me try and help you by sending a beautiful quote!")
async def inspire(ctx):
    response_2 = get_quote()
    await ctx.send(response_2)

keep_alive()
bot.run(TOKEN)

