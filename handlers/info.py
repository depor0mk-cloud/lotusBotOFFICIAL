from telegram import Update
from telegram.ext import ContextTypes

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📋 **Список доступных команд:**\n\n"
        "/start — Приветствие\n"
        "/info — Эта справка\n"
        "/создать клан [название] [тег] — Создать новый клан\n"
        "/вступить [название/тег/номер] — Подать заявку или вступить в клан\n"
        "/выйти — Покинуть клан\n"
        "/удалить клан — Удалить клан (только лидер)\n"
        "/мой клан — Информация о вашем клане\n"
        "/список кланов — Список всех кланов\n"
        "/правила — Правила игры\n\n"
        "⚔️ Военные и экономические команды будут добавлены позже."
    )
    await update.message.reply_text(text, parse_mode='Markdown')
