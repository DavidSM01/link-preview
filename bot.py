#!/usr/bin/env python3
from deltachat2 import MsgData, events
from deltabot_cli import BotCli

from app import getResponse

cli = BotCli("bot")


@cli.on(events.NewMessage)
def init(bot, accid, event):
    msg = event.msg
    text = msg.text
    if text:
        try:
            resp = getResponse(text)
        except Exception as err:
            resp = "**Error getting preview:**\n\n" + str(err)
            print(err)
        try:
            if resp:
                respMsg = MsgData(text=resp, quoted_message_id=msg.id)
                bot.rpc.send_msg(accid, msg.chat_id, respMsg)
        except Exception as err:
            print(err)


if __name__ == "__main__":
    cli.start()
