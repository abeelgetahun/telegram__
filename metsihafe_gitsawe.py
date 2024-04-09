# this is ("ab_el")
# telegram bot for ethiopian orthodox tewahdo church 
import os 
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler,filters,ContextTypes
from decouple import config
Token:Final=config("Token")
BOT_USERNAME: Final ="@metsihafe_gitsaweBot"

async def start_command(update: Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello")


def handle_response(text:str)->str:
    proccessed:str=text.lower()
    if "hello" in proccessed:
        return "ኣቤት"
    if "amen" in  proccessed:
        return "ኣሜን"
    return "I dont understand what you wrote "
async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type:str=update.message.chat.type
    text:str =update.message.text 

    print (f'User({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type=="group":
        if BOT_USERNAME in text:
            new_text:str =text.replace(BOT_USERNAME,"").strip()
            response:str=handle_response(new_text)
        else:
            return 
    else:
        response:str =handle_response(text)
    print("bot:" , response)
    await update.message.reply_text(response)

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__=="__main__":
    print("starting bot...")
    app=Application.builder().token(Token).build()
    # commands
    app.add_handler(CommandHandler("start",start_command))
    # Message handler
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    # Error handler
    app.add_error_handler(error)

    # polls 
    print("polling...")
    app.run_polling(poll_interval=3)