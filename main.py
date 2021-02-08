import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_ID = int(os.getenv('BOT_ID'))

class BotClient(discord.Client):

    async def on_message(self, message):
        if(message.author.id != BOT_ID):
            self.channel = message.channel
            await self.reply_on_request('123')

    async def reply_on_request(self, message):
        await self.channel.send(message)

client = BotClient()
client.run(TOKEN)