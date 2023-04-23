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
    number = text[0]
    if number.isdigit() and len(text) >= 3:
        text1, text2 = text[1], text[2]
        photo_file = CreateMem(int(number), text1, text2).text()
        with open(photo_file, 'rb'):
            await context.bot.send_photo(chat_id=chat_id, photo=photo_file)
    else:
        await update.message.reply_text("Выбери шаблон для будущего мема и "
                                        "придумай текст. Ответ пришли одним сообщением в формате:\n"
                                        "номер шаблона\n"
                                        "текст1\n"
                                        "текст2")






async def start(update, context):
    user = update.effective_user
    chat_id = update.message.chat_id

    await update.message.reply_html(
        rf"Привет, {user.mention_html()}! Я помогу тебе сделать твой собственный мем. Сначала выбери шаблон и "
                                    "придумай текст. Ответ пришли одним сообщением в формате:\n"
                                    "номер шаблона\n"
                                    "текст1\n"
                                    "текст2")
    photo_files = [open('images/mem1_text.jpg', 'rb'), open('images/mem2_text.jpg', 'rb')]

    media = [telegram.InputMediaPhoto(photo_file) for photo_file in photo_files]

    await context.bot.send_media_group(chat_id=chat_id, media=media)



async def help_command(update, context):
    await update.message.reply_text("Я помогу тебе сделать твой собственный мем!\n"
                                    "Нажми /start, чтобы начать. Затем выбери шаблон для будущего мема и "
                                    "придумай текст. Ответ пришли одним сообщением в формате:\n"
                                    "номер шаблона\n"
                                    "текст1\n"
                                    "текст2")


def main():
    application = Application.builder().token('5822667731:AAF2BwfBkHzk9Di3SoydIF4GMBhKamn8wfA').build()

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, send_text)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
