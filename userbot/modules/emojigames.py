# fix by @heyworld for OUB
# bug fixed by @d3athwarrior

from telethon.tl.types import InputMediaDice
from userbot.events import xubot_cmd
from userbot import CUSTOM_CMD as xcm
from userbot import bot, CMD_HELP


@bot.on(xubot_cmd(outgoing=True, pattern="dice(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice(''))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(''))
        except BaseException:
            pass


@bot.on(xubot_cmd(outgoing=True, pattern="dart(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('🎯'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🎯'))
        except BaseException:
            pass


@bot.on(xubot_cmd(outgoing=True, pattern="ball(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('🏀'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🏀'))
        except BaseException:
            pass

CMD_HELP.update({
    "emojigames":
    f"`{xcm}dice` 1-6 or `{xcm}dart`1-6 or `{xcm}ball`1-5\
\nUsage: hahaha just a magic.\nWarning:`Don't use any other values or bot will crash`"
})
