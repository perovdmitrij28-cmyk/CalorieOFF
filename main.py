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
            "id": 4,
            "name": "🥬 Зеленый борщ без картофеля",
            "recipe": """Ингредиенты:
        - 100 г щавеля или шпината
        - 1 огурец
        - 2 яйца
        - 200 мл кефира
        - Зелень по вкусу

        Приготовление:
        1. Отварите яйца вкрутую.
        2. Нарежьте щавель и огурец.
        3. Смешайте овощи с кефиром.
        4. Добавьте нарезанные яйца и зелень перед подачей.

        💡 Лайфхак: Используйте свежий щавель для кислого аромата.
        ⏱ Время приготовления: ~15 мин"""
        },
        {
            "id": 5,
            "name": "🥗 Овощной салат с квашеной капустой",
            "recipe": """Ингредиенты:
        - 1 свежий огурец
        - 1 помидор
        - 100 г квашеной капусты
        - 1 ст.л. оливкового масла

        Приготовление:
        1. Нарежьте овощи кубиками.
        2. Смешайте с капустой.
        3. Заправьте оливковым маслом.

        💡 Лайфхак: Добавьте немного зелени и семян льна для пользы.
        ⏱ Время приготовления: ~10 мин"""
        },
        {
            "id": 6,
            "name": "🌸 Запеченная цветная капуста",
            "recipe": """Ингредиенты:
        - 1 головка цветной капусты
        - 2 зубчика чеснока
        - 2 ст.л. оливкового масла
        - Соль, перец по вкусу

        Приготовление:
        1. Разделите капусту на соцветия.
        2. Смешайте с маслом, солью, перцем и измельченным чесноком.
        3. Запеките при 200°C 20 минут.

        💡 Лайфхак: Добавьте немного паприки для аромата и цвета.
        ⏱ Время приготовления: ~25 мин"""
        }
    ],
    "🍝 Итальянская кухня": [
        {
            "id": 7,
            "name": "🍝 Спагетти с оливковым маслом",
            "recipe": """Ингредиенты:
        - 200 г спагетти
        - 2 ст.л. оливкового масла
        - 2 зубчика чеснока
        - Петрушка для украшения

        Приготовление:
        1. Отварите спагетти до аль денте.
        2. Обжарьте чеснок на масле 1–2 минуты.
        3. Смешайте с пастой и украсьте петрушкой.

        💡 Лайфхак: Используйте свежую петрушку и немного тертого пармезана.
        ⏱ Время приготовления: ~15 мин"""
        },
        {
            "id": 8,
            "name": "🦐 Морепродукты",
            "recipe": """Ингредиенты:
        - 150 г креветок
        - 100 г мидий
        - Сок лимона по вкусу

        Приготовление:
        1. Обжарьте морепродукты 5–7 минут.
        2. Подавайте с лимоном.

        💡 Лайфхак: Можно добавить немного острого перца для пикантности.
        ⏱ Время приготовления: ~10 мин"""
        },
        {
            "id": 9,
            "name": "🥘 Рататуй",
            "recipe": """Ингредиенты:
        - 1 баклажан
        - 1 кабачок
        - 1 красный перец
        - 2 помидора
        - 2 ст.л. оливкового масла

        Приготовление:
        1. Нарежьте все овощи кубиками.
        2. Тушите с маслом и специями 20 минут.

        💡 Лайфхак: Добавьте тимьян и базилик для итальянского вкуса.
        ⏱ Время приготовления: ~25 мин"""
        }
    ],
    "🇪🇸 Испанская кухня": [
        {
            "id": 10,
            "name": "🥪 Тапас с оливками и хамоном",
            "recipe": """Ингредиенты:
        - 50 г хамона
        - 10 оливок
        - Тонкий хлеб

        Приготовление:
        1. Нарежьте хамон и хлеб.
        2. Выложите на хлеб, украсьте оливками.

        💡 Лайфхак: Подайте с бокалом красного вина.
        ⏱ Время приготовления: ~5 мин"""
        },
        {
            "id": 11,
            "name": "🍲 Паэлья с морепродуктами",
            "recipe": """Ингредиенты:
        - 150 г риса
        - 150 г морепродуктов
        - Шафран, специи, овощи

        Приготовление:
        1. Обжарьте морепродукты.
        2. Добавьте рис, специи и овощи, тушите до готовности.

        💡 Лайфхак: Используйте паэльницу для равномерного приготовления.
        ⏱ Время приготовления: ~30 мин"""
        },
        {
            "id": 12,
            "name": "🥘 Испанское овощное рагу",
            "recipe": """Ингредиенты:
        - 1 помидор
        - 1 перец
        - 1 морковь
        - 1 баклажан
        - Масло, специи

        Приготовление:
        1. Нарежьте овощи.
        2. Тушите с маслом и специями до мягкости.

        💡 Лайфхак: Добавьте немного чеснока и свежей зелени для аромата.
        ⏱ Время приготовления: ~20 мин"""
        }
    ],
    "🇮🇳 Индийская кухня": [
        {
            "id": 13,
            "name": "🍛 Дал с рисом",
            "recipe": """Ингредиенты:
        - 150 г чечевицы
        - 100 г риса
        - 1 лук, 1 помидор
        - Куркума, кумин

        Приготовление:
        1. Варите чечевицу с луком, помидором и специями 20 минут.
        2. Подавайте с отварным рисом.

        💡 Лайфхак: Можно добавить щепотку гарам масала для аромата.
        ⏱ Время приготовления: ~30 мин"""
        },
        {
            "id": 14,
            "name": "🍗 Курица тика масала",
            "recipe": """Ингредиенты:
        - 200 г курицы
        - Йогурт, специи, томатная паста

        Приготовление:
        1. Замаринуйте курицу в йогурте со специями 30 минут.
        2. Обжарьте, затем тушите с томатной пастой 15–20 минут.

        💡 Лайфхак: Для мягкой курицы используйте йогурт без сахара.
        ⏱ Время приготовления: ~50 мин"""
        },
        {
            "id": 15,
            "name": "🥗 Салат Коха",
            "recipe": """Ингредиенты:
        - 1 огурец
        - Мята
        - Сок лимона
        - Соль

        Приготовление:
        1. Нарежьте огурец.
        2. Добавьте мяту, лимонный сок и соль.
        3. Перемешайте и подавайте.

        💡 Лайфхак: Салат отлично освежает в жару.
        ⏱ Время приготовления: ~10 мин"""
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
        "name": "🥣 Греческий йогурт с ягодами",
        "recipe": """Ингредиенты:
    - 150 г греческого йогурта
    - 50 г любых ягод (клубника, черника)
    - 1 ч.л. меда

    Приготовление:
    1. Выложите йогурт в миску.
    2. Добавьте ягоды.
    3. Полейте медом и перемешайте.
    💡 Лайфхак: Можно добавить немного орехов или семян чиа для текстуры.
    ⏱ Время приготовления: ~3 мин"""
    },
    {
        "name": "🥑 Тост с авокадо",
        "recipe": """Ингредиенты:
    - 1 спелый авокадо
    - 1 ломтик хлеба
    - Сок лимона по вкусу
    - Соль, перец

    Приготовление:
    1. Разомните авокадо с лимоном, солью и перцем.
    2. Намажьте на поджаренный тост.
    💡 Лайфхак: Можно добавить тонко нарезанные помидоры или яйцо пашот сверху.
    ⏱ Время приготовления: ~5 мин"""
    },
    {
        "name": "🥗 Салат из огурцов и укропа",
        "recipe": """Ингредиенты:
    - 1 огурец
    - Несколько веточек укропа
    - 1 ст.л. оливкового масла
    - Соль по вкусу

    Приготовление:
    1. Нарежьте огурец тонкими кружочками.
    2. Мелко нарежьте укроп.
    3. Смешайте овощи, заправьте маслом и солью.
    💡 Лайфхак: Можно добавить немного лимонного сока для свежести.
    ⏱ Время приготовления: ~5 мин"""
    },
    {
        "name": "🍏 Фруктовый салат",
        "recipe": """Ингредиенты:
    - 1 яблоко
    - 1 банан
    - 1 апельсин
    - Немного меда

    Приготовление:
    1. Нарежьте фрукты небольшими кубиками.
    2. Смешайте в миске.
    3. Полейте медом и перемешайте.
    💡 Лайфхак: Добавьте немного мяты для аромата.
    ⏱ Время приготовления: ~5 мин"""
    },
    {
        "name": "🍌 Банановый смузи",
        "recipe": """Ингредиенты:
    - 1 банан
    - 150 мл молока или йогурта
    - 1 ч.л. меда

    Приготовление:
    1. Нарежьте банан.
    2. Смешайте банан, молоко и мед в блендере.
    3. Взбейте до однородной массы.
    💡 Лайфхак: Можно добавить немного корицы или какао для вкуса.
    ⏱ Время приготовления: ~3 мин"""
    },
    {
        "name": "🥕 Морковные палочки с хумусом",
        "recipe": """Ингредиенты:
    - 2 моркови
    - 50 г хумуса

    Приготовление:
    1. Нарежьте морковь длинными палочками.
    2. Подавайте с хумусом для макания.
    💡 Лайфхак: Можно добавить немного кунжута на хумус для аромата.
    ⏱ Время приготовления: ~5 мин"""
    },
    {
        "name": "🍞 Бутерброд с творогом и зеленью",
        "recipe": """Ингредиенты:
    - 2 ломтика хлеба
    - 50 г творога
    - Несколько веточек зелени
    - Соль по вкусу

    Приготовление:
    1. Намажьте творог на хлеб.
    2. Посыпьте мелко нарезанной зеленью.
    3. Добавьте соль по вкусу.
    💡 Лайфхак: Можно добавить немного ломтиков огурца для свежести.
    ⏱ Время приготовления: ~5 мин"""
    },
    {
        "name": "🥤 Кефир с ягодами",
        "recipe": """Ингредиенты:
    - 200 мл кефира
    - 50 г ягод
    - 1 ч.л. меда

    Приготовление:
    1. Выложите ягоды в стакан.
    2. Залейте кефиром.
    3. Добавьте мед и перемешайте.
    💡 Лайфхак: Можно добавить щепотку корицы для аромата.
    ⏱ Время приготовления: ~3 мин"""
    },
    {
        "name": "🍅 Быстрый салат Капрезе",
        "recipe": """Ингредиенты:
    - 1 помидор
    - 50 г сыра моцарелла
    - Несколько листиков базилика
    - 1 ч.л. бальзамического уксуса

    Приготовление:
    1. Нарежьте помидор и сыр кружочками.
    2. Выложите слоями, чередуя с базиликом.
    3. Полейте бальзамическим уксусом.
    💡 Лайфхак: Можно добавить немного оливкового масла для вкуса.
    ⏱ Время приготовления: ~5 мин"""
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
