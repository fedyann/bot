import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    chat_id = update.message.chat_id
    photo_file = open('images/meme.jpg', 'rb')
    try:
        await context.bot.send_photo(chat_id=chat_id, photo=photo_file)
        logging.info('Photo sent successfully.')
    except telegram.TelegramError as e:
        logging.error(f'Error sending photo: {e}')
    finally:
        photo_file.close()


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет, {user.mention_html()}! Я помогу тебе сделать твой собственный мем. Сначала выбери шаблон!",
    )


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я пока не умею помогать...")


def main():
    application = Application.builder().token('5822667731:AAF2BwfBkHzk9Di3SoydIF4GMBhKamn8wfA').build()

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
