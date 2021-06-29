# Import statements for environment variables, Discord, Replit databases, and UpTimeRobot
import os
import discord
import random
from replit import db
from yappy_mutt import yap

client = discord.Client()

def get_quote():
  if "quotes" in db.keys():
    quotes = db["quotes"]
    return quotes[random.randrange(len(quotes))]

def add_quotes(new_quote):
  if "quotes" in db.keys():
    quotes = db["quotes"]
    quotes.append(new_quote)
    db["quotes"] = quotes
  else:
    db["quotes"] = [new_quote]

def reset():
  if "quotes" in db.keys():
    del db["quotes"]

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$hitme"):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith("$add"):
    quote = message.content.split("$add ", 1)[1]
    add_quotes(quote)
    #await message.channel.send("New quote added.")
  
  if message.content.startswith("$reset"):
    reset()
    await message.channel.send("All quotes reset.")

run = os.environ['spot bot key']
yap()
client.run(run)