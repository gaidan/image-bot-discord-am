import random
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

imagelist = []
client = discord.Client()

#with open("image_list.txt", "r") as f:
#    content = f.readlines()

#imagelist = [x.strip() for x in content]

#imgsrclist = ["image_list2", "image_list3.txt"]

#imgsrclist = ["image_list3.txt", "image_list2", "image_list4.txt", "image_list5.txt"]

imgsrclist = ["mainimages"]

for i in imgsrclist:
    with open(i, "r") as f:
        content = f.readlines()
    for x in content:
        imagelist.append(x.strip())

@client.event
async def on_message(message):
    global imagelist
    #with open("image_list.txt", "r") as f:
    #    content = f.readlines()
    #imagelist = [x.strip() for x in content]
    #for i in imgsrclist:
    #    with open(i, "r") as f:
    #        content = f.readlines()
    #    for x in content:
    #        imagelist.append(x.strip())
    if message.author == client.user:
        return
    if message.content == "!image":
        response = random.choice(imagelist)
        await message.channel.send(response)
    print(message.content, message.author)

client.run(TOKEN)
