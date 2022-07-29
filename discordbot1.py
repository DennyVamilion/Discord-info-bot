 #!/bin/usr/usr python3

import discord
import datetime
from discord.utils import get

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
day = datetime.datetime.now().day
year = datetime.datetime.now().year
monat = datetime.datetime.now().month

class MyClient(discord.Client):
    async def on_ready(self):
        print('ich habe mich eingelockt')

        
    async def on_message(self, message):
        #print('Nachricht von' + str(message.author) + 'enthalt' + str(message.content))
        if message.author == client.user:
            return

        
        if message.content.startswith('!Musik bot'):
            await message.channel.send('!play und der song zum skippen !skip')
            await message.author.send('!play und der song zum skippen !skip')
            
        if message.content.startswith('!Musik'):
            await message.channel.send('Ahhh Yamete Kudasai :v') 
            await message.channel.send('Danny‘s Schniedel')
            await message.channel.send('Legends never die')
            await message.channel.send('Best Gaming Music 2021 ♫ Best of EDM ♫ Trap, Bass, House, Dubstep')
            await message.channel.send('Best Music Mix 2021 ♫ Best of EDM 2021 ♫ Gaming Music Trap, Bass, Dubstep, House')
            await message.channel.send('Эвелоша')
            await message.channel.send('K NAAN - Wavin Flag Coca-Cola Celebration Mix')
            await message.channel.send('ылшз')
           # await message.channel.send
        
        if message.content.startswith('!yt'):
            await message.channel.send('https://www.youtube.com/channel/UCYM23yWHd6sqqMiz9HJc4Qw')
            
         #if message.content.startswith('!datum')
            #await message.channel.send('')
            
          
            
            
            
        




client = MyClient()
client.run('')#put ur client id in here
        
