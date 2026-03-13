#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import ApplicationBuilder, CommandHandler
import config
from handlers.start import start
from handlers.info import info

def main():
    # Создаём приложение с токеном из конфига
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()

    # Регистрируем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))

    print("🚀 Бот White Lotus запущен и готов к работе...")
    app.run_polling()

if __name__ == "__main__":
    main()
