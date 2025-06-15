import os
import feedparser
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")  # 🔴 Remove extra quote if present
RSS_FEEDS = {
    "Bitcoinist": "https://bitcoinist.com/feed/",
    "NewsBTC": "https://www.newsbtc.com/feed/",
    "CryptoPotato": "https://cryptopotato.com/feed/",
    "99Bitcoins": "https://99bitcoins.com/feed/",
    "CryptoBriefing": "https://cryptobriefing.com/feed/"
}

def crypto_news(update: Update, context: CallbackContext):
    for name, url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(url)
            update.message.reply_text(f"<b>📰 {name} Headlines:</b>", parse_mode="HTML")
            for entry in feed.entries[:3]:
                message = f"• <a href='{entry.link}'>{entry.title}</a>"
                update.message.reply_text(message, parse_mode="HTML")
        except Exception as e:
            update.message.reply_text(f"❌ Failed to fetch {name} news: {str(e)}")

if __name__ == "__main__":
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("crypto", crypto_news))
    updater.start_polling()
    updater.idle()
