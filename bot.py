import discord
import datetime
import random
import websweeper
HELP = """
$search (keyword) - show an image based on following keyword search

$batchsearch (keyword) (amount)- show multiple images 
"""

TOKEN = 'Discord_TOKEN_HERE'
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    #global DHAR_LOGGER
    global ACTUAL_DATE
    #DHAR_LOGGER.write(f"[{ACTUAL_DATE}]: DharMannFam has been activated \n")
    #DHAR_LOGGER.close()

@client.event
async def on_message(message):
    #global DHAR_LOGGER
    user_message = str(message.content)
    user = (message.author)

    if user_message.lower() == "$help":
        await message.channel.send(HELP)

    if "$batchsearch" in user_message.lower() and user != client.user:
        print("call")
        query = user_message.split(" ", 2)
        keyword = query[1]
        num = query[2]
        num = int(num)
        url = websweeper.find_images(keyword, num)
        for u in url:
            await message.channel.send(u)

    if "$search" in user_message.lower() and user != client.user:
        query = user_message.split(" ", 1)
        query = query[1]
        url = websweeper.find_images(query, 1)
        for u in url:
            await message.channel.send(u)


client.run(TOKEN)
