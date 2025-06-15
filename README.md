# 📰 Telegram Crypto News Bot

A bot that delivers real-time cryptocurrency news from multiple sources directly to Telegram.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

## 🌟 Features

- Fetches news from 5+ top crypto sources:
  - Bitcoinist
  - NewsBTC
  - CryptoPotato
  - 99Bitcoins
  - CryptoBriefing
- Clean HTML formatting with direct article links
- Error handling for failed feed requests
- Easy deployment via Render.com

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Telegram bot token from [@BotFather](https://t.me/BotFather)
- Render.com account

### Local Setup
```bash
git clone https://github.com/yourusername/crypto-news-bot.git
cd crypto-news-bot
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
