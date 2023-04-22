import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    chat_id = update.message.chat_id
    with open('images/mem1.jpg', 'rb') as photo_file:
        await context.bot.send_photo(chat_id=chat_id, photo=photo_file)
    with open('images/mem_1.jpg', 'rb') as photo_file:
        await context.bot.send_photo(chat_id=chat_id, photo=photo_file)
    with open('images/mem_2.jpg', 'rb') as photo_file:
        await context.bot.send_photo(chat_id=chat_id, photo=photo_file)



def start(update, _):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # для версии 13.x
    update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)
    # для версии 20.x необходимо использовать оператор await
    # await update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)


def button(update, _):
    query = update.callback_query
    variant = query.data

    # `CallbackQueries` требует ответа, даже если
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы.
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
    # для версии 20.x необходимо использовать оператор await
    # await query.answer()

    # редактируем сообщение, тем самым кнопки
    # в чате заменятся на этот ответ.
    query.edit_message_text(text=f"Выбранный вариант: {variant}")
    # для версии 20.x необходимо использовать оператор await
    # await query.edit_message_text(text=f"Выбранный вариант: {variant}")

def help_command(update, _):
    update.message.reply_text("Используйте `/start` для тестирования.")
    # для версии 20.x необходимо использовать оператор await
    # await update.message.reply_text("Используйте `/start` для тестирования.")


def main():
    application = Application.builder().token('5822667731:AAF2BwfBkHzk9Di3SoydIF4GMBhKamn8wfA').build()

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button))

    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
