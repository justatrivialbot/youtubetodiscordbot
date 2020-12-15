<<<<<<< HEAD
"""
Youtube RSS feed to Discord.
General note: the version running on the r/hermitcraft discord also posts
comments to a couple of reddit threads. This logic has been removed for the
Github version since let's face it, you're looking for a discord bot only.
"""
import asyncio
import feedparser
import pickle
import os
import time
from datetime import datetime, timedelta, timezone
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.utils import get
from dotenv import load_dotenv

# define global variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!!")
# Log into reddit using data from the env


# Feed retrieval
def getFeed(channel):
    # define the url
    channel_url = "https://www.youtube.com/feeds/videos.xml?channel_id="
    channel_url += channel
    # retrieve the feed
    NewsFeed = feedparser.parse(channel_url)
    return NewsFeed


# Feed data parsing
def parseFeed(feed_data, pretty_name, last_timestamp):
    # add time parsing later
    output = []
    entries = feed_data.entries

    # get the first entry data for the discord
    first_entry = feed_data.entries[0]
    pub_time = first_entry.published_parsed  # tuple
    pub_timestamp = time.mktime(pub_time)
    pub_time_str = time.strftime("%B %d, %Y at %I:%m%p UTC", pub_time)

    # check if it's a new video
    if pub_timestamp > last_timestamp:
        msg = (f"{pretty_name} New video {pub_time_str} ({pub_timestamp})")
        print(msg)
        chatstring = "**" + pretty_name + "** uploaded "
        chatstring += "**" + first_entry.title + "** "
        chatstring += "at " + pub_time_str
        chatstring += " " + first_entry.link
        output = [chatstring, pub_timestamp]
    else:  # not a new video
        # print(f"No new videos from {pretty_name}")
        output = ["", pub_timestamp]

    # loop through all entries in each feed for the subreddits
    for entry in entries:
        entry_pub_time = datetime.fromisoformat(entry.published)
        title = entry.title.replace('|', '')
        now = datetime.now(timezone.utc)
        substring = "hermitcraft"
        # check if it's a new video
        if now - timedelta(hours=24) <= entry_pub_time:
            if substring in title.lower():
                pretty_time = str(entry_pub_time)[:-9]
                msg = (f"|{pretty_name}|{title}|{pretty_time}|\n")
                # print(msg)
                output.append(msg)

    # print(output)
    return output  # list with 3 items: chatstring, pub timestamp, reddit


@bot.command(name="patrolvideos")
@has_permissions(administrator=True)
async def repeatvideocheck(ctx, looptime):
    """
    Repeating video patrol.
    looptime = how often to check, in minutes. Recommend 5+
    """
    big_looptime = int(looptime) * 60  # Convert passed loop time to seconds
    # big_looptime = int(looptime)
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("checking videos " + dt_string)
        filename = "channeldata.txt"
        channel_ids = pickle.load(open(filename, "rb"))
        # set up the markdown table for reddit
        for idx, channel_id in enumerate(channel_ids):
            feed_get = getFeed(channel_id[0])
            feed_parse = parseFeed(feed_get, channel_id[1],
                                   channel_id[2])
            if channel_id[3] == "main":
                disc_channel = "channel-one"
            elif channel_id[3] == "alt":
                disc_channel = "channel-two"
            try:
                if feed_parse[0]:
                    chosen_channel = get(ctx.guild.channels,
                                         name=disc_channel)
                    await chosen_channel.send(feed_parse[0])
            except Exception:
                pass
            await asyncio.sleep(1)  # seconds
        # end for loop
        # Write the channel ids to file
        pickle.dump(channel_ids, open(filename, "wb"))
        # for channel in channel_ids:
        #     print(f"{channel[0]}: {channel[1]}, {channel[2]}, {channel[3]}")
        await asyncio.sleep(int(big_looptime))


@bot.command(name="addchannel")
@has_permissions(administrator=True)
async def newchannel(ctx, channel_id, last_vid_timestamp, channel_type, args):
    """
    Adds a new channel to the roster.
    channel_id: unique string e.g. UClu2e7S8atp6tG2galK9hgg
    last_vid: UTC timestamp of last video
    channel_type = main or alt
    args: display name of channel in double quotes
    """
    # pull the list from pickle
    filename = "channeldata.txt"
    channel_ids = pickle.load(open(filename, "rb"))
    # add a new list item
    display_name = args
    new_channel = [channel_id, display_name, last_vid_timestamp, channel_type]
    channel_ids.append(new_channel)
    # dump it back into pickle
    pickle.dump(channel_ids, open(filename, "wb"))
    await ctx.send(f"Channel **{display_name}** added to roster.")


@bot.command(name="listchannels")
@has_permissions(administrator=True)
async def channellist(ctx):
    """
    Lists channels currently included in the roster.
    """
    filename = "channeldata.txt"
    channel_ids = pickle.load(open(filename, "rb"))
    name_list = []
    for channel in channel_ids:
        name_list.append(channel[1])
    output = ", ".join(name_list)
    await ctx.send(output)


@bot.command(name="deletechannel")
@has_permissions(administrator=True)
async def delchannel(ctx, args):
    """
    Removes a channel from the roster.
    Args: Channel display name, in double quotes, case insensitive
    """
    filename = "channeldata.txt"
    channel_ids = pickle.load(open(filename, "rb"))
    for idx, channel in enumerate(channel_ids):
        channel_name = channel[1].lower()
        target_channel = args.lower()
        if channel_name == target_channel:
            channel_ids.remove(channel_ids[idx])
    pickle.dump(channel_ids, open(filename, "wb"))
    await ctx.send(f"Channel **{target_channel}** removed from roster.")

bot.run(TOKEN)
=======
"""
Youtube RSS feed to Discord.
General note: the version running on the r/hermitcraft discord also posts
comments to a couple of reddit threads. This logic has been removed for the
Github version since let's face it, you're looking for a discord bot only.
"""
import asyncio
import feedparser
import pickle
import os
import time
from datetime import datetime, timedelta, timezone
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.utils import get
from dotenv import load_dotenv

# define global variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!!")
# Log into reddit using data from the env


# Feed retrieval
def getFeed(channel):
    # define the url
    channel_url = "https://www.youtube.com/feeds/videos.xml?channel_id="
    channel_url += channel
    # retrieve the feed
    NewsFeed = feedparser.parse(channel_url)
    return NewsFeed


# Feed data parsing
def parseFeed(feed_data, pretty_name, last_timestamp):
    # add time parsing later
    output = []
    entries = feed_data.entries

    # get the first entry data for the discord
    first_entry = feed_data.entries[0]
    pub_time = first_entry.published_parsed  # tuple
    pub_timestamp = time.mktime(pub_time)
    pub_time_str = time.strftime("%B %d, %Y at %I:%m%p UTC", pub_time)

    # check if it's a new video
    if pub_timestamp > last_timestamp:
        msg = (f"{pretty_name} New video {pub_time_str} ({pub_timestamp})")
        print(msg)
        chatstring = "**" + pretty_name + "** uploaded "
        chatstring += "**" + first_entry.title + "** "
        chatstring += "at " + pub_time_str
        chatstring += " " + first_entry.link
        output = [chatstring, pub_timestamp]
    else:  # not a new video
        # print(f"No new videos from {pretty_name}")
        output = ["", pub_timestamp]

    # loop through all entries in each feed for the subreddits
    for entry in entries:
        entry_pub_time = datetime.fromisoformat(entry.published)
        title = entry.title.replace('|', '')
        now = datetime.now(timezone.utc)
        substring = "hermitcraft"
        # check if it's a new video
        if now - timedelta(hours=24) <= entry_pub_time:
            if substring in title.lower():
                pretty_time = str(entry_pub_time)[:-9]
                msg = (f"|{pretty_name}|{title}|{pretty_time}|\n")
                # print(msg)
                output.append(msg)

    # print(output)
    return output  # list with 3 items: chatstring, pub timestamp, reddit


@bot.command(name="patrolvideos")
@has_permissions(administrator=True)
async def repeatvideocheck(ctx, looptime):
    """
    Repeating video patrol.
    looptime = how often to check, in minutes. Recommend 5+
    """
    big_looptime = int(looptime) * 60  # Convert passed loop time to seconds
    # big_looptime = int(looptime)
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("checking videos " + dt_string)
        filename = "channeldata.txt"
        channel_ids = pickle.load(open(filename, "rb"))
        # set up the markdown table for reddit
        for idx, channel_id in enumerate(channel_ids):
            feed_get = getFeed(channel_id[0])
            feed_parse = parseFeed(feed_get, channel_id[1],
                                   channel_id[2])
            if channel_id[3] == "main":
                disc_channel = "channel-one"
            elif channel_id[3] == "alt":
                disc_channel = "channel-two"
            try:
                if feed_parse[0]:
                    chosen_channel = get(ctx.guild.channels,
                                         name=disc_channel)
                    await chosen_channel.send(feed_parse[0])
            except Exception:
                pass
            await asyncio.sleep(1)  # seconds
        # end for loop
        # Write the channel ids to file
        pickle.dump(channel_ids, open(filename, "wb"))
        # for channel in channel_ids:
        #     print(f"{channel[0]}: {channel[1]}, {channel[2]}, {channel[3]}")
        await asyncio.sleep(int(big_looptime))


@bot.command(name="addchannel")
@has_permissions(administrator=True)
async def newchannel(ctx, channel_id, last_vid_timestamp, channel_type, args):
    """
    Adds a new channel to the roster.
    channel_id: unique string e.g. UClu2e7S8atp6tG2galK9hgg
    last_vid: UTC timestamp of last video
    channel_type = main or alt
    args: display name of channel in double quotes
    """
    # pull the list from pickle
    filename = "channeldata.txt"
    channel_ids = pickle.load(open(filename, "rb"))
    # add a new list item
    display_name = args
    new_channel = [channel_id, display_name, last_vid_timestamp, channel_type]
    channel_ids.append(new_channel)
    # dump it back into pickle
    pickle.dump(channel_ids, open(filename, "wb"))
    await ctx.send(f"Channel **{display_name}** added to roster.")


@bot.command(name="listchannels")
@has_permissions(administrator=True)
async def channellist(ctx):
    """
    Lists channels currently included in the roster.
    """
    filename = "channeldata.txt"
    channel_ids = pickle.load(open(filename, "rb"))
    name_list = []
    for channel in channel_ids:
        name_list.append(channel[1])
    output = ", ".join(name_list)
    await ctx.send(output)


@bot.command(name="deletechannel")
@has_permissions(administrator=True)
async def delchannel(ctx, args):
    """
    Removes a channel from the roster.
    Args: Channel display name, in double quotes, case insensitive
    """
    filename = "channeldata.txt"
    channel_ids = pickle.load(open(filename, "rb"))
    for idx, channel in enumerate(channel_ids):
        channel_name = channel[1].lower()
        target_channel = args.lower()
        if channel_name == target_channel:
            channel_ids.remove(channel_ids[idx])
    pickle.dump(channel_ids, open(filename, "wb"))
    await ctx.send(f"Channel **{target_channel}** removed from roster.")

bot.run(TOKEN)
>>>>>>> 4f4495ec3a8542beb18ca55c279652518c1e7922
