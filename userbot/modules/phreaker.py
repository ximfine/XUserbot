import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot
from userbot.events import xubot_cmd


@bot.on(xubot_cmd(outgoing=True, pattern="gen(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    gen = "gen"
    await event.edit("```Processing```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            link1 = await conv.send_message(f'/{gen} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock plox```")
            return
        else:
            await event.delete()
            await asyncio.sleep(8)
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])


@bot.on(xubot_cmd(outgoing=True, pattern="chk$"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    ss = "ss"
    await event.edit("`Checking CC.....`☠️")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            msg = conv.send_message(f'/{ss} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("unblock me (@Carol5_bot) to work")
            return
        if response.text.startswith("Wait for result..."):
            await event.edit("Sorry i cant't convert it check wheter is non animated sticker or not")
        else:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            response = await response
            if response.text.startswith("|"):
                response = conv.wait_event(
                    events.NewMessage(
                        incoming=True,
                        from_users=1247032902))
                response = await response
                await event.delete()
                await event.client.send_message(event.chat_id, response.message, reply_to=reply_message.id)
                await event.client.delete_messages(conv.chat_id,
                                                   [msg.id, response.id])
            else:
                await event.edit("try again")
        await bot.send_read_acknowledge(conv.chat_id)
