from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7557343046:AAHstwesgNK62S7PkDOOn-WtMIMzqwva0aw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Press me", callback_data="hello")]]
        await update.message.reply_text(
                "Test",
                        reply_markup=InlineKeyboardMarkup(keyboard)
                            )

                            async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                query = update.callback_query
                                    print("BUTTON:", query.data)
                                        await query.answer()
                                            await query.edit_message_text("Worked!")

                                            app = Application.builder().token(TOKEN).build()

                                            app.add_handler(CommandHandler("start", start))
                                            app.add_handler(CallbackQueryHandler(button))

                                            app.run_polling()