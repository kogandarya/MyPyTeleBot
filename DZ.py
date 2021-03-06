# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    dz1_ResponseHandler = lambda message: bot.send_message(chat_id, f"Привет, {message.text}!")
    my_input(bot, chat_id, "Как Вас зовут?", dz1_ResponseHandler)
# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько Вам лет?", dz2_ResponseHandler)

def dz2_ResponseHandler(bot, chat_id, age_int):
    bot.send_message(chat_id, text=f"Привет, друг! Тебе {age_int} лет? Выглядишь прекрасно!")
# -----------------------------------------------------------------------
def dz3(bot, chat_id):
    dz3_ResponseHandler = lambda message: bot.send_message(chat_id, f"{message.text * 4 + message.text}")
    my_input(bot, chat_id, "Как Вас зовут?", dz3_ResponseHandler)
# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    dz4_ResponseHandler = lambda message: bot.send_message(chat_id, f"Привет, {message.text}! Рад знакомству!")
    my_input(bot, chat_id, "Как Вас зовут?", dz4_ResponseHandler)
# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько вам лет?", dz5_ResponseHandler)

def dz5_ResponseHandler(bot, chat_id, age_int):
    bot.send_message(chat_id, text=f"О! тебе уже {age_int}! \nА через год будет уже {age_int+1}!!!")
# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    dz6_ResponseHandler = lambda message: bot.send_message(chat_id, f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", dz6_ResponseHandler)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)
# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):

    # bot.send_message(chat_id, text=botGames.GameRPS_Multiplayer.name, reply_markup=types.ReplyKeyboardRemove())

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)
    # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, ResponseHandler)  # то-же самое, но короче

def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)  # это не рекурсия, но очень похоже
        # у нас пара процедур, которые вызывают друг-друга, пока пользователь не введёт корректные данные,
        # и тогда этот цикл прервётся, и управление перейдёт "наружу", в ResponseHandler

# -----------------------------------------------------------------------
