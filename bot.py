import telebot
from telebot import types

TOKEN = "8553170140:AAEdhQNNueurWd1A1xBwC7DFQJa2ftlH_fU"

bot = telebot.TeleBot(TOKEN)


# ===== /start =====
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(
        types.KeyboardButton("🛒 Товари"),
        types.KeyboardButton("📦 Замовлення")
    )
    keyboard.add(
        types.KeyboardButton("📞 Контакти"),
        types.KeyboardButton("ℹ️ Про магазин")
    )

    bot.send_message(
        message.chat.id,
        "👋 Вітаємо в магазині *Shop*!\n\n"
        "Оберіть, що вас цікавить ⬇️",
        parse_mode="Markdown",
        reply_markup=keyboard
    )


# ===== товари =====
@bot.message_handler(func=lambda m: m.text == "🛒 Товари")
def products(message):
    bot.send_message(
        message.chat.id,
        "🛒 Наші популярні товари:\n"
        "• Мотоцикли\n"
        "• Мінитрактори\n"
        "• Квадроцикли\n"
        "• Запчастини\n\n"
        "🌐 Переглянути на сайті:\n"
        "http://localhost:8000/products/"
    )


# ===== замовлення =====
@bot.message_handler(func=lambda m: m.text == "📦 Замовлення")
def orders(message):
    bot.send_message(
        message.chat.id,
        "📦 Щоб оформити замовлення:\n"
        "1️⃣ Оберіть товар на сайті\n"
        "2️⃣ Натисніть «Додати в кошик»\n"
        "3️⃣ Перейдіть до кошика\n\n"
        "Або напишіть нам назву товару 👇"
    )


# ===== номер телефона =====
@bot.message_handler(func=lambda m: m.text == "📞 Контакти")
def contacts(message):
    bot.send_message(
        message.chat.id,
        "📞 Контакти магазину Shop:\n\n"
        "Телефон: +380 98 538 67 00\n"
        "Графік: Пн–Пт 09:00–18:00\n\n"
        "Ми завжди на звʼязку 🙂"
    )


# ===== Інфо=====
@bot.message_handler(func=lambda m: m.text == "ℹ️ Про магазин")
def about(message):
    bot.send_message(
        message.chat.id,
        "ℹ️ *Shop* — навчальний інтернет-магазин.\n\n"
        "Тут ви можете:\n"
        "✔️ переглядати товари\n"
        "✔️ оформлювати замовлення\n"
        "✔️ звʼязатися з підтримкою\n\n"
        "Дякуємо, що ви з нами 💚",
        parse_mode="Markdown"
    )


@bot.message_handler(func=lambda message: True)
def any_text(message):
    bot.send_message(
        message.chat.id,
        "🤖 Я вас почув!\n"
        "Оберіть пункт у меню ⬇️ або напишіть своє питання."
    )


print("🤖 Bot is running...")
bot.polling()
