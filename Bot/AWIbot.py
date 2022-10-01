import discord
import os
import random
from replit import db
from alivek import alivek

client = discord.Client()

key_words = ["meowdar"]

starter_prime = [":)"]

if "responding" not in db.keys():
  db["responding"] = True

def update_prime(looking_message):
  if "prime" in db.keys():
    prime = db["prime"]
    prime.append(looking_message)
    db["prime"] = prime
  else:
    db["prime"] = [looking_message]

def delete_primes(index):
  prime = db["prime"]
  if len(prime) > index:
    del prime[index]
  db["prime"] = prime

@client.event

async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='CYBERTRON', url='https://www.youtube.com/watch?v=-LReNkc7KUg&t=1s&ab_channel=LIEGEMAXIMO-LEGIONCOMMANDER'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  
  
  if message.content.startswith("$hello"):
    await message.channel.send("yo!")

  if msg.startswith("$prime?"):
    await message.channel.send("yes...")

  if msg.startswith("//help"):
    await message.channel.send("```Use these keywords to search for your desired anime/cartoon/movie!``` ```1.//transformers``` ```2.//ben10``` ```3.//perman``` ```4.//doreamon```")

  @commands.command(pass_context=True)
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, amount =1):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send('Context removed sir! {}'.format(ctx.author.mention), delete_after=2)
        await ctx.message.delete()
  
  if message.content.startswith("//transformers"): 
    embedVar = discord.Embed(title="Results for [Transformers]", url="https://anime-world.in/?s=transformers", color=0x00ff00)
    embedVar.add_field(name="Transformers: Rescue Bots", value="[Watch/Download :point_left:](https://anime-world.in/series/transformers-rescue-bots/)", inline=False)
    embedVar.add_field(name="Transformers: War for Cybertron", value="[Watch/Download :point_left:](https://anime-world.in/series/transformers-war-for-cybertron/)", inline=False)
    embedVar.add_field(name="Transformers Prime Beast Hunters: Predacons Rising", value="[Watch/Download :point_left:](https://anime-world.in/movies/transformers-prime-beast-hunters-predacons-rising/)", inline=False)
    embedVar.add_field(name="Transformers: Robots In Disguise", value="[Watch/Download :point_left:](https://anime-world.in/series/transformers-robots-in-disguise/)", inline=False)
    embedVar.add_field(name="Transformers: Prime", value="[Watch/Download :point_left:](https://anime-world.in/series/transformers-prime/)", inline=False)
    await message.channel.send(embed=embedVar) 
    
  


  if db["responding"]:  
   options = starter_prime
   if "prime" in db.keys():
     options = options + db["prime"]

   if any(word in msg for word in key_words):
     await message.channel.send(random.choice(options))

  if msg.startswith("$request"):
    looking_message = msg.split("$request ",1)[1]
    update_prime(looking_message)
    await message.channel.send("New request has been added.")

  if msg.startswith("$del"):
    prime = []  
    if "prime" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_primes(index)
      prime = db["prime"]
    await message.channel.send(prime)  

  if msg.startswith("$list"):
    prime = []
    if "prime" in db.keys():
      prime = db["prime"]
    await message.channel.send(prime) 

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")

    else: 
      db["responding"] = False
      await message.channel.send("Responding is off.")    

alivek()
client.run(os.getenv("token"))