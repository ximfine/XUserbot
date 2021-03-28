import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from userbot import CMD_HELP, bot
from userbot.events import xubot_cmd
from userbot import CUSTOM_CMD as xcm

path = "TEMP_DOWNLOAD_DIRECTORY"

telegraph = Telegraph()
r = telegraph.create_account(short_name="telegraph")
auth_url = r["auth_url"]


@bot.on(xubot_cmd(outgoing=True, pattern="tgm"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`processing........`")
    if not event.reply_to_msg_id:
        await event.edit("`Reply di image /sticker Goblok!!`")
        return
    start = datetime.now()
    r_message = await event.get_reply_message()
    downloaded_file_name = await event.client.download_media(
        r_message, path
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


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


CMD_HELP.update({"telegraph": f">`{xcm}tgm`"
                 "\nUsage: Upload t(text) or m(media) on Telegraph."})
