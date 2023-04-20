# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for BOT Users
 ├ /start - Start Bot
 ├ /about - About this Bot
 ├ /help - Help Command this Bot
 ├ /ping - To check live bot
 └ /uptime - To see bot status
 
 ❏ Command For Admin BOT
 ├ /logs - To view bot logs
 ├ /setvar - To set var with dibot command
 ├ /delvar - To remove var with bot command
 ├ /getvar - To see one of the vars with the bot command
 ├ /users - To view bot user statistics
 ├ /batch - To link more than one file
 ├ /speedtest - To Test the bot server speed
 └ /broadcast - To send broadcast messages to bot users

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About this Bot:

@{} is a Telegram Bot for storing posts or files that can be accessed via a special link..

 • Creator: @{} """
