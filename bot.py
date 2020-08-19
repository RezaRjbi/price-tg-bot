from functionality import Functionality
from telegram.ext import CommandHandler, MessageHandler, Filters

token = ""  # get your own token from @Botfather and paste it between ""
funcs = Functionality(token=token)

start_handler = CommandHandler("start", funcs.start)
funcs.dispather.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), funcs.echo)
funcs.dispather.add_handler(echo_handler)

price_handler = CommandHandler("price", funcs.price)
funcs.dispather.add_handler(price_handler)

unknown_handler = MessageHandler(Filters.command, funcs.unknown)
funcs.dispather.add_handler(unknown_handler)

funcs.updater.start_polling()
