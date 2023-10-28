from typing import Final
from telegram import Update 
from datetime import datetime
from telegram.ext import Application , CommandHandler, MessageHandler , filters , ContextTypes, CallbackQueryHandler ,CallbackContext
import urllib
import webbrowser


TOKEN: Final = '6968096470:AAE6PMREC3v69IT5BT_9aqVIqPGT3EKdlVU'
BOT_USERNAME : Final = '@dr_sauce_the_bot'

#command
async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey there I am docttor sauce i cook beats!\nwhat beat would u like to make??")
    
async def help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("help")
    
async def custom_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("custom")
    return urllib.urlopen('https://t.me/dr_sauce_the_bot/Testing_app')

async def game_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("starting game")
    webbrowser.open('https://t.me/dr_sauce_the_bot/Testing_app')

    
    
#responses

def handle_responses(text:str) -> str:
    processed : str = text.lower()
    if 'start' in processed or 'help' in processed or 'custom' in processed:
        return datetime.now
    else:
        return 'please check menu for actions'
    
    
async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type : str = update.message.chat.type
    text : str = update.message.text
    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text : str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_responses(new_text)
        else:
            return 
    else:
        response:str = handle_responses(text)
    print('BOT: ',response)
    await update.message.reply_text(response)
    
    
async def error(pdate: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {Update} caused error {context.error}')
    
    
if __name__ == '__main__':
    print('startind sauce')
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))
    app.add_handler(CommandHandler('game',game_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    app.add_error_handler(error)
    
    print('loading sauce')
    app.run_polling(poll_interval=1)
    
    
    
    
    
    