import discord
from discord.ext import commands
import random
import time
import datetime
import re
import asyncio
from typing import Union
from dateutil.relativedelta import relativedelta
from discord import Color
import pyblox3
import requests
import pycountry

TOKEN = "" # your mother
intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix = "c!", intents=intents,help_command=None)
# client = discord.Client(intents=intents)

#For roze only
snipemessage = []
snipeauthor = []

editedauthor = []
beforecontent = []
aftercontent = []

# For other servers
snipemessage2 = []
snipeauthor2 = []

editedauthor2 = []
beforecontent2 = []
aftercontent2 = []

api_key = "" #get ur own api key lol
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#Roze Logs
if client.get_guild(id=732632405084471417):
    logs = client.get_channel(813511718017302578)
@client.event

async def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith("c!ping"):
    #     await message.channel.send("pong")

    if message.content.startswith("c!say") and message.author.guild_permissions.administrator:
        mes = message.content.split()
        output = ""
        for x in mes[1:]:
            output += x
            output += " "
        await message.channel.send(output)
        await message.delete()

    if message.content.startswith("c!flip"):
        roll = random.randint(1,100)
        if roll > 50:
            await message.channel.send('{}'.format(message.author.mention)+" heads")
        if roll < 50:
            await message.channel.send('{}'.format(message.author.mention)+" tails")
        if roll == 50:
            await message.channel.send('{}'.format(message.author.mention)+" It landed on its side LOL")

    if message.content.startswith("c!help"):
        embed = discord.Embed(title="__Catgirl Bot Commands__", color=Color.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/804509541186273310/812330454807609364/image0.jpg")
        embed.add_field(name="c!flip", value="Flips a standard coin")
        embed.add_field(name="c!rps", value="Play rock paper scissors with the bot!")
        embed.add_field(name="c!catgirl", value="Get a picture of a catgirl.")
        embed.add_field(name="c!av", value="Get a user's profile picture")
        embed.add_field(name="c!userinfo", value="Get all info about a user!")
        embed.add_field(name="c!serverinfo", value="Get all info about this server!")
        embed.add_field(name="c!invite", value="Invite Catgirl Bot into your server!")
        embed.add_field(name="c!snipe", value="Displays last deleted message")
        embed.add_field(name="c!editsnipe", value="Displays last edited message")
        embed.add_field(name="c!ship", value="Ships two users!")
        embed.add_field(name="c!rbxsearch", value="Shows the information of a roblox user")
        embed.add_field(name="c!weather", value="Displays the weather of a given city")
        embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
        await message.channel.send(content = None, embed=embed)

        embed2 = discord.Embed(title="__Catgirl **ADMIN** Commands__", color=Color.random())
        embed2.add_field(name="c!say", value="Makes the bot say something")
        embed2.add_field(name="c!delete", value="Deletes the previous X messages")
        embed2.add_field(name="c!dmraid", value="spams a user's dms 100 times (only envy can use)")
        embed2.add_field(name="c!tourney", value="useful for 2v2 tournaments")
        embed2.add_field(name="c!warn", value="Warns a mentioned user")
        embed2.add_field(name="c!ban", value="Bans a mentioned user")
        embed2.add_field(name="c!kick", value="Kicks a mentioned user")
        embed2.add_field(name="c!mute", value="Mutes a mentioned user")
        embed2.add_field(name="c!unmute", value="Unmutes a mentioned user")
        embed2.set_footer(text="Catgirl Bot | Developed by envy#0002")
        await message.channel.send(content=None, embed=embed2)

    if message.content.startswith("c!rps"):
        channel = message.channel
        await channel.send("Say your choice, then I'll say mine!")
        responses = [
            "rock",
            "paper",
            "scissors"
        ]
        def check(x):
            while True:
                content = x.content
                content = content.title()
                return content in ("Rock", "Paper", "Scissors")
                break
            else:
                print("")

        msg = await client.wait_for("message", check=check)
        await channel.send('{}'.format(message.author.mention)+" I pick "+random.choice(responses))

    if message.content.startswith("c!catgirl"):
        channel = message.channel
        catgirllist = [
            "https://cdn.discordapp.com/attachments/804509541186273310/812330467243720734/image0.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330467512287232/image1.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330467864215632/image2.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330468267130961/image3.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330468690231326/image4.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330454807609364/image0.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330455558914098/image2.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330455834689546/image3.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330456108105808/image4.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330456413896714/image5.png",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330456711561277/image6.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330456975540244/image7.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330457249087540/image8.jpg",
            "https://cdn.discordapp.com/attachments/804509541186273310/812330457692635177/image9.jpg",
            "https://cdn.discordapp.com/attachments/734455435494555769/812468847466512394/47e738e4fb2efa80885763961d3a9749.gif",
            "https://cdn.discordapp.com/attachments/734455435494555769/812468872229683220/630ltm088ey11.jpg",
            "https://cdn.discordapp.com/attachments/734455435494555769/812468921110102056/download.jpg",
            "https://cdn.discordapp.com/attachments/734455435494555769/812469037053247498/f94b074d9b0bb4de42de906ff99c8314.gif",
            "https://cdn.discordapp.com/attachments/734455435494555769/812469147131707432/images.jpg"
            "https://cdn.discordapp.com/attachments/734455435494555769/812469285226152007/wallpapersden.com_red-eye-anime-girl_wxl.jpg",
            "https://cdn.discordapp.com/attachments/734455435494555769/812469350387679242/368c065124d551b52e1f0cd0131ed1313f6c21e9_hq.jpg",
            "https://cdn.discordapp.com/attachments/734455435494555769/812469404423421952/965193-neko-wallpapers-1920x1080-for-windows-10_-_Copy.jpg",
            "https://cdn.discordapp.com/attachments/734455435494555769/812469463483285534/GOxjyfI.jpg",
            "https://cdn.discordapp.com/attachments/734455435494555769/812469619502874644/tumblr_pk7rg78FSm1vkdrmj_540_-_Copy.jpg"
        ]
        embed = discord.Embed(title=message.author.display_name+"'s Catgirl",color=Color.random())
        embed.set_author(name="Requested by "+message.author.name + "#" + message.author.discriminator, icon_url=message.author.avatar_url)
        embed.set_image(url = random.choice(catgirllist))
        embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
        await channel.send(content=None, embed=embed)

    if message.content.startswith("c!av"):
        if (message.mentions.__len__() > 0):
            for user in message.mentions:
                username = user.name
                discriminator = user.discriminator
                embed = discord.Embed(title="__" + username + "'s profile picture__", color=Color.random())
                embed.set_author(name=username + "#" + discriminator, icon_url=user.avatar_url)
                embed.set_image(url=user.avatar_url)
                embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
                await message.channel.send(content=None, embed=embed)
        else:
            username = message.author.name
            discriminator = message.author.discriminator
            clientProfilePicture = message.author.avatar_url
            embed = discord.Embed(title="__ Your profile picture__", color=Color.random())
            embed.set_author(name=username + "#" + discriminator, icon_url=message.author.avatar_url)
            embed.set_image(url=clientProfilePicture)
            embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
            await message.channel.send(content=None, embed=embed)

    if message.content.startswith("c!userinfo"):
        timenow = datetime.datetime.now()
        timenow = timenow - datetime.timedelta(microseconds=timenow.microsecond)
        if (message.mentions.__len__() > 0):
            for user in message.mentions:
                username = user.name
                discriminator = user.discriminator

                creationtime = user.created_at
                creationtime = creationtime - datetime.timedelta(microseconds=creationtime.microsecond)

                joineddate = user.joined_at
                joineddate = joineddate - datetime.timedelta(microseconds=joineddate.microsecond)

                avatar = user.avatar_url

                datecreated = relativedelta(timenow, creationtime)
                dcyears = str(datecreated.years)
                dcmonths = str(datecreated.months)
                dcdays = str(datecreated.days)

                datejoined = relativedelta(timenow, joineddate)
                djyears = str(datejoined.years)
                djmonths = str(datejoined.months)
                djdays = str(datejoined.days)
        else:
            author = message.author
            username = author.name
            discriminator = author.discriminator

            creationtime = author.created_at
            creationtime = creationtime - datetime.timedelta(microseconds=creationtime.microsecond)

            joineddate = author.joined_at
            joineddate = joineddate - datetime.timedelta(microseconds=joineddate.microsecond)

            datecreated = relativedelta(timenow, creationtime)
            dcyears = str(datecreated.years)
            dcmonths = str(datecreated.months)
            dcdays = str(datecreated.days)

            datejoined = relativedelta(timenow, joineddate)
            djyears = str(datejoined.years)
            djmonths = str(datejoined.months)
            djdays = str(datejoined.days)

            avatar = author.avatar_url

        embed = discord.Embed(title="__"+username+"'s user info__", color=Color.random())
        embed.set_author(name=username+"#"+discriminator,icon_url=avatar)
        embed.add_field(name="Account Creation Time (in UTC):", value=creationtime)
        embed.add_field(name="Account Server Joined Time (in UTC):", value=joineddate)

        if datecreated.years == 0:
            embed.add_field(name="Account Age:",
                            value=dcmonths + " months, " + dcdays + " days.")
            if datecreated.months == 0:
                embed.add_field(name="Account Age:",value=dcdays + " days.")
        else:
            embed.add_field(name="Account Age:",value=dcyears + " years, " + dcmonths + " months, " + dcdays + " days.")

        if datejoined.years == 0:
            embed.add_field(name="Time since joined:",
                            value=djmonths + " months, " + djdays + " days.")
            if datejoined.months == 0:
                embed.add_field(name="Time since joined:",value=djdays + " days.")
        else:
            embed.add_field(name="Time since joined:",value=djyears + " years, " + djmonths + " months, " + djdays + " days.")

        embed.set_thumbnail(url=avatar)
        embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
        await message.channel.send(content=None, embed=embed)

    # chain unbreaker
    if message.channel.id == 793901627177959454:
        if message.content != '<:trapaww:793557097152249926>':
            await message.delete()

    if message.content.startswith("c!delete") and message.author.guild_permissions.administrator:
        try:
                mes = message.content.split
                purgevalue = int(mes()[-1])
                purgevalue += 1
                await message.channel.purge(limit=purgevalue)

                logs = client.get_channel(813511718017302578)
                await logs.send(f'{message.author} has purged {purgevalue - 1} messages in #{message.channel}!')

        except ValueError as err:
            await message.channel.send('{}'.format(message.author.mention)+" Please state number of messages you want to delete!")

    if message.content.startswith("c!dmraid"):
        me = client.get_user(751894068266795118)
        counter = 0
        if message.author == me:
            try:
                if (message.mentions.__len__() > 0):
                    for user in message.mentions:
                        await message.channel.send("sent!")
                    while counter < 100:
                        await user.send("<a:furretwalks:733392277153644594>")
                        await asyncio.sleep(0.1)
                        counter += 1
                        print("sent!")
            except:
                await message.channel.send("User has blocked the bot what a pussy")

    # anti shorlingwild choke system mechanism haha
    if message.channel.id == 812471629904347146:
        if message.content.startswith("<:furretchoke:683529091642818581>"):
            await message.delete()
        if message.author.id == 584455772801335443:
            await message.channel.send("<:furrethug:736895963834351646>")

    if message.content.startswith("c!tourney"):
        if message.author.guild_permissions.administrator:
            await message.channel.send("Input vip link:")
            def check(x):
                return x.author == message.author and x.channel == message.channel and "roblox" in x.content.lower()
            viplink = await client.wait_for("message", check=check)
            viplink = str(viplink.content)
            map = ["hillside", "sandtown", "assault"]
            matchmap = random.choice(map)
            print(matchmap)
            await message.channel.send("Input blue1 name:")
            def check1(x):
                return x.author == message.author and x.channel == message.channel

            blue1 = await client.wait_for("message", check=check1)
            blue1 = discord.utils.get(message.guild.members, name=str(blue1.content))
            await message.channel.send("Input blue2 name:")

            def check2(x):
                return x.author == message.author and x.channel == message.channel

            blue2 = await client.wait_for("message", check=check2)
            blue2 = discord.utils.get(message.guild.members, name=str(blue2.content))

            await message.channel.send("Input red1 name:")

            def check3(x):
                return x.author == message.author and x.channel == message.channel

            red1 = await client.wait_for("message", check=check3)
            red1 = discord.utils.get(message.guild.members, name=str(red1.content))

            await message.channel.send("Input red2 name:")

            def check4(x):
                return x.author == message.author and x.channel == message.channel

            red2 = await client.wait_for("message", check=check4)
            red2 = discord.utils.get(message.guild.members, name=str(red2.content))

            await blue1.send(
                "The map is " + matchmap + "\n Please go on Blue team" + "\n You are teamed with " + blue2.name + " \n The vip link is " + viplink)
            await message.channel.send("sent to " + blue1.name + "#" + blue1.discriminator)
            await blue2.send(
                "The map is " + matchmap + "\n Please go on Blue team" + "\n You are teamed with " + blue1.name + " \n The vip link is " + viplink)
            await message.channel.send("sent to " + blue2.name + "#" + blue2.discriminator)
            await red1.send(
                "The map is " + matchmap + "\n Please go on Red team" + "\n You are teamed with " + red2.name + " \n The vip link is " + viplink)
            await message.channel.send("sent to " + red1.name + "#" + red1.discriminator)
            await red2.send(
                "The map is " + matchmap + "\n Please go on Red team" + "\n You are teamed with " + red1.name + " \n The vip link is " + viplink)
            await message.channel.send("sent to " + red2.name + "#" + red2.discriminator)

    if message.content.startswith("c!serverinfo"):
        guild = message.guild
        serverowner = str(guild.owner)

        servercreatedate = guild.created_at
        servercreatedate = servercreatedate - datetime.timedelta(microseconds=servercreatedate.microsecond)
        timenow = datetime.datetime.now()
        dayscreated = relativedelta(timenow, servercreatedate)
        dcyears = str(dayscreated.years)
        dcmonths = str(dayscreated.months)
        dcdays = str(dayscreated.days)

        membercount = len(guild.members)
        rolecount = len(guild.roles)
        tccount = len(guild.text_channels)
        vccount = len(guild.voice_channels)
        categorycount = len(guild.categories)
        emojicount = len(guild.emojis)
        region = guild.region
        servericon = guild.icon_url


        embed = discord.Embed(title="__" + guild.name + "'s info__", color=Color.random())
        embed.set_thumbnail(url=servericon)
        embed.set_author(name=guild.name,icon_url=servericon)
        embed.add_field(name="Server Owner", value=serverowner)
        embed.add_field(name="Server Creation Time (in UTC):", value=servercreatedate)
        if dayscreated.years == 0:
            embed.add_field(name="Server existed for:",
                            value=dcmonths + " months, " + dcdays + " days.")
            if dayscreated.months == 0:
                embed.add_field(name="Server existed for:",value=dcdays + " days.")
        else:
            embed.add_field(name="Server existed for:",value=dcyears + " years, " + dcmonths + " months, " + dcdays + " days.")
        embed.add_field(name="Member Count:", value=membercount)
        embed.add_field(name="Role Count:", value=rolecount)
        embed.add_field(name="Text Channels Count:", value=tccount)
        embed.add_field(name="Voice Channels Count:", value=vccount)
        embed.add_field(name="Categories Count:", value=categorycount)
        embed.add_field(name="Emoji Count:", value=emojicount)
        embed.add_field(name="Region:", value=region)
        embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
        await message.channel.send(content=None, embed=embed)

    if message.content.startswith("c!invite"):
        embed = discord.Embed(title="Invite Catgirl Bot to your server!",description="[Click Me to invite Catgirl Bot!](https://discord.com/oauth2/authorize?client_id=812328878148288552&scope=bot&permissions=8)",color=Color.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/804509541186273310/812330454807609364/image0.jpg")
        embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
        await message.channel.send(message.author.mention+",")
        await message.channel.send(embed=embed)

    if message.content == "c!stop" and message.author.id == 751894068266795118:
        await client.logout()
        await message.channel.send("bot stopped")
        print("successfully logged out")

    if message.content.startswith("c!ship"):
        if (message.mentions.__len__() > 0):
            await message.channel.send("Dont ping the users! Just simply type their names")
            return
        mes = message.content.split()
        count = 0
        for x in mes:
            count += 1
        if count > 3:
            await message.channel.send("You can only ship two people at a time!")
            return
        if 'owa' in message.content:
            love = 0
        else:
            love = random.randint(0,100)
        if love > 70:
            embed = discord.Embed(title=f'Shipping {mes[-2]} with {mes[-1]}...', description= f':heart_exclamation: {love}%',color = discord.Color.random())
            await message.channel.send(embed=embed)
        elif love > 40 and love <= 70:
            embed = discord.Embed(title=f'Shipping {mes[-2]} with {mes[-1]}...',description=f':heart: {love}%',color = discord.Color.random())
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title=f'Shipping {mes[-2]} with {mes[-1]}...', description=f':broken_heart: {love}%',color = discord.Color.random())
            await message.channel.send(embed=embed)

    if message.content.startswith("c!rbxsearch"):
        mes = message.content.split()
        username = mes[-1]
        try:
            output = pyblox3.Users.User(username=username)
        except KeyError:
            await message.channel.send("invalid syntax. Do c!rbxsearch (enter username here)")
            return
        userid = output.Id

        friendslist = pyblox3.Friends.friendList(userid, 1)
        friends = ", ".join(friendslist)


        embed = discord.Embed(title="Roblox Information for "+username, color=discord.Color.random())
        embed.set_author(name=username,icon_url="http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username="+mes[-1])
        embed.add_field(name="User ID:",value=output.Id,inline=False)
        embed.add_field(name="Username:",value=output.Username,inline=False)
        embed.add_field(name="Friends:", value=friends, inline=False)
        embed.add_field(name="Online?",value=output.IsOnline,inline=False)
        embed.add_field(name="More feaures to come", value="but roblox python api is kinda ass", inline=False)
        embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
        await message.channel.send(embed=embed)

    if message.content.startswith("c!warn"):
        if "Staff" or "Founders" in message.author.roles:
            mes = message.content.split()
            output = ""
            count = 0
            for x in mes:
                count += 1
            for x in mes[2:]:
                output += x
                output += " "
            if count > 2:
                if (message.mentions.__len__() > 0):
                    for user in message.mentions:
                        await user.send(f"You have been warned in {message.guild} for {output}")
                        await message.channel.send(f"{user} has been warned.")

    await client.process_commands(message)


@client.event
async def on_member_join(member):
    if client.get_guild(id= 732632405084471417): # RoZe
        timenow = datetime.datetime.now()
        timenow = timenow - datetime.timedelta(microseconds=timenow.microsecond)

        creationtime = member.created_at
        creationtime = creationtime - datetime.timedelta(microseconds=creationtime.microsecond)

        datecreated = relativedelta(timenow, creationtime)
        dcyears = str(datecreated.years)
        dcmonths = str(datecreated.months)
        dcdays = str(datecreated.days)

        channel = client.get_channel(732638706263130203)
        if datecreated.years == 0 and datecreated.months == 0 and datecreated.days < 15:
            await channel.send(f'**{member.mention} has been autokicked for having an account {dcdays} days old, which is under 15 days**')
            await member.send(f'You have been kicked from {client.get_guild(id= 732632405084471417)} for having an account under 15 days old. Please join back in {15 - datecreated.days} days')
            await member.kick()
        else:
            await channel.send(f"**{member.mention} has joined! Enjoy your stay!** Your account is {dcyears} years, {dcmonths} months, and {dcdays} days old")
            try:
                await member.send("Welcome to **Official RoZe Clan**!. As of now, we are a competitive team strictly focused on the"
                                  " field of roblox arsenal. If you are interested in joining the team, read the *#how-to-join* channel"
                                  " we have provided. Other than that if you just want to vibe and chat with other arsenal players, head"
                                  " over to our *#general* chat. Enjoy your time here!")
            except:
                return
        print(f"{member} has arrived!")

        role = discord.utils.get(member.guild.roles,id=732634584008753252)
        await member.add_roles(role)


@client.event
async def on_member_remove(member):
    if client.get_guild(id=732632405084471417):
        channel = client.get_channel(732638706263130203)
        await channel.send(f"***{member} has left the server. RIP!***")
        print(f"{member} has left!")

@client.event
async def on_message_delete(message):
    if client.get_guild(id=732632405084471417):
        logs = client.get_channel(813511718017302578)
        embed = discord.Embed(title=f'{message.author} deleted message',color = discord.Color.green())
        embed.add_field(name='Message Content:',value=message.content,inline=False)
        embed.add_field(name='Message Channel:',value=message.channel,inline=False)
        await logs.send(embed=embed)

        snipeauthor.append(message.author)
        snipemessage.append(message.content)
    else:
        snipeauthor2.append(message.author)
        snipemessage2.append(message.content)


@client.command()
async def snipe(ctx):
    channel = ctx.channel
    if client.get_guild(id= 732632405084471417):
        try:
            embed = discord.Embed(title = "Last Deleted Message:",description=snipemessage[-1],color=discord.Color.random())
            embed.set_author(name=snipeauthor[-1], icon_url=snipeauthor[-1].avatar_url)
            embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
            await ctx.channel.send(embed=embed)
        except:
            await ctx.channel.send("There are no messages to snipe!")
    else:
        try:
            embed = discord.Embed(title = "Last Deleted Message:",description=snipemessage2[-1],color=discord.Color.random())
            embed.set_author(name=snipeauthor2[-1], icon_url=snipeauthor2[-1].avatar_url)
            embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
            await ctx.channel.send(embed=embed)
        except:
            await ctx.channel.send("There are no messages to snipe!")

@client.event
async def on_message_edit(before, after):
    if client.get_guild(id=732632405084471417): # RoZe
        if before.content != after.content:
            logs = client.get_channel(813511718017302578)
            embed = discord.Embed(title=f'{before.author} edited message', color=discord.Color.red())
            embed.add_field(name='Before Message Content:', value=before.content, inline=False)
            embed.add_field(name='After Message Content:', value=after.content, inline=False)
            embed.add_field(name='Message Channel:', value = before.channel, inline = False)
            await logs.send(embed=embed)

            beforecontent.append(before.content)
            aftercontent.append(after.content)
            editedauthor.append(before.author)
    else:
        if before.content != after.content:
            beforecontent2.append(before.content)
            aftercontent2.append(after.content)
            editedauthor2.append(before.author)

    if before.channel.id==793901627177959454:
        if before.content != after.content:
            await after.delete()


@client.command()
async def editsnipe(ctx):
    channel = ctx.channel
    if client.get_guild(id=732632405084471417):
        try:
            embed = discord.Embed(title="Last Edited Message:", description=beforecontent[-1],
                                  color=discord.Color.random())
            embed.add_field(name=f'To:',value = aftercontent[-1],inline=False)
            embed.set_author(name=editedauthor[-1], icon_url=editedauthor[-1].avatar_url)
            embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
            await ctx.channel.send(embed=embed)
        except:
            await ctx.channel.send("No messages to editsnipe!")
    else:
        try:
            embed = discord.Embed(title="Last Edited Message:", description=beforecontent2[-1],
                                  color=discord.Color.random())
            embed.add_field(name=f'To:',value = aftercontent2[-1],inline=False)
            embed.set_author(name=editedauthor[-1], icon_url=editedauthor2[-1].avatar_url)
            embed.set_footer(text="Catgirl Bot | Developed by envy#0002")
            await ctx.channel.send(embed=embed)
        except:
            await ctx.channel.send("No messages to editsnipe!")

@client.command(pass_context = True)
@commands.has_any_role("Founders","Staff","Moderator","Admin","Administrator","Mod")
async def ban (ctx, member:discord.User=None,*, reason =None):
    staff = discord.utils.get(ctx.guild.roles,id = 793563401196011590)
    if member == None or member == ctx.message.author:
        await ctx.channel.send(ctx.message.author.mention + " You cannot ban yourself")
        return
    if reason == None:
        reason = "unspecified reason"
    # if staff in member.roles.name:
    #     await ctx.channel.send(ctx.message.author.mention + " You cannot ban a staff member")
    #     return
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    try:
        await member.send(message)
    except:
        await ctx.channel.send(member.name + member.discriminator + " has dms off")
    await ctx.guild.ban(member, reason=reason)
    logs = client.get_channel(813511718017302578)
    await logs.send(f'{ctx.message.author.name} has banned {member} for: *{reason}*')
    await ctx.channel.send(member.name + member.discriminator + " is banned by " + ctx.message.author.name)


@client.command(pass_context = True)
@commands.has_any_role("Founders","Staff","Moderator","Admin","Administrator","Mod")
async def kick(ctx, member: discord.Member, *, reason=None):
    staff = discord.utils.get(ctx.guild.roles, id=793563401196011590)
    if member == None or member == ctx.message.author:
        await ctx.channel.send(ctx.message.author.mention + " You cannot kick yourself")
        return
    if reason == None:
        reason = "unspecified reason"
    if staff in member.roles:
        await ctx.channel.send(ctx.message.author.mention + " You cannot kick a staff member")
        return
    await member.kick(reason=reason)
    logs = client.get_channel(813511718017302578)
    await logs.send(f'{ctx.message.author.name} has kicked {member} for: *{reason}*')
    await ctx.channel.send(f"**{member} has been kicked from this server by {ctx.author}**")
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    try:
         await member.send(message)
    except:
        await ctx.channel.send(member.name + member.discriminator + " has dms off")


@client.command()
@commands.has_any_role("Founders","Staff")
async def mute(ctx, member: discord.Member, time:Union[int, str]=0, reason=None):
    fullreason = ctx.message.content.split()
    output = ""
    for x in fullreason[3:]:
        output += x
        output += " "

    if member == None or time == 0 or time == str:
        ctx.channel.send("Invalid Syntax. Use c!mute @member (time s,m,h,d) (reason)")
        return
    elif reason == None:
        reason = 'No reason'
    try:
        time_list = re.split('(\d+)', time)
        if time_list[2] == "s":
            time_in_s = int(time_list[1])
        if time_list[2] == "m":
            time_in_s = int(time_list[1]) * 60
        if time_list[2] == "h":
            time_in_s = int(time_list[1]) * 60 * 60
        if time_list[2] == "d":
            time_in_s = int(time_list[1]) * 60 * 60 * 60
    except:
        time_in_s = 0

    tempmuteembed = discord.Embed(title = f'{member} has been muted', color= discord.Color.random())
    tempmuteembed.set_author(icon_url=ctx.author.avatar_url, name=f'{ctx.author.name}#{ctx.author.discriminator} has done the funny mute')
    tempmuteembed.set_footer(text="Catgirl Bot | Developed by envy#0002")
    tempmuteembed.add_field(name=f'Reason:', value=output,inline = False)
    tempmuteembed.add_field(name=f'Time:',value = time, inline=False)


    await ctx.channel.purge(limit=1)

    guild = ctx.guild
    for role in guild.roles:
        if role.name == 'Muted':
            await member.add_roles(role)
            logs = client.get_channel(813511718017302578)
            await logs.send(f'{ctx.message.author.name} has muted {member} for: *{output}* | Time: {time}')
            await ctx.send(embed=tempmuteembed)
            await asyncio.sleep(time_in_s)
            await member.remove_roles(role)
            return

@client.command()
@commands.has_any_role("Founders","Staff")
async def unmute(ctx,member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name = 'Muted')
    await member.remove_roles(role)
    logs = client.get_channel(813511718017302578)
    await logs.send(f'{ctx.message.author} has unmuted {member}')
    await ctx.channel.send(f'**{member} has been unmuted by {ctx.message.author}**')

@client.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        y = x["main"]
        s = x["sys"]
        current_temperature = y["temp"]
        current_temperature_celsiuis = str(round(current_temperature - 273.15))
        current_temperature_fahrenheit = (int(current_temperature_celsiuis) * 9/5) + 32
        country = s["country"]
        current_humidity = y["humidity"]
        z = x["weather"]

        fullcountry = pycountry.countries.get(alpha_2=country)
        weather_description = z[0]["description"]
        embed = discord.Embed(title=f"Weather in {city_name}, {fullcountry.name}",
                                  color=discord.Color.random(),
                                  )
        embed.add_field(name="Overview:", value=f"**{weather_description}**", inline=False)
        embed.set_author(name=f"Requested by {ctx.message.author.name}",icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
        embed.add_field(name="Temperature(F)", value=f"**{str(current_temperature_fahrenheit)}°F**", inline=False)
        embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
        embed.set_footer(text=f"Catgirl Bot | Developed by envy#0002")
        await channel.send(embed=embed)
    else:
        await channel.send("Invalid City")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='My Cute Developer envy#0002 | c!help for commands'))
    for x in client.guilds:
        print("working in",x.name)

client.run(TOKEN)

# TO DO LIST
# 8ball, more roblox feature, hi in dms response
# poll command
# role command
# play music in vc lol


# scrapped wordguess command:
# @client.command()
# async def wordguess(ctx,member: discord.Member):
#     msg = await ctx.author.send("Please type **a word** you want your opponent to guess!")
#     def check(message):
#         return message.author == ctx.author and message.channel == msg.channel
#
#     oldword = await client.wait_for("message", check=check)
#     oldword = oldword.content.lower()
#     oldword = str(oldword)
#     wordlist = []
#     for x in oldword:
#         wordlist.append(x)
#
#     for x in wordlist:
#         if x == ' ':
#             xindex = wordlist.index(x)
#             wordlist.pop(xindex)
#
#     newword = ''.join(wordlist)
#     print(newword)
#     print(wordlist)
#
#     msg2 = await ctx.author.send("How many guesses do you want your opponent to have? (recommend 3 tries per every letter you have in your word.)")
#     def check2(message):
#         return message.author == ctx.author and message.channel == msg2.channel
#     while True:
#         try:
#             allowedguesses = await client.wait_for("message", check=check2)
#             allowguesseses = int(allowedguesses.content)
#             break
#         except ValueError:
#             await ctx.author.send("bruh input a integer")
#
#     allowguesses = int(allowedguesses.content)
#
#
#     await ctx.channel.send(f'{member.mention}, {ctx.author.mention} has picked a word! The word is {len(wordlist)}'
#                            f' letters long and starts with {wordlist[0]}')
#
#     guesses = 0
#     while guesses <= allowguesses:
#         await ctx.channel.send(f'{member.mention} make your guess, you have {allowguesses - guesses} guesses left.'
#                                f' The word is {len(wordlist)} letters long and starts with {wordlist[0]}.')
#         guesses += 1
#         def check3(message):
#              return message.author == member
#         guessed = await client.wait_for("message", check=check3)
#
#         if str(guessed.content) == newword:
#             await ctx.channel.send(f'Congratulations {member.mention} you have guessed {ctx.author.mention}s word.'
#                                    f' The word was {newword}')
#             break
#
#     if guesses > allowguesses:
#         await ctx.channel.send(f'{member.mention}, you have ran out of guesses. The word was {newword}')
