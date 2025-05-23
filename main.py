import logging
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "
7981544996:AAHAW0dbmk4hl4MlJO8p5RT5UKom1NaKr4I"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start_message():
    return (
        "👋 Benvingut/da a *Veïns Units Lleida!*\n\n"
        "Aquest bot t'ajuda a trobar el teu grup de barri i mantenir-te informat.\n\n"
        "👉 Escriu /barri per veure la llista de grups per barri.\n"
        "👉 Escriu /ajuda per més opcions."
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown_v2(start_message())

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandes disponibles:\n"
        "/start – Missatge de benvinguda\n"
        "/barri – Mostra els grups de cada barri\n"
        "/ajuda – Mostra aquest missatge"
    )

async def barri(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 Grups per barri de Lleida:\n"
        "- Balàfia → t.me/SeguretatBalafia\n"
        "- Cappont → t.me/SeguretatCappont\n"
        "- Pardinyes → t.me/SeguretatPardinyes\n"
        "- Centre Històric → t.me/SeguretatCentreHistoric\n"
        "- Mariola → t.me/SeguretatMariola\n"
        "- La Bordeta → t.me/SeguretatBordeta\n"
        "- Noguerola → t.me/SeguretatNoguerola\n"
        "- Rambla Ferran → t.me/SeguretatRamblaFerran\n"
        "- Secà de Sant Pere → t.me/SeguretatSacaSantPere"
    )

async def filtrar_missatges(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contingut = update.message.text.lower()
    paraules_prohibides = ["puta", "merda", "imbècil", "subnormal"]
    if any(paraula in contingut for paraula in paraules_prohibides):
        await update.message.delete()
        await update.message.reply_text("⚠️ El teu missatge ha estat eliminat per contingut ofensiu.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajuda", ajuda))
    app.add_handler(CommandHandler("barri", barri))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filtrar_missatges))
    app.run_polling()
