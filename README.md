# The r/Hermitcraft Discord Videos Bot

## Features

* Alerts Discord of new videos on any number of Youtube channels.
* Utilizes RSS feeds to eliminate Youtube API usage.
* In-channel administration of channel list.
* Allows for two separate subgroups, e.g., for main and second channels piped to separate discord channels.

## Installation

* Requires Python 3.
   * Packages: asyncio, feedparser, pickle, discord.py, os, datetime, time, dotenv
* Keeps and regularly updates a text file (channeldata.txt).
* Configure your default channel list.
   * channeldata.txt uses pickle to encode a list of lists. Do not try to edit it yourself. Instead, use the provided "resetchannelids.py" helper file.
   * The bot also allows you to add, remove, and list Youtube channels from within discord, but for first run it will probably be easier to do it within "resetchannelids.py" instead, particularly if you've got a long list of channels.
   * The provided file includes all Hermitcraft main and second channels in a list of lists. Edit as you see fit.
   * The list format for a new channel is [str(channel_id), str(display_name), int(utc_timestamp), str(subgroup_name)].
   * To obtain the unique Youtube channel id for a new channel, visit the channel in your browser, open in console, and look for "<link rel="canonical" href="https://youtube.com/channel/this_is_the_unique_id_you_want"> in the header.
* Edit "discordvideos.py"
   * Set your desired Youtube subgroup to discord output channel mapping in lines 98-101. The default subgroups are "main" and "alt" and the default output channels are "channel-one" and "channel-two".
   * The default prefix for bot commands is "!!". Change this on line 21 if you like.
* Create a Discord bot:
   * Go to the [Discord Developers page](https://discord.com/developers/applications).
   * Create a New Application (top right corner).
   * Enter the application you just created.
   * On the General information screen, fill in the Name and Description.
   * In the left hand menu, select "Bot".
   * Create a new Bot and set its username and a profile pic if you so desire.
   * In the token section click "Copy", then paste the copied data into the included .env file where it says "YOUR_TOKEN_HERE".
   * Back in the Discord page, select "OAuth2" from the left hand menu.
   * In the Scopes section select the checkbox for "Bot". It should be in the center column. A "Bot Permissions" section will appear underneath the Scopes section.
   * In the new Bot Permissions section select at minimum "Send Messages" and "Embed Links". If you plan to add additional features to your bot feel free to grant it additional permissions.
   * Once you have selected all permissions, copy the link in the text field at the bottom of the Scopes section and go there in your browser to add your bot to your discord.
* From the command line run the "discordvideos.py" script and your bot should join your discord.
* Assign proper permissions to your bot in discord as you see fit.

## Bot Operation

* !!help will display a help file.
* I recommend adding the bot to three channels: one for administration plus the two channels where it's speaking. However, all commands require discord admin permissions to run so you could technically only have the bot in your output channels.
* Commands are:
   * addchannel
   * listchannels
   * deletechannel
   * patrolvideos
* The patrolvideos command requires a frequency parameter in minutes, e.g., "!!patrolvideos 15" to run it every 15 minutes.
   * Youtube builds in an automatic delay of approximately 11 minutes between the time videos hit subscriber feeds and the time they hit the API. However, to be courteous and avoid rate limiting I would recommend running it no more than once every 10 minutes or so.

## Known Issues

* The patrolvideos loop isn't terribly robust. If your internet connection dies or it encounters an error it will stop dead, requiring a rebooting of the script.
* I would eventually like to convert it to a background task but I don't know how to do that yet. It will happen once I chew on the discord.py docs a bit more.
