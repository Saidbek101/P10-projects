from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

share_contact_btn = ReplyKeyboardMarkup(resize_keyboard=True)
share_contact_btn.add(KeyboardButton('Telefon raqamni yuborish', request_contact=True))

# Yes or no , confirm btn
confirm_data_btn = InlineKeyboardButton('Saqlash', callback_data='confirm_yes')
no_confirm_btn = InlineKeyboardButton('Qaytadan yuborish', callback_data='confirm_no')
yes_or_no_inline_btn = InlineKeyboardMarkup()
yes_or_no_inline_btn.add(no_confirm_btn)
yes_or_no_inline_btn.add(confirm_data_btn)

courser_btn = InlineKeyboardMarkup()
python_course = InlineKeyboardButton('Python Backend', callback_data='course_pb')
java_course = InlineKeyboardButton('Java Backend', callback_data='course_jb')
foundation_course = InlineKeyboardButton('Foundation', callback_data='course_fn')
flutter_course = InlineKeyboardButton('Flutter', callback_data='course_fl')
courser_btn.add(java_course)
courser_btn.add(flutter_course)
courser_btn.add(python_course)
courser_btn.add(foundation_course)