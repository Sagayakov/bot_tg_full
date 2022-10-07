from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
#ReplyKeyboardRemove удаляет клаву после использования

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Прайс')
#b4 = KeyboardButton('Поделиться номером', request_contact=True)
#b5 = KeyboardButton('Поделиться местоположением', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) #one_time_keyboard=True прячет клаву

kb_client.add(b1).row(b2, b3)
#.add(x) один в строке / .row(x1,x2..) все в строку / .insert(x) компанует