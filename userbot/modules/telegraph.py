import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import xubot_cmd
from userbot import CUSTOM_CMD as xcm

telegraph = Telegraph()
r = telegraph.create_account(short_name="telegraph")
auth_url = r["auth_url"]


@bot.on(xubot_cmd(outgoing=True, pattern="tg (media|text)"))
@bot.on(xubot_cmd(outgoing=True, pattern="tg (m|t)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`processing........`")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "Created New Telegraph account {} for the current session. \n**Do not give this url to anyone, even if they say they are from Telegram!**".format(
                auth_url
            ),
        )
    optional_title = event.pattern_match.group(2)
    if event.reply_to_msg_id:
        start = datetime.now()
        r_message = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str in ["media", "m"]:
            downloaded_file_name = await event.client.download_media(
                r_message, TEMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.now()
            ms = (end - start).seconds
            await event.edit(
                f"`Downloaded to {downloaded_file_name} in {ms} seconds.`"
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await event.edit("**Error : **" + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await event.edit(
                    "**Sukses Upload to : **[Telegraph](https://telegra.ph{})\
                    \n**Time Taken : **`{} seconds.`".format(
                        media_urls[0], (ms + ms_two)
                    ),
                    link_preview=True,
                )
        elif input_str in ["text", "t"]:
            user_object = await event.client.get_entity(r_message.sender_id)
            title_of_page = user_object.first_name  # + " " + user_object.last_name
            # apparently, all Users do not have last_name field
            if optional_title:
                title_of_page = optional_title
            page_content = r_message.message
            if r_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await event.client.download_media(
                    r_message, TEMP_DOWNLOAD_DIRECTORY
                )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page(
                title_of_page, html_content=page_content)
            end = datetime.now()
            ms = (end - start).seconds
            cat = f"https://telegra.ph/{response['path']}"
            await event.edit(
                f"**Sukses Upload to : ** [Telegraph]({cat})\
                 \n**Time Taken : **`{ms} seconds.`",
                link_preview=True,
            )
    else:
        await event.edit(
            "`Reply to a message to get a permanent telegra.ph link. (Inspired by @ControllerBot)`",
        )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


CMD_HELP.update({"telegraph": f">`{xcm}tgm`"
                 "\nUsage: Upload t(text) or m(media) on Telegraph."})
