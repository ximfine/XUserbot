"""Get Detailed info about any message
Syntax: .json"""
import io
from userbot import bot
from telethon import events
from userbot.events import xubot_cmd

MAX_MESSAGE_SIZE_LIMIT = 4095


@bot.on(xubot_cmd(pattern="json"))
async def _(event):
    if event.fwd_from:
        return
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    if len(the_real_message) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(the_real_message)) as out_file:
            out_file.name = "json.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                reply_to=reply_to_id
            )
            await event.delete()
    else:
        await event.edit("`{}`".format(the_real_message))



@bot.on(xubot_cmd(pattern="xjson"))
async def _(event):
    if event.fwd_from:
        return
    catevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = catevent.stringify()
    await event.edit(the_real_message, parse_mode=parse_pre)
