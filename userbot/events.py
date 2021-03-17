# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

import codecs
import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc

import requests
from telethon import events

from userbot import BOTLOG_CHATID, LOGSPAMMER, bot, CUSTOM_CMD, CMD_HELP, UB_BLACK_LIST_CHAT


def admin_cmd(pattern=None, command=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith(r"\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        elif pattern.startswith(r"^"):
            args["pattern"] = re.compile(pattern)
            cmd = pattern.replace("$", "").replace("^", "").replace("\\", "")
            try:
                CMD_HELP[file_test].append(cmd)
            except BaseException:
                CMD_HELP.update({file_test: [cmd]})
        else:
            if len(CUSTOM_CMD) == 2:
                catreg = "^" + CUSTOM_CMD
                reg = CUSTOM_CMD[1]
            elif len(CUSTOM_CMD) == 1:
                catreg = "^\\" + CUSTOM_CMD
                reg = CUSTOM_CMD
            args["pattern"] = re.compile(catreg + pattern)
            if command is not None:
                cmd = reg + command
            else:
                cmd = (
                    (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_HELP[file_test].append(cmd)
            except BaseException:
                CMD_HELP.update({file_test: [cmd]})

    args["outgoing"] = True
    # should this command be available for other users?

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(UB_BLACK_LIST_CHAT)
    if black_list_chats:
        args["chats"] = black_list_chats

    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]

    # check if the plugin should listen for outgoing 'messages'

    return events.NewMessage(**args)


def errors_handler(func):
    async def wrapper(errors):
        try:
            await func(errors)
        except BaseException:
            if BOTLOG_CHATID is None:
                return
            date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            ftext = "\nDisclaimer:\nThis file is pasted only here ONLY here,"
            ftext += "\nwe logged only fact of error and date,"
            ftext += "\nwe respect your privacy,"
            ftext += "\nyou may not report this error if you've"
            ftext += "\nany confidential data here, no one will see your data\n\n"
            ftext += "--------BEGIN USERBOT TRACEBACK LOG--------"
            ftext += "\nDate: " + date
            ftext += "\nGroup ID: " + str(errors.chat_id)
            ftext += "\nSender ID: " + str(errors.sender_id)
            ftext += "\n\nEvent Trigger:\n"
            ftext += str(errors.text)
            ftext += "\n\nTraceback info:\n"
            ftext += str(traceback.format_exc())
            ftext += "\n\nError text:\n"
            ftext += str(sys.exc_info()[1])
            new = {"error": str(sys.exc_info()[1]), "date": datetime.datetime.now()}
            ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

            command = 'git log --pretty=format:"%an: %s" -5'

            ftext += "\n\n\nLast 5 commits:\n"

            process = await asyncio.create_subprocess_shell(
                command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())
            ftext += result
            from .helpers.utils import _format

            if LOGSPAMMER:
                        await error.edit(
                            "`Sorry, my userbot has crashed.\nThe error logs are stored in the userbot's log chat.`"
                        )

                        log = codecs.open("error.log", "r", encoding="utf-8")
                        data = log.read()
                        key = (
                            requests.post(
                                "https://nekobin.com/api/documents",
                                json={"content": data},
                            )
                            .json()
                            .get("result")
                            .get("key")
                        )
                        url = f"https://nekobin.com/raw/{key}"
                        anu = f"{text}\n`Here the error:`\nPasted to: [Nekobin]({url})"
                        await check.client.send_message(send_to, anu)
                        remove("error.log")

    return wrapper
                    

class Loader:
    def __init__(self, func=None, **args):
        self.Config = Config
        bot.add_event_handler(func, events.NewMessage(**args))


# Admin checker by uniborg
async def is_admin(client, chat_id, user_id):
    if not str(chat_id).startswith("-100"):
        return False
    try:
        req_jo = await client(GetParticipantRequest(channel=chat_id, user_id=user_id))
        chat_participant = req_jo.participant
        if isinstance(
            chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
        ):
            return True
    except Exception as e:
        LOGS.info(str(e))
        return False
    else:
        return False


def register(**args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    disable_edited = args.get("disable_edited", True)
    
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    if "disable_edited" in args:
        del args["disable_edited"]

    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass

            try:
                CMD_HELP[file_test].append(cmd)
            except BaseException:
                CMD_HELP.update({file_test: [cmd]})
        except BaseException:
            pass


    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(UB_BLACK_LIST_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args))
        bot.add_event_handler(func, events.NewMessage(**args))
        try:
            CMD_HELP[file_test].append(func)
        except Exception:
            CMD_HELP.update({file_test: [func]})
        return func

    return decorator


def command(**args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    pattern = args.get("pattern", None)
    allow_edited_updates = args.get("allow_edited_updates", False)
    args["incoming"] = args.get("incoming", False)
    args["outgoing"] = True
    if bool(args["incoming"]):
        args["outgoing"] = False

    try:
        if pattern is not None and not pattern.startswith("(?i)"):
            args["pattern"] = "(?i)" + pattern
    except BaseException:
        pass

    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass
            try:
                CMD_HELP[file_test].append(cmd)
            except BaseException:
                CMD_HELP.update({file_test: [cmd]})
        except BaseException:
            pass

    args["blacklist_chats"] = True
    black_list_chats = list(UB_BLACK_LIST_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if "allow_edited_updates" in args:
        del args["allow_edited_updates"]

    def decorator(func):
        if allow_edited_updates:
            bot.add_event_handler(func, events.MessageEdited(**args))
        bot.add_event_handler(func, events.NewMessage(**args))
        try:
            CMD_HELP[file_test].append(func)
        except BaseException:
            CMD_HELP.update({file_test: [func]})
        return func

    return decorator
