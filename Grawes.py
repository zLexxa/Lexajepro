import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hi and Welcome to Grawes Server! We hope you enjoy and stay!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready Freddy') 


@client.event
async def on_message(message):
    if message.content == '!ban':
        await client.send_message(message.channel,'')
    if message.content == '!ban':
        await client.send_message(message.channel,'ban user')
        
client.run('NTM3Mzg2NTgwMjUyNDI2MjUw.DynePg.petSDDnyqEg4NmLCFDU8SF_eLrk')
