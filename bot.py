import os
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from aigeneration import send_message, show_contexte

load_dotenv()

token = os.getenv('TOKEN')

async def start(update, context):
    await update.message.reply_text("""
    Bienvenu sur le bot de test Python
    Envoyez /site pour recevoir le site      
                                    """)
    
async def lien(update, context):
    await update.message.reply_text("Le lien est https://google.com")

async def question(update, context):
    keyboard = [
        [KeyboardButton("Python"), KeyboardButton("Java")]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

    await update.message.reply_text("Quel est votre langage de programmation préféré ?", reply_markup=reply_markup)

async def youtube(update, context):
    keyboard = [
        [InlineKeyboardButton('Python', 'https://www.youtube.com', 'Python', 'https://www.youtube.com')],
        [InlineKeyboardButton('Python', 'https://www.youtube.com', 'Python', 'https://www.youtube.com')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Que voulez vous apprendre aujourd'hui ?", reply_markup=reply_markup)

async def message_recu(update, context):
    texte = update.message.text

    if texte.lower() == "hello":
        await update.message.reply_text("Salut 👋")
    elif texte.lower() == "context":
        await update.message.reply_text(f"{show_contexte()} hello")
    else:
        reponse = send_message(texte)
        await update.message.reply_text(reponse)


if __name__ == '__main__':
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('lien', lien))
    app.add_handler(CommandHandler('question', question))
    app.add_handler(CommandHandler('youtube', youtube))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_recu))

    app.run_polling(poll_interval=5)
