from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "توکن_ربات_تو_اینجا"  # <-- اینو بعدا با توکن خودت جایگزین کن

voters = set()  # ذخیره اسامی کسانی که رأی دادن

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("رأی دادن", callback_data="vote")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("برای رأی دادن روی دکمه زیر بزن:", reply_markup=reply_markup)

async def vote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    if user.username not in voters:
        voters.add(user.username)
        await query.answer("رأی شما ثبت شد ✅")
    else:
        await query.answer("شما قبلا رأی داده‌اید ⚠️")
    
    # نمایش لیست کسانی که رأی داده‌اند
    print("اسامی رأی‌دهنده‌ها:", voters)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(vote, pattern="vote"))

app.run_polling()
