# Librairies python Pypi et autres

import os
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

#Mes propres outils :

from Tools.AI.aigeneration import send_message, show_contexte
from Tools.Google.googletask import creer_tache

load_dotenv()

token = os.getenv('TOKEN')

# fonction basique

def extract_command(texte):
    return " ".join(texte.split(" ")[1:])
# fonction telegram

async def start(update, context):
    await update.message.reply_text("""
    Bienvenu sur le bot de test Python
    Envoyez /site pour recevoir le site      
                                    """)
    
    keyboard = [
        [InlineKeyboardButton('Python', 'https://www.youtube.com', 'Python', 'https://www.youtube.com')],
        [InlineKeyboardButton('Python', 'https://www.youtube.com', 'Python', 'https://www.youtube.com')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Que voulez vous apprendre aujourd'hui ?", reply_markup=reply_markup)
async def lien(update, context):
    await update.message.reply_text("Le lien du projet github est : https://github.com/leofargues/hippoca/tree/main")

async def tache(update, context):
    await update.message.reply_text("La tâche ")

async def message_recu(update, context):
    texte = update.message.text

    if texte.lower() == "hello":
        await update.message.reply_text("Salut 👋")
    elif texte.lower() == "context":
        await update.message.reply_text(f"{show_contexte()} hello")
    elif "@" in texte.lower():
        if "task".lower() in texte.lower():
            creer_tache(extract_command(texte))
            await update.message.reply_text(f"La tâche { extract_command(texte) } à été crée ")

    else:
        reponse = send_message(texte)
        await update.message.reply_text(reponse)


if __name__ == '__main__':
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('lien', lien))
    # app.add_handler(CommandHandler('question', question))
    # app.add_handler(CommandHandler('youtube', youtube))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_recu))

    app.run_polling(poll_interval=5)
