import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def send_text(update, context):
    chat_id = update.message.chat_id





async def start(update, context):
    user = update.effective_user
    chat_id = update.message.chat_id

    await update.message.reply_html(
        rf"Привет, {user.mention_html()}! Я помогу тебе сделать твой собственный мем. Сначала выбери шаблон!",
    )
    with open('images/mem_1.jpg', 'rb') as photo_file:
        await context.bot.send_photo(chat_id=chat_id, photo=photo_file)
        await update.message.reply_text("1")
    with open('images/mem_2.jpg', 'rb') as photo_file:
        await context.bot.send_photo(chat_id=chat_id, photo=photo_file)
        await update.message.reply_text("2")
    with open('images/meme.jpg', 'rb') as photo_file:
        await context.bot.send_photo(chat_id=chat_id, photo=photo_file)
        await update.message.reply_text("3")


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я пока не умею помогать...")


def main():
    application = Application.builder().token('5822667731:AAF2BwfBkHzk9Di3SoydIF4GMBhKamn8wfA').build()

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, send_text)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
