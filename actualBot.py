from __future__ import unicode_literals
import os
import random
from dotenv import load_dotenv
import youtube_dl
from discord.utils import get
from discord import FFmpegPCMAudio, File
import time
from selenium import webdriver
import smtplib, ssl
import urllib.request


port = 465  # For SSL



driver = webdriver.Chrome()


# 1
from discord.ext import commands
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
import requests




# 2
bot = commands.Bot(command_prefix='!')

def get_page(url):
    driver.get(url)
    return driver.page_source
    

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(pass_context=True)
async def insta(ctx, url):
    #r = requests.get(url) instagram poopie need to use selenium
    r = get_page(url)
    index = r.find("video_url")
    
    print(r)
    
    if index == -1:
        print("I crapped my pants.")
        return
    
    #probably a better way to do this but i dont care
    lastindex = index + 12
    while r[lastindex] != '\"':
        lastindex += 1
    
    
    video_url = r[index + 12:lastindex]
    print(video_url)
    video_url = video_url.replace("\\u0026", "&")
    print(video_url)
    
    channel = bot.get_channel(410967350494625805)
    filename = str(random.randint(1,1000000))
    urllib.request.urlretrieve(video_url, filename + ".mp4") 
    attach =  discord.File(filename + ".mp4")
    await channel.send(file=attach)
    
    
    
bot.run(TOKEN)



    