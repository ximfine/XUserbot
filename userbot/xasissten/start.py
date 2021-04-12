from telethon  import TelegramClient, custom, events, Button
from userbot import BOT_TOKEN, API_KEY, API_HASH

tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 3
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline("{} {}".format("☠️", x), data="ub_modul_{}".format(x))
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⬅️", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    '❎', b'close'
                ),
                custom.Button.inline(
                    "➡️", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs



dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id
        logo = "https://telegra.ph/file/099b2bf1c3256847946bf.mp4"

@tgbot.on(events.NewMessage(pattern="/start"))
async def handler(event):
            sender = await event.message.get_sender()
            text = (
                f"Hai {sender.first_name}\nSaya adalah bot assisten {ALIVE_NAME}\n\nSaya adalah [XBØT-REMIX](https://github.com/ximfine/XBot-Remix) modules helper...\nplease make your own bot, don't use mine")
            await tgbot.send_file(event.chat_id, logo, caption=text,
                                  buttons=[
                                      [
                                          Button.url(
                                              text="🔱 OFFICIAL CHANNELS 🔱",
                                              url="https://t.me/X_Projectss"
                                          )
                                      ]
                                  ]
                                  )

@tgbot.on(events.InlineQuery)  # pylint:disable=E0602
async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith(""):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.article(
                    "Please Use Only With .help Command",
                    text="{}\nTotal loaded modules: {}".format(
                        "[XBOT-REMIX](https://github.com/ximfine/XBot-Remix) modules helper.\n",
                        len(dugmeler),
                    ),
                    buttons=buttons,
                    link_preview=False,
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "xbot Helper",
                    text="List of Modules",
                    buttons=[],
                    link_preview=True,
                )
            else:
                result = builder.article(
                    "xbot",
                    text="""You can convert your account to bot and use them. Remember, you can't manage someone else's bot! All installation details are explained from GitHub address below.""",
                    buttons=[
                        [
                            custom.Button.url(
                                "GitHub Repo",
                                "https://github.com/ximfine/XBot-Remix",
                            ),
                            custom.Button.url(
                                "Support",
                                "https://t.me/X_Projectss"),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer([result] if result else None)

@tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@tgbot.on(events.CallbackQuery(data=b'close'))
async def close(event):
    await event.edit("Button closed!", buttons=Button.clear())

@tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(b"ub_modul_(.*)")
            )
        )
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == uid:  # pylint:disable=E0602
       modul_name = event.data_match.group(1).decode("UTF-8")

       cmdhel = str(CMD_HELP[modul_name])
       if len(cmdhel) > 150:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace("`", "")[:150]
                        + "..."
                        + "\n\nRead more .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace("`", "")

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} No document has been written for module.".format(
                        modul_name
                    )
                )
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

except BaseException:
    LOGS.info(
            "Support for inline is disabled on your bot. "
            "To enable it, define a bot token and enable inline mode on your bot. "
            "If you think there is a problem other than this, contact us.")
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file."
        )
        sys.exit(1)
