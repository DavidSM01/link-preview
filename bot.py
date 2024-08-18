#!/usr/bin/env python3
from deltachat2 import MsgData, events
from deltabot_cli import BotCli

from app import getResponse

cli = BotCli("bot")


@cli.on(events.NewMessage)
def init(bot, accid, event):
    msg = event.msg
    text = msg.text
    if not text:
        return

    try:
        resp = getResponse(text)
    except Exception as err:
        resp = "**Error:**\n" + str(err)
        print(err)

    respMsg = MsgData(text=resp, quoted_message_id=msg.id)
    bot.rpc.send_msg(accid, msg.chat_id, respMsg)


if __name__ == "__main__":
    cli.start()
