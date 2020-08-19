import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import get_price

token = "" # get your own toke from @Botfather
bot = telegram.Bot(token=token)

updater = Updater(token=token, use_context=True)
dispather = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="gheymat tala")


start_handler = CommandHandler("start", start)
dispather.add_handler(start_handler)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispather.add_handler(echo_handler)


def caps(update, context):
    if context.args:
        caps_text = "".join(context.args).upper()
        context.bot.send_message(chat_id=update.effective_chat.id, text=caps_text)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="type your message after '/caps'")


csps_handler = CommandHandler("caps", caps)
dispather.add_handler(csps_handler)


def price(update, context):
    message = get_price.get_price()
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


price_handler = CommandHandler("price", price)
dispather.add_handler(price_handler)


def unknown(update, context):
    user_id = update.effective_chat.id
    context.bot.send_message(chat_id=user_id,
                             text=f"sorry i don'n recognize {update.message.text.split()[0]} as a command")


unknown_handler = MessageHandler(Filters.command, unknown)
dispather.add_handler(unknown_handler)

updater.start_polling()
