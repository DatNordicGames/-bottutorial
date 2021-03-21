import discord 
import os
import requests
import json
from replit import db

client = discord.Client()

@client.event
async def on_ready():
    print("done")

@client.event
async def on_message(message):
    while True:
      await message.channel.send("XD")
      print("XDone")


    
  
client.run(os.getenv('TOKEN'))


