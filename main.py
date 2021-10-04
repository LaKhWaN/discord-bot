# auto voice channel arranger
# email bot

import discord
import random
from discord import guild
from discord.ext import commands

client = commands.Bot(command_prefix=";")
LOBBY_VC_ID = 891717223549403250
# GAMING_VC_ID = discord.VoiceChannel()
# GAMING_VC_ID.id = 891717223549403252
@client.event
async def on_ready():
    print("Bot is online.")

@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(LOBBY_VC_ID)
    members = channel.members
    memids = [member.id for member in members]
    if len(memids) == 2:
        channel = guild.Guild.create_voice_channel(name='anything')
        await member.move_to(channel)

@client.command()
async def test(ctx):
    print(ctx.guild.voice_channels)

# @client.command()
# async def prathmesh(ctx):
#     await ctx.send("Prathmesh nub")

# @client.command()
# async def rolldice(ctx):
#     options = [i for i in range(1,7)]
#     await ctx.send(f"Die rolled, and die landed with {random.choice(options)} facing.")

# @client.command(aliases=['clear','purge'])
# async def _clear(ctx,amount=5):
#     await ctx.channel.purge(limit=amount+1)

# @client.command()
# async def kick(ctx,member: discord.Member,*,reason=None):
#     await ctx.send(f"{ctx.message.author.name} has kicked {member.nick} from the server.")
#     await member.kick(reason=reason)

# @client.event
# async def on_command_error(ctx,error):
#     await ctx.send(f"**Error:** `{error}`")




client.run("ODc5NjU2NTM4Njk0OTAxNzgw.YSS5_g.Q28uVyI-qq_iEYer4E3Q8WwMvRA")