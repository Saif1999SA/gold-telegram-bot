import logging
import os
import telebot

# إعدادات اللوج
logging.basicConfig(level=logging.INFO)

# التوكن الخاص بك من BotFather
TOKEN = os.getenv("BOT_TOKEN")  # سيتم ضبطه من متغيرات البيئة في Render

# إنشاء البوت
bot = telebot.TeleBot(TOKEN)

# رسالة الترحيب
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome! I will send you gold (XAUUSD) trade signals here.\nPlease wait for real-time signals based on scalping and swing strategy.")

# إرسال توصية تجريبية
@bot.message_handler(commands=['test'])
def send_test_signal(message):
    bot.send_message(message.chat.id, """
📈 GOLD SIGNAL

💰 Type: BUY  
📍 Entry: 2328.50  
🎯 Target 1: 2331.00  
🎯 Target 2: 2334.00  
🛑 Stop Loss: 2325.80  
⏱️ Timeframe: M15  
🔍 Strategy: RSI Oversold + Bullish engulfing + Support zone
""")

# تشغيل البوت
def main():
    print("Bot is running...")
    bot.infinity_polling()

if __name__ == '__main__':
    main()
