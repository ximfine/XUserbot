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
            await conv.send_message(f"/gen {query}")
            await.asyncio.sleep(3)
            r1 = await conv.get_response()
            r2 = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @SaitamaRobot plox")
        if r1.text.startswith("Waiting"):
            return await event.edit(f"`No result found for` **{query}**")
        else:
            await event.edit(r2,
                             reply_to=event.reply_to_msg_id)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])
