from dotenv import load_dotenv
import os
from brave_api import brave_request
import json 
import gpt

import discord
from discord.ext import commands
import openai
import requests
from gpt import openai_request
from gpt import openai_Find_Intention

# Définissez les intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Initialisez le bot avec le nouveau préfixe '/'
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():   
    print(f'Connecté en tant que {bot.user}')

# Event on /bot 
@bot.command(name='bot')
async def qwery_command(ctx, *, query: str):
    try:
        async with ctx.typing():  # Indique que le bot est en train de "taper"
            AnswerOrRag = openai_Find_Intention(query) 
            if AnswerOrRag != 'RAG':
                braveResult = brave_request(query)
                response = openai_request(query, braveResult)
            else:
                response = AnswerOrRag
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Une erreur est survenue : {e}")

bot.run(os.environ.get("discord_key"))
