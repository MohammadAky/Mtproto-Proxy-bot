from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, Application, CallbackQueryHandler
from bot.utils.decorators import admin_only
from bot.keyboards.inline import main_menu_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"👋 Hello <b>{user.first_name}</b>!\n\n"
        "🔧 <b>MTProto Proxy Manager Bot</b>\n\n"
        "Use the menu below to manage your proxies.",
        parse_mode="HTML",
        reply_markup=main_menu_keyboard(),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 <b>Commands:</b>\n\n"
        "/start - Show main menu\n"
        "/help - Show this help\n"
        "/create - Create a new proxy\n"
        "/list - List all proxies\n"
        "/delete &lt;id&gt; - Delete a proxy\n"
        "/status - System status\n",
        parse_mode="HTML",
    )


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks"""
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    
    # Route to appropriate handler based on button pressed
    if callback_data == "create":
        from bot.handlers.proxy import create_proxy_start
        await create_proxy_start(update, context)
    elif callback_data == "list":
        from bot.handlers.proxy import list_proxies
        await list_proxies(update, context)
    elif callback_data == "status":
        from bot.handlers.admin import status
        await status(update, context)


def register_common_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_callback, pattern="^(create|list|status)$"))