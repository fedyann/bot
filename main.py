import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
import telegram
from text_to_image import CreateMem

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def send_text(update, context):
    chat_id = update.message.chat_id
    text = update.message.text.split('\n')
    number, text1, text2 = text[0], text[1], text[2]
    if number.isdigit():
        photo_file = CreateMem(int(number), text1, text2).text()
        with open(photo_file, 'rb'):
            await context.bot.send_photo(chat_id=chat_id, photo=photo_file)





async def start(update, context):
    user = update.effective_user
    chat_id = update.message.chat_id

    await update.message.reply_html(
        rf"Привет, {user.mention_html()}! Я помогу тебе сделать твой собственный мем. Сначала выбери шаблон!",
    )
    photo_files = [open('images/mem1.jpg', 'rb'), open('images/mem2.jpg', 'rb')]

    media = [telegram.InputMediaPhoto(photo_file) for photo_file in photo_files]

    await context.bot.send_media_group(chat_id=chat_id, media=media)



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
