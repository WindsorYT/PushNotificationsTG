from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from wakeonlan import send_magic_packet

# Конфигурация
BOT_TOKEN = "7322069268:AAFB_sh0ZJNzy0KBRlnwjrjry2fKtHKjrcg"  # Ваш токен
ALLOWED_ID = 7972414861  # Ваш Telegram ID
MAC_ADDRESS = "18-C0-4D-EC-41-5C"  # MAC-адрес компьютера

# Команда для включения компьютера
async def wake_pc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ALLOWED_ID:
        send_magic_packet(MAC_ADDRESS)
        await update.message.reply_text("Компьютер включается!")
    else:
        await update.message.reply_text("У вас нет прав на выполнение этой команды.")

def main():
    # Создайте объект Application с вашим токеном
    application = Application.builder().token(BOT_TOKEN).build()

    # Обработчик команды с латинскими символами
    application.add_handler(CommandHandler("start_computer", wake_pc))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
