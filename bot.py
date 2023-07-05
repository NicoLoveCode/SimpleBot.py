import discord
from discord.ext import commands
from discord import Option

#This isn't an actual bot, its just code for a bot. you'll have to make your own bot user and put the token here, and it'll run this code on your bot user.
#You also need to keep this on at all times if you want the bot to always respond.
#Or you could of course use heroku, which is free.

#These are the variables you need to configure.
token = 'token here'
messagemaxlength = 100
logdeletedmessages = False
logeditedmessages = False

bot = commands.Bot()

#list of my own personally made roasts.
#you can use them however you want this is open source
roasts = [
    'you sound like you eat hotdogs with mayo',
    'youre more obselete than the ueue in queue',
    'youre so trash you probably have a wife and kids and are a millionare',
    'you are the kinda guy to go on about how eating burgers is healthy due to its nutrients',
    'the new minecraft block limit is less distance from your ego to your iq',
    'im sure you know about rolling down in the deep iq levels',
    'im sure neither of your parents were there when you were born',
    'did you kill both of your parents by them looking at your ugly ass face?'
]

#I'm pretty sure this is against discords ToS so I disabled it.

#@bot.slash_command()
#@commands.has_permissions(manage_messages=True)
#async def mouth(ctx, word):
#    await ctx.respond(word)

@bot.slash_command(name = "unmute", description = "unmute any muted members")
@commands.has_permissions(manage_messages = True)
async def unmute(ctx, member: discord.Member):
    permDisR = discord.utils.get(ctx.guild.roles, name = 'Muted')
    await member.remove_roles(permDisR)
    await ctx.respond('Unmuted.')

@bot.slash_command(name = "mute", description = "mute any member")
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member: discord.Member):
    permDisR = discord.utils.get(ctx.guild.roles, name = 'Muted')
    if not permDisR:
        permDisR = await ctx.guild.create_role(name = 'Muted')
        for channel in ctx.guild.channels:
            await channel.set_permissions(permDisR, speak=False, send_messages=False)

    await member.add_roles(permDisR)
    await ctx.respond('Muted.')

@mute.error
async def permserror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        ctx.respond('Sorry! You dont have permission.')



@bot.slash_command(name = 'unban', description = 'unban any banned members')
@commands.has_permissions(ban_members = True)
async def unban(ctx, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.respond(f"{user} has been unbanned.")

@unban.error
async def permserror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        ctx.respond('Sorry! You dont have permission.')

@bot.slash_command(name = 'ban', descirption = 'ban any member')
@commands.has_permissions(ban_members = True)
async def ban(ctx, user:discord.Member, *, reason = None):
    if reason == None:
        reason == 'no reason'
    await user.ban(reason=reason)
    try:
        await user.send(f"You have been banned in {ctx.guild} for {reason}")
    except:
        return
    await ctx.respond(f"{user} has been banned.")

@ban.error
async def permserror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        ctx.respond('Sorry! You dont have permission.')

@bot.slash_command(name = 'kick' , description = 'kick any member')
@commands.has_permissions(kick_members = True)
async def warn(ctx, user:discord.Member, *, reason = None):
    if reason == None:
        reason = 'no reason'
    await ctx.respond(f'{user}! you have been warned! reason: {reason}')

@warn.error
async def permserror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        ctx.respond('Sorry! You dont have permission.')



@bot.event
async def on_message(message):
    if message.author != bot.user:
        print(f'(#{message.channel}) {message.author}: {message.content}')
        if len(message.clean_content) >= messagemaxlength:
            await message.delete()
            await message.channel.send(f'Sorry! your message must be under {messagemaxlength} characters.')

@bot.event
async def on_message_delete(message):
    if logdeletedmessages == True:
        print(f'User {message.author} has deleted "{message.content}"')
    else:
        return

@bot.event
async def on_message_edit(before, after):
    if logeditedmessages == True:
        print(f'User {before.author} has edited "{before.content}" to "{after.content}"')
    else:
        return

@bot.event
async def on_ready():
    print(f'Client ready as {bot.user}')

bot.run(token)
