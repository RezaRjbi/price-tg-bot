import get_price
from telegram.ext import Updater
import telegram


class Functionality:

    def __init__(self, token):
        self.token = token  # get your own token from @Botfather
        self.bot = telegram.Bot(token=self.token)
        self.updater = Updater(token=self.token, use_context=True)
        self.dispather = self.updater.dispatcher

    def start(self, update, context):
        msg = "از طریق دستور /price میتوانید از ربات استقاده کنید"
        user_id = update.effective_chat.id
        context.bot.send_message(chat_id=user_id, text=msg)

    def echo(self, update, context):
        msg = update.message.text
        user_id = update.effective_chat.id
        context.bot.send_message(chat_id=user_id, text=msg)

    def price(self, update, context):
        msg = get_price.get_price()
        user_id = update.effective_chat.id
        context.bot.send_message(chat_id=user_id, text=msg)

    def unknown(self, update, context):
        msg = f"sorry i don'n recognize {update.message.text.split()[0]} as a command!"
        user_id = update.effective_chat.id
        context.bot.send_message(chat_id=user_id, text=msg)