import telebot
from telebot import types
import config
import random

bot = telebot.TeleBot(config.token)

# --- Подробные рецепты по кухням ---
diet_options = {
    "🍣 Японская кухня": [
        {
            "id": 1,
            "name": "🍱 Суши с сырой рыбой",
            "recipe": """Ингредиенты:
- 200 г свежего лосося или тунца
- 150 г риса для суши
- 4 листа нори
- Соевый соус, васаби по вкусу

Приготовление:
1. Промойте рис до прозрачной воды и сварите согласно инструкции.
2. Дайте рису слегка остыть.
3. Нарежьте рыбу тонкими ломтиками.
4. На лист нори выложите тонкий слой риса, сверху — рыбу.
5. Сверните ролл, нарежьте на 6–8 кусочков.
6. Подавайте с соевым соусом и васаби.

💡 Лайфхак: Используйте острый нож, смоченный водой, чтобы роллы нарезались аккуратно.
⏱ Время приготовления: ~30 мин"""
        },
        {
            "id": 2,
            "name": "🥗 Салат с фунчозой и овощами",
            "recipe": """Ингредиенты:
        - 100 г фунчозы
        - 1 огурец
        - 1 морковь
        - Зеленый лук по вкусу
        - 1 ч.л. рисового уксуса
        - 1 ст.л. соевого соуса
        - Кунжут по желанию

        Приготовление:
        1. Отварите фунчозу 3–5 минут, промойте холодной водой.
        2. Нарежьте огурец и морковь тонкой соломкой.
        3. Смешайте овощи с фунчозой, добавьте соус и уксус.
        4. Посыпьте кунжутом и перемешайте.

        💡 Лайфхак: Можно добавить немного свежего имбиря для пикантного вкуса.
        ⏱ Время приготовления: ~15 мин"""
        },
        {
            "id": 3,
            "name": "🍝 Паста с морепродуктами",
            "recipe": """Ингредиенты:
        - 200 г пасты
        - 150 г морепродуктов (креветки, мидии)
        - 2 ст.л. оливкового масла
        - 2 зубчика чеснока
        - Соль, перец по вкусу

        Приготовление:
        1. Отварите пасту до состояния аль денте.
        2. Обжарьте чеснок на оливковом масле 1–2 минуты.
        3. Добавьте морепродукты, обжаривайте 5–7 минут.
        4. Смешайте с пастой, посолите и поперчите.

        💡 Лайфхак: Для насыщенного вкуса добавьте немного лимонного сока.
        ⏱ Время приготовления: ~20 мин"""
        }
    ],
    "🥖 Русская кухня": [
        {
            "id": 2,
            "name": "🥗 Салат с фунчозой и овощами",
            "recipe": """Ингредиенты:
        - 100 г фунчозы
        - 1 огурец
        - 1 морковь
        - Зеленый лук по вкусу
        - 1 ч.л. рисового уксуса
        - 1 ст.л. соевого соуса
        - Кунжут по желанию

        Приготовление:
        1. Отварите фунчозу 3–5 минут, промойте холодной водой.
        2. Нарежьте огурец и морковь тонкой соломкой.
        3. Смешайте овощи с фунчозой, добавьте соус и уксус.
        4. Посыпьте кунжутом и перемешайте.

        💡 Лайфхак: Можно добавить немного свежего имбиря для пикантного вкуса.
        ⏱ Время приготовления: ~15 мин"""
        },
        {
            "id": 3,
            "name": "🍝 Паста с морепродуктами",
            "recipe": """Ингредиенты:
        - 200 г пасты
        - 150 г морепродуктов (креветки, мидии)
        - 2 ст.л. оливкового масла
        - 2 зубчика чеснока
        - Соль, перец по вкусу

        Приготовление:
        1. Отварите пасту до состояния аль денте.
        2. Обжарьте чеснок на оливковом масле 1–2 минуты.
        3. Добавьте морепродукты, обжаривайте 5–7 минут.
        4. Смешайте с пастой, посолите и поперчите.

        💡 Лайфхак: Для насыщенного вкуса добавьте немного лимонного сока.
        ⏱ Время приготовления: ~20 мин"""
        }
    ],
    "🍝 Итальянская кухня": [
        {
            "id": 2,
            "name": "🥗 Салат с фунчозой и овощами",
            "recipe": """Ингредиенты:
        - 100 г фунчозы
        - 1 огурец
        - 1 морковь
        - Зеленый лук по вкусу
        - 1 ч.л. рисового уксуса
        - 1 ст.л. соевого соуса
        - Кунжут по желанию

        Приготовление:
        1. Отварите фунчозу 3–5 минут, промойте холодной водой.
        2. Нарежьте огурец и морковь тонкой соломкой.
        3. Смешайте овощи с фунчозой, добавьте соус и уксус.
        4. Посыпьте кунжутом и перемешайте.

        💡 Лайфхак: Можно добавить немного свежего имбиря для пикантного вкуса.
        ⏱ Время приготовления: ~15 мин"""
        },
        {
            "id": 3,
            "name": "🍝 Паста с морепродуктами",
            "recipe": """Ингредиенты:
        - 200 г пасты
        - 150 г морепродуктов (креветки, мидии)
        - 2 ст.л. оливкового масла
        - 2 зубчика чеснока
        - Соль, перец по вкусу

        Приготовление:
        1. Отварите пасту до состояния аль денте.
        2. Обжарьте чеснок на оливковом масле 1–2 минуты.
        3. Добавьте морепродукты, обжаривайте 5–7 минут.
        4. Смешайте с пастой, посолите и поперчите.

        💡 Лайфхак: Для насыщенного вкуса добавьте немного лимонного сока.
        ⏱ Время приготовления: ~20 мин"""
        }
    ],
    "🇪🇸 Испанская кухня": [
        {
            "id": 2,
            "name": "🥗 Салат с фунчозой и овощами",
            "recipe": """Ингредиенты:
        - 100 г фунчозы
        - 1 огурец
        - 1 морковь
        - Зеленый лук по вкусу
        - 1 ч.л. рисового уксуса
        - 1 ст.л. соевого соуса
        - Кунжут по желанию

        Приготовление:
        1. Отварите фунчозу 3–5 минут, промойте холодной водой.
        2. Нарежьте огурец и морковь тонкой соломкой.
        3. Смешайте овощи с фунчозой, добавьте соус и уксус.
        4. Посыпьте кунжутом и перемешайте.

        💡 Лайфхак: Можно добавить немного свежего имбиря для пикантного вкуса.
        ⏱ Время приготовления: ~15 мин"""
        },
        {
            "id": 3,
            "name": "🍝 Паста с морепродуктами",
            "recipe": """Ингредиенты:
        - 200 г пасты
        - 150 г морепродуктов (креветки, мидии)
        - 2 ст.л. оливкового масла
        - 2 зубчика чеснока
        - Соль, перец по вкусу

        Приготовление:
        1. Отварите пасту до состояния аль денте.
        2. Обжарьте чеснок на оливковом масле 1–2 минуты.
        3. Добавьте морепродукты, обжаривайте 5–7 минут.
        4. Смешайте с пастой, посолите и поперчите.

        💡 Лайфхак: Для насыщенного вкуса добавьте немного лимонного сока.
        ⏱ Время приготовления: ~20 мин"""
        }
    ],
    "🇮🇳 Индийская кухня": [
        {
            "id": 2,
            "name": "🥗 Салат с фунчозой и овощами",
            "recipe": """Ингредиенты:
        - 100 г фунчозы
        - 1 огурец
        - 1 морковь
        - Зеленый лук по вкусу
        - 1 ч.л. рисового уксуса
        - 1 ст.л. соевого соуса
        - Кунжут по желанию

        Приготовление:
        1. Отварите фунчозу 3–5 минут, промойте холодной водой.
        2. Нарежьте огурец и морковь тонкой соломкой.
        3. Смешайте овощи с фунчозой, добавьте соус и уксус.
        4. Посыпьте кунжутом и перемешайте.

        💡 Лайфхак: Можно добавить немного свежего имбиря для пикантного вкуса.
        ⏱ Время приготовления: ~15 мин"""
        },
        {
            "id": 3,
            "name": "🍝 Паста с морепродуктами",
            "recipe": """Ингредиенты:
        - 200 г пасты
        - 150 г морепродуктов (креветки, мидии)
        - 2 ст.л. оливкового масла
        - 2 зубчика чеснока
        - Соль, перец по вкусу

        Приготовление:
        1. Отварите пасту до состояния аль денте.
        2. Обжарьте чеснок на оливковом масле 1–2 минуты.
        3. Добавьте морепродукты, обжаривайте 5–7 минут.
        4. Смешайте с пастой, посолите и поперчите.

        💡 Лайфхак: Для насыщенного вкуса добавьте немного лимонного сока.
        ⏱ Время приготовления: ~20 мин"""
        }
    ]
}

# --- Лёгкие рецепты ---
easy_recipes = [
    {
        "name": "🍳 Омлет с овощами",
        "recipe": """Ингредиенты:
- 2 яйца
- 50 г шпината
- 1 помидор
- Соль, перец по вкусу
- 1 ч.л. масла

Приготовление:
1. Взбейте яйца с солью и перцем.
2. Нарежьте помидор и шпинат.
3. Разогрейте сковороду с маслом, обжарьте овощи 1–2 минуты.
4. Влейте яйца и готовьте на медленном огне 3–4 минуты.
💡 Лайфхак: Накройте сковороду крышкой, омлет будет пышным.
⏱ Время приготовления: ~5 мин"""
    },
    {
        "id": 2,
        "name": "🥗 Салат с фунчозой и овощами",
        "recipe": """Ингредиенты:
    - 100 г фунчозы
    - 1 огурец
    - 1 морковь
    - Зеленый лук по вкусу
    - 1 ч.л. рисового уксуса
    - 1 ст.л. соевого соуса
    - Кунжут по желанию

    Приготовление:
    1. Отварите фунчозу 3–5 минут, промойте холодной водой.
    2. Нарежьте огурец и морковь тонкой соломкой.
    3. Смешайте овощи с фунчозой, добавьте соус и уксус.
    4. Посыпьте кунжутом и перемешайте.

    💡 Лайфхак: Можно добавить немного свежего имбиря для пикантного вкуса.
    ⏱ Время приготовления: ~15 мин"""
    },
    {
        "id": 3,
        "name": "🍝 Паста с морепродуктами",
        "recipe": """Ингредиенты:
    - 200 г пасты
    - 150 г морепродуктов (креветки, мидии)
    - 2 ст.л. оливкового масла
    - 2 зубчика чеснока
    - Соль, перец по вкусу

    Приготовление:
    1. Отварите пасту до состояния аль денте.
    2. Обжарьте чеснок на оливковом масле 1–2 минуты.
    3. Добавьте морепродукты, обжаривайте 5–7 минут.
    4. Смешайте с пастой, посолите и поперчите.

    💡 Лайфхак: Для насыщенного вкуса добавьте немного лимонного сока.
    ⏱ Время приготовления: ~20 мин"""
    }
]

about_text = "Я — ваш личный диетолог-ассистент! 🍎🥗\nПомогу выбрать диету по вкусам и целям и дам подробные рецепты с лайфхаками."

# --- Подготовка всех рецептов для случайного выбора и топ-5 ---
all_recipes_list = [f"{item['name']}:\n{item['recipe']}" for cuisine in diet_options.values() for item in cuisine] + [f"{r['name']}:\n{r['recipe']}" for r in easy_recipes]

# --- Главное меню ---
def main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🍴 Диеты", "ℹ️ Для чего этот бот?", "🎲 Случайный рецепт")
    markup.row("⭐ Топ-5 рецептов", "🧮 Калькулятор БЖУ")
    bot.send_message(chat_id, "Главное меню", reply_markup=markup)

# --- Меню кухонь ---
def cuisine_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    row = []
    for i, cuisine in enumerate(diet_options.keys(), 1):
        row.append(cuisine)
        if i % 2 == 0:
            markup.row(*row)
            row = []
    if row:
        markup.row(*row)
    markup.row("🥗 Лёгкие рецепты")  # новая кнопка
    markup.row("🎲 Случайный рецепт", "⭐ Топ-5 рецептов")
    markup.add("⬅️ Назад")
    bot.send_message(chat_id, "Выберите кухню или рецепт:", reply_markup=markup)

# --- Инлайн-кнопки рецептов ---
def send_cuisine_recipes(chat_id, cuisine_name):
    markup = types.InlineKeyboardMarkup()
    for item in diet_options[cuisine_name]:
        markup.add(types.InlineKeyboardButton(text=item["name"], callback_data=f"recipe_{item['id']}"))
    markup.add(types.InlineKeyboardButton("⬅️ Назад к меню кухонь", callback_data="back_to_cuisine"))
    bot.send_message(chat_id, f"Выберите рецепт из {cuisine_name}:", reply_markup=markup)

# --- Показ лёгких рецептов ---
def send_easy_recipes(chat_id):
    markup = types.InlineKeyboardMarkup()
    for i, r in enumerate(easy_recipes):
        markup.add(types.InlineKeyboardButton(text=f"{r['name']}", callback_data=f"easy_{i}"))
    markup.add(types.InlineKeyboardButton("⬅️ Назад к меню кухонь", callback_data="back_to_cuisine"))
    bot.send_message(chat_id, "Выберите лёгкий рецепт:", reply_markup=markup)

# --- Калькулятор БЖУ с целями ---
# --- Калькулятор БЖУ с возможностью выхода в главное меню ---
def start_bju_calculator(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("⬅️ Главное меню")
    msg = bot.send_message(chat_id, "Введите ваш вес в кг:", reply_markup=markup)
    bot.register_next_step_handler(msg, bju_weight_step)

def bju_weight_step(message):
    if message.text == "⬅️ Главное меню":
        main_menu(message.chat.id)
        return
    try:
        weight = float(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Главное меню")
        msg = bot.send_message(message.chat.id, "Введите ваш рост в см:", reply_markup=markup)
        bot.register_next_step_handler(msg, bju_height_step, weight)
    except ValueError:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Главное меню")
        msg = bot.send_message(message.chat.id, "Введите число для веса.", reply_markup=markup)
        bot.register_next_step_handler(msg, bju_weight_step)

def bju_height_step(message, weight):
    if message.text == "⬅️ Главное меню":
        main_menu(message.chat.id)
        return
    try:
        height = float(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Главное меню")
        msg = bot.send_message(message.chat.id, "Введите ваш возраст:", reply_markup=markup)
        bot.register_next_step_handler(msg, bju_age_step, weight, height)
    except ValueError:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Главное меню")
        msg = bot.send_message(message.chat.id, "Введите число для роста.", reply_markup=markup)
        bot.register_next_step_handler(msg, bju_height_step, weight)

def bju_age_step(message, weight, height):
    if message.text == "⬅️ Главное меню":
        main_menu(message.chat.id)
        return
    try:
        age = int(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Главное меню")
        msg = bot.send_message(message.chat.id, "Введите ваш пол (м/ж):", reply_markup=markup)
        bot.register_next_step_handler(msg, bju_gender_step, weight, height, age)
    except ValueError:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Главное меню")
        msg = bot.send_message(message.chat.id, "Введите число для возраста.", reply_markup=markup)
        bot.register_next_step_handler(msg, bju_age_step, weight, height)

def bju_gender_step(message, weight, height, age):
    if message.text == "⬅️ Главное меню":
        main_menu(message.chat.id)
        return
    gender = message.text.lower()
    if gender not in ["м", "ж"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Главное меню")
        msg = bot.send_message(message.chat.id, "Введите 'м' для мужчины или 'ж' для женщины.", reply_markup=markup)
        bot.register_next_step_handler(msg, bju_gender_step, weight, height, age)
        return

    if gender == "м":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("⬅️ Главное меню")
    markup.row("Снижение веса", "Поддержание веса", "Набор массы")
    msg = bot.send_message(message.chat.id, "Выберите вашу цель:", reply_markup=markup)
    bot.register_next_step_handler(msg, bju_goal_step, bmr)

def bju_goal_step(message, bmr):
    if message.text == "⬅️ Главное меню":
        main_menu(message.chat.id)
        return
    goal = message.text
    if goal == "Снижение веса":
        bmr *= 0.8
    elif goal == "Поддержание веса":
        bmr *= 1.0
    elif goal == "Набор массы":
        bmr *= 1.15
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Главное меню")
        markup.row("Снижение веса", "Поддержание веса", "Набор массы")
        msg = bot.send_message(message.chat.id, "Выберите цель кнопкой.", reply_markup=markup)
        bot.register_next_step_handler(msg, bju_goal_step, bmr)
        return

    protein = round((bmr * 0.3 / 4), 1)
    fat = round((bmr * 0.3 / 9), 1)
    carbs = round((bmr * 0.4 / 4), 1)

    bot.send_message(message.chat.id,
                     f"Калорийность с учётом цели: {round(bmr)} ккал\n"
                     f"Распределение БЖУ:\n"
                     f"Белки: {protein} г\n"
                     f"Жиры: {fat} г\n"
                     f"Углеводы: {carbs} г")
    main_menu(message.chat.id)  # возвращаем в главное меню после расчёта
# --- Универсальная функция назад ---
def go_back(chat_id, target):
    if target == "main":
        main_menu(chat_id)
    elif target == "cuisine":
        cuisine_menu(chat_id)

# --- Старт ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот-диетолог. 🥗 Выбирайте меню через кнопки.")
    main_menu(message.chat.id)

# --- Обработка сообщений ---
@bot.message_handler(func=lambda m: True)
def handle_message(message):
    text = message.text
    if text == "🍴 Диеты":
        cuisine_menu(message.chat.id)
    elif text == "⬅️ Назад":
        go_back(message.chat.id, "main")
    elif text == "ℹ️ Для чего этот бот?":
        bot.send_message(message.chat.id, about_text)
    elif text == "🎲 Случайный рецепт":
        recipe = random.choice(all_recipes_list)
        bot.send_message(message.chat.id, f"Случайный рецепт:\n\n{recipe}")
    elif text == "⭐ Топ-5 рецептов":
        top_recipes = random.sample(all_recipes_list, 5)
        bot.send_message(message.chat.id, "Топ-5 рецептов:\n\n" + "\n\n".join(top_recipes))
    elif text == "🥗 Лёгкие рецепты":
        send_easy_recipes(message.chat.id)
    elif text == "🧮 Калькулятор БЖУ":
        start_bju_calculator(message.chat.id)
    elif text in diet_options:
        send_cuisine_recipes(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используйте кнопки меню. 😊")

# --- Обработка нажатий инлайн-кнопок ---
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data.startswith("recipe_"):
        recipe_id = int(call.data.split("_")[1])
        for cuisine_recipes in diet_options.values():
            for item in cuisine_recipes:
                if item["id"] == recipe_id:
                    markup = types.InlineKeyboardMarkup()
                    markup.add(types.InlineKeyboardButton("⬅️ Назад к меню кухонь", callback_data="back_to_cuisine"))
                    bot.send_message(call.message.chat.id, f"{item['name']}:\n\n{item['recipe']}", reply_markup=markup)
                    return
    elif call.data.startswith("easy_"):
        index = int(call.data.split("_")[1])
        r = easy_recipes[index]
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("⬅️ Назад к меню кухонь", callback_data="back_to_cuisine"))
        bot.send_message(call.message.chat.id, f"{r['name']}:\n\n{r['recipe']}", reply_markup=markup)
    elif call.data == "back_to_cuisine":
        go_back(call.message.chat.id, "cuisine")

# --- Запуск бота ---
bot.polling(none_stop=True, interval=0)
