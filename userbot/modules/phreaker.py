from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot
import asyncio
from userbot.events import xubot_cmd


@bot.on(xubot_cmd(outgoing=True, pattern="gen(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    await event.edit("```Processing```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/gen {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot plox")
        if asu.text.startswith("Wait for result..."):
            return await asyncio.sleep(5)
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])
