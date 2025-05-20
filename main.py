from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)
import json
import os


async def cc_mention(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message == None:
        return
    if update.message.text == None:
        return
    list_mention: list[str] = []
    for k in map_mention:
        if k in update.message.text:
            list_mention += map_mention[k]
    if len(list_mention) == 0:
        return
    set_mention = set(list_mention)
    msg = ", ".join(set_mention)
    msg = "cc: " + msg
    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        reply_to_message_id=update.message.message_id,
    )


map_mention_str = os.getenv("MAP_MENTION")
if not map_mention_str or map_mention_str == "":
    print("MAP_MENTION is not set or empty")
    exit(1)

map_mention = json.loads(map_mention_str)

if len(map_mention) == 0:
    print("map_mention json is empty")
    exit(1)


BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN or BOT_TOKEN == "":
    print("BOT_TOKEN is not set or empty")
    exit(1)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), cc_mention))

print("Bot is running...")
app.run_polling()
